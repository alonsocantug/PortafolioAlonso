# -*- coding: utf-8 -*-
"""Generador del sitio estático (ES/EN). Uso: python3 build.py   (SITE_URL=https://tu-dominio.com para sitemap y hreflang absolutos)
Sin dependencias de Node: jinja2 + markdown-it-py + Pillow. La estructura (content/, templates/, static/) se puede migrar a Astro."""
import os, re, json, shutil, unicodedata, html
from pathlib import Path
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markdown_it import MarkdownIt
from PIL import Image
import data as D

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
SITE = os.environ.get("SITE_URL", "").rstrip("/")

# ---------------------------------------------------------------- imágenes
IMG_SRC = ROOT / "assets" / "img"
_img_cache = {}

def process_image(name):
    if name in _img_cache:
        return _img_cache[name]
    src = IMG_SRC / f"{name}.png"
    im = Image.open(src).convert("RGBA") if Image.open(src).mode in ("RGBA", "P", "LA") else Image.open(src).convert("RGB")
    w, h = im.size
    base = (960, 1600) if w >= 2000 else (480, 960, 1600)
    widths = sorted({x for x in base if x < w} | {min(w, 1600)})
    out = DIST / "img"
    out.mkdir(parents=True, exist_ok=True)
    for x in widths:
        r = im if x == w else im.resize((x, round(h * x / w)), Image.LANCZOS)
        r.save(out / f"{name}-{x}.webp", "WEBP", quality=90, method=6)
    _img_cache[name] = (widths, w, h)
    return _img_cache[name]

def picture(name, alt, sizes="(min-width: 70rem) 1120px, 100vw", eager=False):
    widths, w, h = process_image(name)
    srcset = ", ".join(f"/img/{name}-{x}.webp {x}w" for x in widths)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="/img/{name}-{widths[-1]}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'width="{w}" height="{h}" alt="{html.escape(alt, quote=True)}" {load}>')

# ---------------------------------------------------------------- markdown
def slug(text):
    t = unicodedata.normalize("NFKD", text)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")

def make_md(lang, toc):
    md = MarkdownIt("commonmark").enable("table")
    t = D.UI[lang]

    def image(tokens, idx, options, env):
        tok = tokens[idx]
        src = tok.attrGet("src")
        alt = tok.content
        if src.startswith("img:"):
            return "<figure>" + picture(src[4:], alt) + "</figure>"
        return f'<img src="{src}" alt="{html.escape(alt, quote=True)}">'
    md.renderer.rules["image"] = image

    def heading_open(tokens, idx, options, env):
        tok = tokens[idx]
        text = tokens[idx + 1].content
        sid = slug(text)
        tok.attrSet("id", sid)
        if tok.tag == "h2":
            toc.append((sid, text))
        return md.renderer.renderToken(tokens, idx, options, env)
    md.renderer.rules["heading_open"] = heading_open

    def link_open(tokens, idx, options, env):
        tok = tokens[idx]
        href = tok.attrGet("href") or ""
        if href.startswith("http"):
            tok.attrSet("rel", "noopener")
        return md.renderer.renderToken(tokens, idx, options, env)
    md.renderer.rules["link_open"] = link_open

    md.renderer.rules["table_open"] = lambda tk, i, o, e: f'<div class="table-wrap" tabindex="0" role="region" aria-label="{t["table_label"]}"><table>'
    md.renderer.rules["table_close"] = lambda tk, i, o, e: "</table></div>"
    return md

def load_case(lang, key):
    raw = (ROOT / "content" / lang / f"{key}.md").read_text(encoding="utf-8")
    _, fm, body = raw.split("---", 2)
    meta = yaml.safe_load(fm)
    toc = []
    md = make_md(lang, toc)
    return meta, md.render(body.strip()), toc

# ---------------------------------------------------------------- sitio
env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))

def path_of(lang, key):
    return f"/{lang}/{D.ROUTES[key][lang]}"

def write(rel, content):
    p = DIST / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

PAGES = []  # (lang, key) para el sitemap

def render(lang, key, template, section, title, description, **ctx):
    other = "en" if lang == "es" else "es"
    alt_path = path_of(other, key)
    alternates = [(lang, SITE + path_of(lang, key)), (other, SITE + alt_path), ("x-default", SITE + path_of("es", key))]
    html_out = env.get_template(template).render(
        lang=lang, t=D.UI[lang], title=title, description=description, section=section,
        href=lambda k: path_of(lang, k), alt_href=alt_path, alternates=alternates,
        anchors=D.ANCHORS[lang], email=D.EMAIL, linkedin=D.LINKEDIN, behance=D.BEHANCE, **ctx)
    write(f"{lang}/{D.ROUTES[key][lang]}index.html", html_out)
    PAGES.append((lang, key))

def projects_for(lang):
    t = D.UI[lang]
    return [
        dict(title=t["p_wy_title"], text=t["p_wy_text"], tags=t["p_wy_tags"], facts=t["p_wy_facts"], main=True,
             image=picture("wy-card", t["p_wy_alt"], sizes="(min-width: 48em) 55vw, 100vw"),
             href=path_of(lang, "with-you"), cta=t["read_case"]),
        dict(title=t["p_fi_title"], text=t["p_fi_text"], tags=t["p_fi_tags"], facts=t["p_fi_facts"],
             image=picture("fi-card", t["p_fi_alt"], sizes="(min-width: 48em) 50vw, 100vw"),
             href=path_of(lang, "firmia"), cta=t["read_case"]),
        dict(title=t["p_ds_title"], text=t["p_ds_text"], tags=t["p_ds_tags"], pending=True,
             href=D.BEHANCE, cta=t["see_behance"]),
    ]

def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    shutil.copytree(ROOT / "static", DIST, dirs_exist_ok=True)

    for lang in ("es", "en"):
        t = D.UI[lang]
        projs = projects_for(lang)
        jsonld = json.dumps({
            "@context": "https://schema.org", "@type": "Person", "name": "Alonso Cantú",
            "jobTitle": t["hero_role"], "address": {"@type": "PostalAddress", "addressLocality": "Monterrey", "addressRegion": "Nuevo León", "addressCountry": "MX"},
            "sameAs": [D.LINKEDIN, D.BEHANCE], "knowsLanguage": ["es", "en"],
        }, ensure_ascii=False)
        render(lang, "home", "home.html", "home", t["home_title"], t["home_desc"], projects=projs, jsonld=jsonld,
               hero_img=picture("wy-hero", t["hero_alt"], sizes="(min-width: 64em) 45vw, 100vw", eager=True))
        render(lang, "projects", "projects.html", "projects", t["projects_title"], t["projects_desc"], projects=projs)
        for key in ("with-you", "firmia"):
            meta, body, toc = load_case(lang, key)
            hero = picture(meta["hero"], meta["hero_alt"], sizes="(min-width: 70rem) 1120px, 100vw", eager=True) if meta.get("hero") else None
            embed = None
            if meta.get("embed") and meta.get("prototype"):
                embed = meta["prototype"].replace("://www.figma.com/proto/", "://embed.figma.com/proto/") + "&embed-host=share&hide-ui=1"
            render(lang, key, "case.html", "projects", meta["page_title"], meta["description"], meta=meta, body=body, toc=toc, hero=hero, embed=embed)
        render(lang, "about", "about.html", "about", t["about_title"], t["about_desc"])
        render(lang, "cv", "cv.html", "cv", t["cv_title"], t["cv_desc"])

    write("index.html", env.get_template("root.html").render(base=SITE))
    write("404.html", env.get_template("404.html").render())
    write("robots.txt", "User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE}/sitemap.xml\n" if SITE else ""))
    if SITE:
        urls = [SITE + "/"] + [SITE + path_of(l, k) for l, k in PAGES]
        write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
              "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    print("OK:", len(PAGES), "páginas,", len(list((DIST / 'img').glob('*.webp'))), "imágenes")

if __name__ == "__main__":
    main()

# Portafolio · Alonso Cantú (ES/EN)

Sitio estático bilingüe. Contenido en `content/{es,en}/*.md`, textos de interfaz en `data.py`, plantillas en `templates/`, estilos y fuentes en `static/`.

## Compilar
    pip install jinja2 markdown-it-py pillow pyyaml
    SITE_URL=https://tu-sitio.vercel.app python3 build.py   # genera dist/ (SITE_URL activa sitemap y hreflang absolutos)
    cd dist && python3 -m http.server 8000                  # vista previa

## Publicar (GitHub + Vercel)
Vercel publica la carpeta `dist/` tal cual (ya compilada y incluida en el repositorio). No necesita build.
Si cambias contenido: `python3 build.py`, y sube de nuevo los archivos modificados.

## Pendiente
- Caso del Dashboard (hoy la tarjeta enlaza a Behance, "En preparación").
- Capturas reales de Figma para las imágenes de With You.
- Decidir si el correo se muestra públicamente (hoy sí; teléfono no).

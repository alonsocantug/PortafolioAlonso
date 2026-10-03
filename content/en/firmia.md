---
page_title: Firmia — Case study
description: B2B SaaS concept for carpentry and construction with interactive quotes that clients review and sign off on from any device. Landing page, quote preview and mobile flow.
title: Firmia
summary: A B2B SaaS concept that replaces PDF quotes with an interactive quote the client reviews and signs off on from any device. I designed the landing page, an interactive quote preview and a 7-screen mobile flow.
tags: ["Portfolio project", "Concept", "Individual"]
facts:
  - ["Role", "UX/UI: page structure, content, interface, components and contrast review"]
  - ["Tools", "Figma"]
  - ["Scope", "Desktop landing page (1440 px) with 5 sections and a kit of 7 components with hover states. As an extension, a 7-screen mobile flow for iPhone 16 with a prototype"]
  - ["Out of scope", "User research and usability testing"]
note_label: Note on method.
note: This is an interface design exercise on a concept, with no real client and no user research. The landing page figures (90%, 0 and 24/7), the quote number, the amounts and the contact details are examples, not measured results.
hero: fi-case
hero_alt: "Four Firmia mobile screens: my quotes, summary, sign-off and confirmation"
prototype: "https://www.figma.com/proto/QuFyeK4A08L6gaJjd4IzQT/Firmia-UX-UI?node-id=31-247&p=f&scaling=scale-down&content-scaling=fixed&page-id=29%3A212&starting-point-node-id=31%3A247&show-proto-sidebar=1"
---

## Problem and goal

**Concept hypothesis.** People who quote construction or carpentry work often send a static PDF that the client has to open, review and answer through another channel. The problem Firmia sets out is being able to review, adjust and approve a quote from anywhere and on any device, without relying on loose files. It is a design hypothesis: I did not validate it with interviews.

**Goal.** Design a page that explains the product in seconds and a clear quote preview where the client sees materials, labor, lead times, deposit and VAT, and can accept and sign, request changes or download a copy.

**Product scope.** The concept includes sharing the quote through messaging such as WhatsApp. That part is not designed in this file.

## Design

The landing page follows an order meant to let someone in the trade understand the product without reading more than needed: promise, benefits, evidence and process.

**1. Hero.** A headline with the promise ("Construction and carpentry quotes approved instantly"), a sentence explaining the change from PDFs, and two actions with a clear hierarchy: "Ver un presupuesto en vivo" (see a live quote) as the primary action and "Cómo funciona" (how it works) as the secondary one. The tilted card on the right shows a quote for the same folio that appears further down.

![Firmia landing hero with headline, two actions and a quote card](img:fi-hero)

**2. Benefits.** Six cards with an icon, a short title and one sentence: itemized materials, instant sign-off, clear lead times, project history, accessibility, and use on site and in the workshop. The cards can be read in any order.

![Benefits section with six cards](img:fi-features)

**3. How it works.** Three numbered steps that follow the real journey: site survey and quote, review by client and architect, and sign-off.

![How it works section with three numbered steps](img:fi-how)

**Style decisions.** A dark hero with amber and warm brown accents that echo wood, and light sections for dense content. Primary buttons are 56 px tall so they are easy to see and tap.

## Interactive quote preview

This is the centerpiece of the project: a card that replaces the PDF and that the client can review before deciding.

![Quote preview for the Encino kitchen fabrication and installation with breakdown, deposit, total and three actions](img:fi-preview)

**What the client sees, in order.**

1. The project, the quote number, who issues it and the status ("Pending approval").
2. Who the client is, where the site is and who the responsible architect is.
3. The breakdown in two blocks: materials and hardware, and labor and workshop, with quantity, unit price and subtotal.
4. Lead times (12 business days of fabrication and 3 of installation) and deposit terms (60% to start and 40% on delivery).
5. The summary: materials subtotal ($58,280.00), labor subtotal ($16,320.00), general subtotal ($74,600.00), 16% VAT ($11,936.00) and project total ($86,536.00).
6. Three actions: accept and sign off, request changes or download a copy.

**Design decisions.**

- Numbers are right-aligned and subtotals are bold, to compare at a glance.
- The total is separated and is the largest text in the summary, because it is the first thing a decision maker looks for.
- The primary action is a solid "Accept and sign"; "Request changes" has an outline and "Download copy" is the least prominent, so a doubt does not force an acceptance.
- A note below explains what is recorded on acceptance: the signature, the date and the deposit terms.

**Verified math.** I checked every line: materials $58,280 + labor $16,320 = $74,600; plus VAT of $11,936 gives $86,536. The quote number, amounts and names are examples.

## Mobile extension: the client flow

After the landing page, I designed the client's mobile journey as an exercise; the original case had left it out. It is an extension: I did not validate it with users or a usability test.

**What I designed.** Seven screens for iPhone 16 (393 × 852 px): a home with "My quotes", access from the link, summary, breakdown, request changes, sign-off and confirmation. The Figma prototype has two entry points: the direct link the client receives and the app home.

[View the interactive prototype in Figma](https://www.figma.com/proto/QuFyeK4A08L6gaJjd4IzQT/Firmia-UX-UI?node-id=31-247&p=f&scaling=scale-down&content-scaling=fixed&page-id=29%3A212&starting-point-node-id=31%3A247&show-proto-sidebar=1)

![Firmia mobile screens: home, access, summary and breakdown](img:fi-movil-a)

![Firmia mobile screens: request changes, sign-off and confirmation](img:fi-movil-b)

**Design decisions.**

- A linear path instead of a menu: the client arrives from a link, reviews and signs. The bottom menu appears only on the home; inside the flow there is none, so nothing competes with the primary action.
- One primary action per screen (solid button) and one secondary with an outline. Requesting changes is always one tap away, so a doubt does not force a signature.
- A back arrow and a "Step 1 of 3" indicator on summary, breakdown and sign-off, because what gets signed is a commitment involving money.
- On the sign-off screen, a checkbox that repeats the quote number and the total, so the signer sees exactly what they accept.
- Touch targets of at least 44 px and iPhone 16 safe areas (59 px at the top and 34 px at the bottom).
- Unlike the landing kit, the mobile system has variables and text styles with proper names, and reusable components: buttons, status tags, line items, top bar, progress and bottom menu.

**Accessibility.** I measured the contrast of the main pairs: secondary text #6B645F on #FAFAF9, 5.56:1; white on the #92400E button, 7.09:1; "Pendiente" tag, 8.15:1; "Firmado" tag, 6.49:1; focus ring, 6.79:1. #6B645F resolves the gray that failed on the landing page. I designed focus states on the options and the checkbox. I did not test with a screen reader or the real focus order, and I designed only one screen size.

**Example data.** The breakdown line items, the 60% deposit ($51,921.60 on a total of $86,536) and the "Closet vestidor" quote are examples, as on the landing page.

## Accessibility

I measured the contrast of the main color pairs against WCAG 2.1 AA (4.5:1 minimum for normal text).

| Pair | Ratio | Result |
|---|---|---|
| Dark text on the hero amber button (#1C1917 on #D97706) | 5.49:1 | Pass |
| White on "Solicitar demo" (#FFFFFF on #92400E) | 7.09:1 | Pass |
| Yellow stats on the hero (#FBBF24 on #1C1917) | 10.48:1 | Pass |
| Light gray on the hero (#A8A29E on #1C1917) | 6.93:1 | Pass |
| Secondary gray on white (#78716C on #FFFFFF) | 4.80:1 | Pass |
| Secondary gray on #FAFAF9 | 4.59:1 | Pass |
| Secondary gray on #F5F5F4 | 4.40:1 | Fails for small text |
| "Pendiente" tag (#78350F on #FEF3C7) | 8.15:1 | Pass |

**What I found.** The secondary gray (#78716C) drops to 4.40:1 on the #F5F5F4 background of the preview section. The fix is to darken it to #6B645F, which gives 5.33:1 on that background and 5.81:1 on white. The mobile extension already uses #6B645F; on the landing page it remains a pending improvement in the file.

**What I did not measure.** I did not check every text; there are 11 px texts in the details and footer that deserve a separate review. On the landing page I also did not design focus states or keyboard navigation, although it lists them as a benefit; I did design focus states later, in the mobile extension.

## Learnings and what I would do differently

- **Checking my own numbers.** When auditing the project I found that the hero showed a different total than the preview for the same quote, and that the hero sum did not add up. I fixed it so both cards show $86,536.00. I learned that in a product about money, consistent figures are part of trust.
- **Promise only what I designed.** The landing page says it is responsive and keyboard accessible, but in the original design only the desktop version existed and there were no focus states. I later designed the mobile flow and focus states, but the landing page still has no mobile version. What I would do differently: design the mobile version first, because the product promises use on site, then the focus states, and only then write the promise.
- **Talk to the people who quote.** I framed the problem as a hypothesis. Next time I would interview carpenters and contractors to learn how they quote and get paid today, and what they need to sign off from the site, before drawing the first screen.
- **Example figures, labeled.** The hero statistics (90%, 0 and 24/7) are examples. In a real case I would replace them with measured data or remove them.
- **A more complete system.** The landing kit has seven components with hover states. It lacks focus, disabled and error states, and color variables with proper names instead of the automatic ones; the mobile system already covers part of that.

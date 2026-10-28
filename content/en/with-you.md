---
page_title: With You — Case study
description: Mobile app for guided 3–5 minute breathing to lower anxiety. An individual portfolio project, from research to design system.
title: With You
summary: A mobile app that leads to a guided 3–5 minute breathing exercise to lower anxiety. I designed it end to end, from research to design system.
tags: ["Portfolio project", "Individual", "Mobile app"]
facts:
  - ["Role", "End-to-end UX/UI and Product Design: research, synthesis, flows, wireframes, UI, prototype, testing and design system"]
  - ["Duration", "3 weeks"]
  - ["Tools", "Figma, FigJam, Maze"]
  - ["Research", "Literature review and 4 video-call interviews (about 10 min each); 2 personas"]
  - ["Testing", "Real moderated usability test: 4 participants (acquaintances), 10 to 15 min per session, Maze and interviews"]
  - ["Design system", "44-component UI Kit and v1.1 Design System with 48 variables, applied to the screens"]
note_label: Note on method.
note: This is a practice exercise with no real client. The research combined a literature review and 4 real video-call interviews, about 10 minutes each, with bootcamp classmates; the two personas (Sofía and Diego) came out of them. The usability test was real, with 4 participants, all people I know, in sessions I ran myself with Maze and interviews; it is a small, non-representative sample, so it guides decisions but has no statistical value. The photographs of the people are illustrative. The interface, the prototype and the design system are real work and can be reviewed in Figma.
hero: wy-case
hero_alt: "Five With You screens on phones: welcome, home, guided breathing, mood log and progress"
embed: true
prototype: "https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8735-3732&p=f&t=kgGgzBfNxlV73m9J-1&scaling=scale-down&content-scaling=fixed&page-id=194%3A839&starting-point-node-id=8735%3A3732"
---

## Problem and goal

According to the WHO, in 2023 there were 470 million people with an anxiety disorder and 322 million with depression; nearly 1 in 7 people (1.2 billion) lived with a mental disorder ([WHO, mental disorders fact sheet, updated 11 September 2026](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)).

**Starting hypothesis.** A person with anxiety needs to recover calm in a few minutes, without configuring anything and without interrupting their routine. The literature supports slow breathing and short sessions; the rest (simplicity, mood logging) are design decisions that I later tested with people.

**Goal.** Design a mobile app that helps reduce anxiety and stress with guided breathing that is simple, quick and effective.

**Proposed solution.** Guided breathing sessions of 3 to 5 minutes, mood tracking, progress tracking and a simple, friendly interface.

## Research

*Literature review and 4 short interviews; see the note on method above.*

**Literature review.** I reviewed sources on anxiety and breathing: the [WHO](https://www.who.int/news-room/fact-sheets/detail/mental-disorders) for context, and three studies ([Balban et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873947), *Cell Reports Medicine*; [Luo et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11897343), *Scientific Reports*; [Iwabe et al., 2025](https://www.frontiersin.org/articles/10.3389/fnhum.2025.1605862), *Frontiers in Human Neuroscience*). Three ideas guided the design:

- Slow breathing reduces anxiety: with 6-second cycles, self-reported anxiety and arousal dropped (Luo et al., 2025), and with a 4 s inhale and 6 s exhale, state anxiety dropped (Iwabe et al., 2025).
- Short sessions may be enough: in a study of 108 people, 5 minutes a day for 28 days improved mood more than meditation, and participants practiced about 20 of the 28 days (Balban et al., 2023). That study does not compare durations, so With You's 3–5 minutes is a design decision that I later tested with users.
- That daily practice improved mood and reduced anxiety; in the same study sleep did not change, so the app does not promise better sleep from breathing (Balban et al., 2023).

**Interviews.** I held 4 video-call interviews, about 10 minutes each, with bootcamp classmates, to understand how they experience anxiety and what they would look for in a breathing app. It is a small sample close to me, so I use it to guide the design, not to generalize.

## Synthesis

**Key insight.** People need to recover calm in a few minutes without interrupting their daily routine.

The interviews and the literature produced five insights:

1. **Immediate access is essential.** People need to open the app and start breathing within seconds.
2. **Short sessions work best.** Sessions of 3 to 5 minutes fit daily routines.
3. **Simplicity reduces friction.** A clean, intuitive interface helps people focus on breathing.
4. **Tracking builds awareness.** Mood and progress tracking helps people see improvement.
5. **Personalization increases engagement.** Personalized content and recommendations make the experience more meaningful.

**Two personas**, built from the 4 interviews and the literature. Each quote is illustrative and sums up that person's need:

- **Sofía**, university student. Feels anxious before exams and deadlines. Wants to reduce anxiety and improve focus. Frustration: complex apps and long sessions. *"I just need something that helps me calm down when I feel overwhelmed."*
- **Diego**, student and freelance designer. Lives with too many deliverables and struggles to disconnect at the end of the day. Wants to sleep better and find moments of calm without altering his routine. *"When I feel overwhelmed, I need something that helps me clear my mind quickly."*

![Persona cards for Sofía and Diego with main need, goals and frustrations](img:wy-personas-en)

For each persona I built a journey map that showed me where calm is lost and where the app could help.

![Journey maps for Sofía and Diego: steps, emotion and pain point at each stage](img:wy-journey-en)

**Key decision.** A direct shortcut to guided breathing from the home screen, designed so the exercise can start in fewer than 4 taps. This is a design goal, not a measurement: with it I aim to reduce friction and increase the chance that a person finishes the session.

| Insight | Design decision |
|---|---|
| 1. Immediate access | "Respira ahora" (Breathe now) button on the home screen |
| 2. Short sessions | Short exercises by category |
| 3. Simplicity | Four tabs (Home, Exercises, My progress, Profile) and one main action per screen |
| 4. Tracking | Mood logging and a progress screen |
| 5. Personalization | Mood selector and recommended exercises on the home screen |

The usability test pointed the same way on three of these insights (immediate access, 3–5 minute sessions and seeing progress). I did not measure how simple the navigation is, nor personalization.

## Design

**Information architecture.** The app has four sections: Home ("Respira ahora", mood of the day, recommendations), Exercises (Anxiety, Stress, Focus, Sleep and relaxation), Emotional tracking (log mood, history, statistics) and Profile (data, goals, settings). The map also includes Help, with wellbeing tips and support resources, which I left out of the prototype as future scope.

![With You information architecture: Home, Exercises, Emotional tracking, Profile and Help with their subsections](img:wy-ia-en)

**User flows**, one per persona:

1. **Sofía, anxiety before an exam.** Opens With You, decides to start a session, chooses anxiety relief, completes the guided breathing and logs her mood. If she feels better, she goes back to studying; if not, the app suggests another session or exploring other tools.
2. **Diego, stress after a hectic day.** Opens With You, goes to Exercises, chooses stress relief, completes the session, logs his mood and checks his progress.

![Sofía's user flow, from opening the app to logging her mood and deciding whether to repeat the session](img:wy-flow-sofia-en)

![Diego's user flow, from opening the app to checking his progress](img:wy-flow-diego-en)

**Wireframes.** Four low-fidelity screens let me decide the structure before color: the navigation flow, quick access to the exercise, information hierarchy, mood logging, a visible timer during the session and the "Respira ahora" button as the main action.

![Four low-fidelity wireframes: home, progress and two steps of the guided breathing](img:wy-wireframes)

**High fidelity.** Four mobile screens in Spanish: Home (greeting, mood selector, recommended exercises and "Respira ahora"), Exercises (four categories with duration), My progress (completed sessions, streak days, average mood and sessions this week) and Profile.

![High-fidelity screens: Home, Exercises and My progress](img:wy-hifi)

**Prototype.** [Open it in Figma](https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8735-3732&p=f&t=kgGgzBfNxlV73m9J-1&scaling=scale-down&content-scaling=fixed&page-id=194%3A839&starting-point-node-id=8735%3A3732) and walk through the guided breathing flow.

**This page and Behance.** The Behance case shows the earlier version of the design. The prototype and screens on this page are version 2 (October 2026): “Respira ahora” went from a gradient button to a hero with a photo, the colors were corrected for contrast (the main blue went from 2.77:1 to 5.93:1, among other changes) and the UI Kit grew to 44 components with a 48-variable Design System. The detail of each change is in the Design System section.

## Usability test

*Real test with 4 participants; see the note on method above.*

**Method.** A moderated usability test on the mobile prototype to validate navigation, the breathing experience and overall usability. Four people close to me took part, in 10 to 15 minute sessions using Maze and interviews. I planned and ran it myself.

| Finding | Change |
|---|---|
| People expected to start a breathing session with a single tap | I redesigned the main "Respira ahora" button |
| They preferred sessions of 3 to 5 minutes | Short guided exercises became the default |
| They wanted to see their progress over time | I added visual tracking to the profile section |

![Home screen before (left) and after (right) the test: the Respira ahora button gains a background and the chosen mood is highlighted](img:wy-cambios)

**What I still don't know.** With 4 acquaintances I cannot generalize, and I did not measure task time or success rate. The changes respond to what I observed and what people said; they were not validated in a second round.

## Design System

**v1.0, the project UI Kit.** Poppins for headings and Inter for body, seven semantic colors (Primary, Anxiety, Stress, Sleep, Focus, Calm and Alert), a radius scale, two shadows and components such as exercise card, badges, progress bars, tab bar and avatar. Colors were painted by hand, without Figma variables.

![UI Kit v1.0: accent colors Primary, Anxiety, Stress, Sleep and Focus with their hex codes](img:wy-uikit)

**v1.1, later audit (September 2026).** I measured contrast against WCAG 2.2 AA and found failures I had not seen while designing. I rebuilt the kit in [a separate Figma file](https://www.figma.com/design/GHPCtHubSztEL1khHyVq3t) with four variable collections, nine text styles, two shadows and 11 components with states (focus, pressed, disabled). It was not tested with users.

**Applied to the screens (October 2026).** When I took the screens to Hi-Fi v2, I brought everything into the project file. The UI Kit grew to 44 components (70 counting their variants) in six sections, and v1.1 became a "Design System" page with 48 variables in four collections. I corrected the colors in the UI Kit styles and in the Design System variables with the same values, so the screens, the kit and the system match. These are the changes I measured on the screens:

| Element | Before | Now |
|---|---|---|
| Buttons, links and active tab | White on #0EA5E9, 2.77:1 | #0369A1, 5.93:1 |
| Secondary text | #717182, 4.51 to 4.79:1 | #5F6472, 5.56 to 5.91:1 |
| Hang-up button | White on #EF4444, 3.76:1 | #DC2626, 4.83:1 |
| Calendar numbers on green and orange | White, 2.54 and 2.80:1 | #111111, 7.44 and 6.74:1 |
| Progress figures (12 and 5) | #10B981 and #F97316 on white, 2.54 and 2.80:1 | #047857 and #C2410C, 5.48 and 5.18:1 |

![The project Design System: color variables for text, surface, border, action, categories, calm and tabs, with their corrected codes](img:wy-ds-color)

Other v1.1 fixes live in the Design System components and are not on the screens yet: badges with safe text colors (4.76 to 6.34:1), 44 px small buttons, a ✓ mark on the selected mood and states for focus, pressed and disabled. The earlier "Respira ahora" had 1.82 to 2.91:1 with white text on a gradient; in Hi-Fi v2 I replaced it with a hero with a photo. I measured the white text over the photo: the title and subtitle are 7.15:1 or higher at the worst point, and I darkened the "Recomendado" tag background because it dropped to 3.52:1 over the bright glints and is now 11.12:1 at minimum.

**Expanded UI Kit in the project file.** It has 15 color styles, 21 text styles, two shadows and four radii (10, 14, 18 and 20 px). Its six sections are navigation and headers, buttons and forms, cards, lists and calendar, mood, and icons and breathing. The components are linked to the prototype screens, such as the exercise card with thumbnail, the breathing hero with photo, the mood selector and the list row.

![UI Kit foundations: 15 color styles, text styles in Poppins and Inter, two shadows and four radii](img:wy-kit-fund)

![Card components: exercise, recommended, average mood, progress, goal, weekly chart, container, thumbnail and breathing hero](img:wy-kit-cards)

![Mood components: emojis, mood tiles with selected state and selectors](img:wy-kit-mood)

![Button and form components: primary button with states, secondary and danger, toggle, text field and notes](img:wy-kit-forms)

![Navigation components: top bar, logo, tab, tab bar and profile menu](img:wy-kit-nav)

![List rows and calendar days with mood state, plus brain icon, pause and play button, avatar and mini emojis](img:wy-kit-lists)

## Learnings and what I would do differently

Designing With You left me four lessons and a clear list of what I would do differently.

- **I talked to real people, but people close to me and in short sessions.** The 4 interviews of about 10 minutes and the test with 4 acquaintances taught me to ask, moderate, observe and turn a finding into a change. Next time I would run longer interviews, with about 5 people living with anxiety who are not close to me, with a script, consent and an analysis template, and measure task success and time to compare against my assumptions.
- **Auditing my own work found what I had not seen.** "Respira ahora" had a contrast of 1.82 to 2.91:1 with white text, far below the 4.5:1 of WCAG AA, even though I had listed "accessible" as a principle. v1.1 fixed it to 4.93–7.88:1 and, on the final screens, the main blue went from 2.77 to 5.93:1. Now I measure contrast at the moment I choose a color, not at the end.
- **Color and emoji are not enough.** The mood selector relied on them; in the Design System I added a ✓ mark to the chosen state and 44 px touch targets, because a person in a moment of anxiety needs to know without doubt what they chose.
- **A design system without variables does not scale.** v1.0 had hand-painted colors. The project Design System has 48 variables in 4 collections, 21 text styles shared with the kit and 11 component sections with states, and every contrast decision is documented.
- **What I still need.** Test the corrected colors with real users, bring the ✓ mark and 44 px targets to the screens, replace the placeholder icons.

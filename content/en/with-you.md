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
  - ["Research", "Literature review and 2 simulated interviews; 2 fictional personas"]
  - ["Testing", "3 simulated users in Maze, 3 tasks"]
  - ["Design system", "UI Kit v1.0 and v1.1 audit with variables and 11 components"]
note_label: Note on method.
note: This is a practice exercise with no real client. The interviews, the personas (Sofía and Diego) and the Maze usability tests were simulated to walk through the full process, so their results illustrate the method and have no statistical value. The photographs of the people are illustrative. The interface, the prototype and the design system are real work and can be reviewed in Figma.
prototype: "https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8457-3245&p=f&t=DD39fRHHVm9bnTrB-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=8457%3A3232"
---

## Problem and goal

According to the WHO, in 2023 there were 470 million people with an anxiety disorder and 322 million with depression; nearly 1 in 7 people (1.2 billion) lived with a mental disorder ([WHO, mental disorders fact sheet, updated 11 September 2026](https://www.who.int/news-room/fact-sheets/detail/mental-disorders)).

In the two simulated interviews, the apps people had already tried failed for the same reasons: too many features, long sessions, or built for meditation rather than fast calm. One person also doubted whether they were breathing correctly.

**Goal.** Design a mobile app that helps reduce anxiety and stress with guided breathing that is simple, quick and effective.

**Proposed solution.** Guided breathing sessions of 3 to 5 minutes, mood tracking, progress tracking and a simple, friendly interface.

## Research

*Practice interviews and personas; see the note on method above.*

**Literature review.** I reviewed sources on anxiety and breathing: the [WHO](https://www.who.int/news-room/fact-sheets/detail/mental-disorders) for context, and three studies ([Balban et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC9873947), *Cell Reports Medicine*; [Luo et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC11897343), *Scientific Reports*; [Iwabe et al., 2025](https://www.frontiersin.org/articles/10.3389/fnhum.2025.1605862), *Frontiers in Human Neuroscience*). Three ideas guided the design:

- Slow breathing reduces anxiety: with 6-second cycles, self-reported anxiety and arousal dropped (Luo et al., 2025), and with a 4 s inhale and 6 s exhale, state anxiety dropped (Iwabe et al., 2025).
- Short sessions may be enough: in a study of 108 people, 5 minutes a day for 28 days improved mood more than meditation, and participants practiced about 20 of the 28 days (Balban et al., 2023). That study does not compare durations, so With You's 3–5 minutes is a design decision supported by the interviews.
- That daily practice improved mood and reduced anxiety; in the same study sleep did not change, so the app does not promise better sleep from breathing (Balban et al., 2023).

**Simulated interviews.** Two university students. I wanted to know how they handle anxiety today, which strategies they use and what they would expect from a wellbeing app.

| Topic | Sofía | Diego |
|---|---|---|
| When it appears | Several jobs at once or an important exam | University deadlines while clients wait for work |
| What they do today | Music, TikTok; tries to breathe deeply without knowing if she does it right | Music or going out; keeps thinking about the same thing |
| Previous apps | Dropped one because it had too many things | Some were long or more about meditating than calming down fast |
| What they expect | Open the app and start without much setup | Something simple: open, breathe and go back to what he was doing |
| Duration | About 5 minutes | Between 3 and 5 minutes |
| Tracking | See whether it improves over time | Know how much he breathed and compare the week |

## Synthesis

**Key insight.** People need to recover calm in a few minutes without interrupting their daily routine.

The two interviews produced four findings: they look for a fast way to calm down, they prefer simple apps, they consider 3–5 minute sessions ideal, and they like keeping a record of how they feel.

**Two fictional personas**, built from those simulated interviews:

- **Sofía**, university student. Feels anxious before exams and deadlines. Wants to reduce anxiety and improve focus. Frustration: complex apps and long sessions. *"I just need something that helps me calm down when I feel overwhelmed."*
- **Diego**, student and freelance designer. Lives with too many deliverables and struggles to disconnect at the end of the day. Wants to sleep better and find moments of calm without altering his routine. *"When I feel overwhelmed, I need something that helps me clear my mind quickly."*

![Persona cards for Sofía and Diego with main need, goals and frustrations](img:wy-personas-en)

For each persona I built a journey map that showed me where calm is lost and where the app could help.

![Journey maps for Sofía and Diego: steps, emotion and pain point at each stage](img:wy-journey-en)

**Key decision.** A direct shortcut to guided breathing from the home screen, designed so the exercise can start in fewer than 4 taps. This is a design goal, not a measurement: with it I aim to reduce friction and increase the chance that a person finishes the session.

| Finding | Design decision |
|---|---|
| They want to calm down fast | "Respira ahora" (Breathe now) button on the home screen |
| They prefer simple apps | Four tabs (Home, Exercises, My progress, Profile) and one main action per screen |
| 3–5 minute sessions | Short exercises by category |
| They like tracking | Mood logging and a progress screen |

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

**Prototype.** [Open it in Figma](https://www.figma.com/proto/ueVtfaqiM6nx04cCVxwbIT/With-you-app_Alonso-Cant%C3%BA?node-id=8457-3245&p=f&t=DD39fRHHVm9bnTrB-1&scaling=scale-down&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=8457%3A3232) and walk through the guided breathing flow.

## Usability test

*Practice test with 3 fictional users in Maze; see the note on method above.*

| Task | Result |
|---|---|
| 1. Start a guided breathing session | All 3 found the main button in about 8 seconds |
| 2. Log their mood when finished | All 3 completed the log without help; one person suggested marking which one was chosen |
| 3. Check their session progress | Two took a few seconds to find the section and all 3 were confused by "Historial" |

**Findings.** The main navigation is intuitive and "Respira ahora" stands out. Mood logging is simple, although it is not clear which icon was selected. "Historial" is confusing and people want to see their progress clearly.

**Changes.**

1. "Mi historial" was renamed **"Mi progreso"**.
2. The **"Respira ahora"** button became more prominent and gained a background that highlights the chosen emotion.

![Home screen before (left) and after (right) the test: the Respira ahora button gains a background and the chosen mood is highlighted](img:wy-cambios)

The finding about the selected icon was left unresolved in this version; I picked it up in the design system audit.

## Design System

**v1.0, the project UI Kit.** Poppins for headings and Inter for body, seven semantic colors (Primary, Anxiety, Stress, Sleep, Focus, Calm and Alert), a radius scale, two shadows and components such as exercise card, badges, progress bars, tab bar and avatar. Colors were painted by hand, without Figma variables.

![UI Kit v1.0: accent colors Primary, Anxiety, Stress, Sleep and Focus with their hex codes](img:wy-uikit)

**v1.1, later audit (September 2026).** I measured contrast against WCAG 2.2 AA and found failures I had not seen while designing. I rebuilt the kit in [a new Figma file](https://www.figma.com/design/GHPCtHubSztEL1khHyVq3t) with four variable collections, nine text styles, two shadows and 11 components with states (focus, pressed, disabled). It was not tested with users.

| Element | v1.0 | v1.1 |
|---|---|---|
| "Respira ahora" text | White on gradient, 1.82 to 2.91:1 | Text #083028, 4.93 to 7.88:1 |
| Category badges | 2.33 to 3.55:1 | Safe text colors, 4.76 to 6.34:1 |
| Active tab | Blue #007AFF, 4.02:1 | #0369A1 with top indicator, 5.93:1 |
| Selected mood | White on light blue, 2.77 to 4.10:1 | #0369A1 with ✓ mark, 5.93:1 |
| Secondary text | Black at 30 to 50%, 2.09 to 3.92:1 | #5F6472, 5.56:1 |
| Small buttons | 30 and 36 px | 44 px |
| Minimum text | 9 and 10 px | 11 and 12 px |

## Learnings and what I would do differently

Designing With You left me four lessons and a clear list of what I would do differently.

- **I designed the process well, but I missed talking to real people.** I practiced each stage with simulated interviews and tests, and that taught me to structure questions, synthesize and turn a finding into a change. Next time I would run a real round with about 5 people living with anxiety, with a script, consent and an analysis template, and compare what changes against what I had assumed.
- **Auditing my own work found what I had not seen.** "Respira ahora" had a contrast of 1.82 to 2.91:1 with white text, far below the 4.5:1 of WCAG AA, even though I had listed "accessible" as a principle. I fixed it to 4.93–7.88:1. Now I measure contrast at the moment I choose a color, not at the end.
- **Color and emoji are not enough.** The mood selector relied on them; I added a ✓ mark to the chosen state and 44 px touch targets, because a person in a moment of anxiety needs to know without doubt what they chose.
- **A design system without variables does not scale.** v1.0 had hand-painted colors. v1.1 has 4 variable collections, 9 text styles and 11 components with states, and every contrast decision is documented.
- **What I still need.** Test v1.1 with real users and replace the placeholder icons.

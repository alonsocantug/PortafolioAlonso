---
page_title: WhatsApp reminders for a clinic — Case study
description: Appointment reminders and booking requests over WhatsApp for a dermatology clinic, with a review of the conversational content and accessibility. Pilot proposal, tested with example data.
title: WhatsApp appointment reminders and booking requests for a clinic
summary: A system that every evening messages patients who have an appointment the next day on WhatsApp and lets them confirm, reschedule or request an appointment with buttons. I proposed it to a dermatology clinic, built it with Make, Google Sheets and the official WhatsApp platform, and reviewed every message the way the patient experiences it.
tags: ["Proposal to a real client", "Individual", "Pilot not started"]
facts:
  - ["Role", "Conversation design, automation build, documentation and commercial proposal"]
  - ["Tools", "WhatsApp Business Platform (Meta), Make, Google Sheets"]
  - ["Scope", "Daily reminder with buttons, menu, appointment request, rescheduling, follow-up, opt-out and front-desk alert"]
  - ["Out of scope", "Real-time availability scheduling, an AI assistant and medical software integration (quoted separately)"]
note_label: Note on status.
note: I built and tested it with Meta's test number, an example schedule and my own phone. There are no real patients and no metrics yet, so I do not claim any reduction in no-shows. The names, phone numbers and appointments in the images are fictional. I do not publish the clinic's name or prices.
hero: wa-card-en
hero_alt: "Two phones with example messages: a reminder with Confirm and Reschedule buttons, and a menu with three buttons"
---

## Problem and goal

**The problem.** When a patient forgets an appointment, the clinic loses that slot and its revenue. The front desk also spends time every day calling or messaging people one by one to confirm. With 20 appointments a day and 2 minutes per confirmation, that is about 40 minutes a day, close to 3 hours a week (an example calculation from the proposal, not a measurement from the clinic).

**The goal.** The schedule alerts patients on its own, they reply with one tap, and the front desk can focus on the people in the clinic. The system does not replace the front desk: it removes the repetitive work and always leaves a way to reach a person.

## How it works

There are two flows. The first runs once a day; the second answers when the patient writes.

![Diagram with two flows: daily reminders from the schedule and replies to patient messages](img:wa-flow)

**Reminders.** Every evening the system looks in the schedule for next-day appointments with no reminder sent and no opt-out, sends a Meta-approved template with name, date, time and doctor, and marks in the schedule that it already sent it so the message is not repeated.

**Replies.** The patient taps Confirm or Reschedule, or writes to the clinic and gets a menu with three buttons: request an appointment, hours and location, and front desk. To request an appointment they pick a service, a day and a time of day with lists and buttons. The request is saved in the sheet and the front desk confirms it, because the system does not reserve slots by itself yet.

This is how it looks in the patient's chat, with fictional data. The texts were written in Spanish and are translated here, and the opt-out text is illustrative:

![Four phones with example messages: reminder and confirmation, rescheduling with a date list, requesting an appointment and opting out](img:wa-chats-en)

**Privacy.** The message only carries name, date, time and doctor, never the reason for the visit, and the sheet the automation reads has no diagnosis columns. It only messages people who gave consent, and anyone who writes BAJA (opt out) stops receiving messages.

## Iterating on the conversational content

Once the system worked, I reviewed every message the way the patient experiences it, from start to finish. I found four problems that could cause real mistakes and several of tone and clarity. I fixed them and tested them with real messages to my own phone. The messages themselves are in Spanish; I translate them here.

| Message | Before | After | Why |
|---|---|---|---|
| Reschedule from the reminder | "We cancelled your appointment tomorrow" | "No problem, Sofía. We let the front desk know you need to change your appointment. Which day suits you better?", with the date list | The text said "cancelled" when the patient asked to reschedule, and the schedule said something else |
| Follow-up with history | "Your last appointment was 10/16/2026", although that appointment was the next day | Takes the most recent past appointment and shows it with the weekday | A wrong fact in a health message erodes trust in the whole system |
| Follow-up without history | No message was sent | "We found no previous appointments with this number. Is this your first visit?", with two buttons | Silence reads as a failure. Every path must end in a reply and a way out |
| Date list | 16/10/2026, 17/10/2026… | Friday, Oct. 16, with no Sundays or days without consultations | People think "on Friday", and offering closed days creates impossible requests |
| Main menu | "Type 1 to book or 2 to talk to the front desk" | Three buttons: Request appointment, Hours and location, Front desk | It was the only step that required typing. I added the most frequent question |
| Talk to the front desk | "Someone from the front desk will be with you in a moment" | "They will contact you here during opening hours" | "In a moment" is a promise that is not kept at night |
| Patient name | The WhatsApp profile name | The name in the schedule | A relative can book from their number, and a profile name can be a nickname |

## Accessibility review

In a second round I checked how each message sounds with a screen reader, how an older person reads it, and how clear it is without relying on emojis. The clinic is in Mexico, so the 12-hour clock and Spanish date formats below refer to Spanish-language messages.

- **Dates.** In lists, "Viernes 16 de oct." instead of "Vie 16/10", which the reader pronounced as "sixteen slash ten". In messages, the full month, because there is no character limit there.
- **Times.** 12-hour format ("4:00 p.m."), which is how most people in Mexico say the time, especially older people.
- **Confirmations.** With labels and a final period (Day, Time, Doctor) so the reader pauses.
- **Emojis.** Each one sits next to a word that says the same thing. I removed the arrow emojis from the Follow-up dates, which the reader announced as "back button".
- **Time-of-day buttons.** Just "Morning" and "Afternoon", with the ranges written in the message.
- **Appointment request.** The message says it is a request and not yet a confirmed appointment, so nobody shows up to an appointment that does not exist.

## Design decisions

- **Lists and buttons instead of forms.** WhatsApp's native form (Flows) was blocked by Meta on the test account. Lists and buttons give a similar experience and work on any account.
- **Every reply carries its context.** Each option's identifier stores what the patient already chose, so the system does not need to remember the conversation or ask again.
- **Ask for the minimum.** Phone and name arrive with the message; the front desk fills in the rest when confirming.
- **Always a way to a person.** Every path offers talking to the front desk.
- **Informal "you" (tuteo).** I considered switching to the formal register for older patients and kept the informal one as a brand decision. Changing it means a new template approved by Meta, so it is pending confirmation with the clinic.

## Proposal and documentation

I prepared the pilot proposal for the clinic and three documents so the work can be repeated with another client:

1. **Client requirements.** A list of what the clinic must have before starting: a responsible person, accounts, a phone number, business details, payment, patient consent and schedule.
2. **Implementation checklist.** Ordered steps in 15 phases, with a table of known errors and their fixes, built from the failures I ran into while building it.
3. **How to explain it to the client.** A plain-language guide: what they gain, what they provide and what each part costs, and what not to promise, such as a percentage reduction in no-shows or a start date before Meta's approvals.

The proposal separates what is included from what is quoted separately, and proposes a three-month pilot in which the clinic shares metrics at 30 and 90 days. Since the pilot has not started, those metrics do not exist.

## What I do not know yet

- **Whether it works with real patients.** Everything was tested with Meta's test number. A real number still has to be registered and the business verified, and the current per-message rate for Mexico confirmed.
- **How much it reduces no-shows.** That is why the pilot first records the last month's no-shows and compares them at 30 and 90 days.
- **What the clinic prefers.** Informal or formal address, and the real hours, phone and address, which are examples today.
- **What happens with a real Follow-up date that falls on a Sunday.** The rule is built and still needs testing.

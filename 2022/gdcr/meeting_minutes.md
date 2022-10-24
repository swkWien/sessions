# Meeting Minutes

## 2022-10-24 Finalize Program

### TBDs

- [x] Eventbrite
  - [x] Stand der Anmeldung https://github.com/swkWien/sessions/issues/92
        Circa 20 Person
  - [x] Mandatory PCR Test?! https://github.com/swkWien/sessions/issues/96
        Verpflichtend!
  - [x] Fragen wie Personen auf Event gestoßen sind?
        Wie bist du auf Event gestoßen.
- [x] Program
  - [x] Claus macht allgemeine Moderation
  - Weiter siehe unten.

### TBD with respect to program

Key questions:
- Are you in? -> Yes
- Who is doing which session? -> See below.
- Do we want to create a fork? -> Yes

The group agrees on...
- Yes, we want "decoupled design" as overarching topic
- Yes, we use SupermarketReceipt kata
- While the sessions are progressive topic-wise,
  each session starts from scratch

Facilitators:
1. Session: "Pen & Paper" by Peter
2. Session: "Facing Reality" by Katrin & Patrick
3. Session: "Untangling the Knot" by Adam
4. Session: "SOLID" by Claus
5. Session: "TBD" by Roland (mit Peter)


## 2022-09-16 Program Discussion

### Participants
- Adam
- Claus
- Katrin
- Peter
- Rea
- Roland

### Notes
- Kurze Vorstellungsrunde
- Peter, hast du an jemanden gedacht bei "Budget für Facilitator"? Zu spät, machen wir selber. Als Idee für nächstes Jahr andenken. Reisebudget + Entschädigung (500€?); auch Verhandlungssache, cool, weil dann gäbe es was neues. Für heuer kein TODO.
- Was ist eure Meinung zu Covid Policy? Amtliche Vorgaben. Bitte testen aber nicht prüfen?
- Wir planen Webseite als primären Einstiegspunkt. Jemand Einwände? Kein Einwände. Landing Page ;)
- Mögliche Themen
  - **Hexagonal**
  - OO vs FP
  - *Brutal*
- Diskussion zum Thema
  - Hexagonal zu anspruchsvoll? Was spricht Personen an?
- Hexagonal für Beginner, Aspekte
  - Separation of Concerns
  - Decoupling
  - Dependency Injection
  - Inversion of Control
- Fokus: Software Design
  - Wir enden bei Hexagonaler Architektur
- Welches Kata?
  - Wir nehmen das selbe Kata.
  - Das selbe für den ganzen Tag?
  - Falls es Sinn macht, das Kata wechseln
- Timetable: copy-pase letztes Jahr
- Siehe auch https://github.com/swkWien/sessions/issues/85
- Notes from GDCR 2021 https://docs.google.com/document/d/1ya50ifaiG8a2b6_J-oypsIHfTrMrDF20lu4ekC_TPZI

### Sketch

**Kata**

TBD
Bspw. Snake
Multiplayer

**1. Session: Pen and Paper**

kürzere Session

Constraint/Frage:
Welche Aktionen gibt es? Evtl. geben wir Kategorien vor. Dann ergeben sich vielleicht Aspekte die man später trennen möchte.
Welche Subdomains gibt es?
Welche Events gibt es?
Welche Akteure gibt es?
Welche Concerns gibt es?
Analyse.

**2. Session: TDD (Outside in für alle die wollen)**

TDD, Pair Programming mit Ping Pong
Optional: plus Design Constraint

**3. Session: Dependency Injection**

Viele Kollaborateure weil kleine Units (wenig Zeilen, wenig Attribute, Object Calisthenics, ...)
Alle Kollaborateure im Konstruktor.

**4. Session: Inversion of Control (beachten Mittagspause)**

Wir wollen, dass man Interfaces verwendet (depend on abstraction)
Domain Logik darf keine konkrete Abhängigkeit auf I/O oder andere System Boundaries haben.

Steuern, an welchem Teil man arbeiten soll (Aspekt vorgeben), damit man schnell ein Interface braucht
Geben einen Teil der Architektur vor

**5. Session: Ports and Adapters**

TDD outside in
Ports and Adapters
Im Sinn von

https://github.com/swkBerlin/ports-and-adapters

- The application itself does not depend directly on any external systems, but only on ports
- The protocol for a port is given by the purpose of the conversation it describes
- For each external system there is an ‘’adapter’’ that converts the API definition to the format needed by that system and vice versa


### TODO/TBD
- Landing Page erstellen (Claus, Rea, noch wer?)
- Landing Page auf GDCR-Seite verlinken

### FOLLOW UP
- Restliche Details


## 2022-09-15 Orga

### Participants
- Roland
- Claus
- Rea
- Katrin

### Notes
- Vorstellungsrunde
- Rea macht nächste Woche ein Dojo
- Vieles ähnlich machen wie letztes Jahr
- Tickets via Eventbrite mit Refund @Roland
- Verpflegung macht Nagarro
  - Frühstück @Roland
  - Deewan @Roland
- Roland und Katrin könnten sich Facilitator Rolle vorstellen
- Wir haben wieder den Trackt
- Bis max 50 Personen
- Aktuell keine Covid-Vorgaben
- Roland braucht keine Unterstützung seitens swkWien
- Irgendwas, das wir morgen mitbedenken sollen? Nein.
- Ziel: so viel letztes Jahr aber mehr Leute.
- **Stärkerer Fokus auf Outreach**
  - Newcomer
  - Diversity
- Reisbudget für Facilitator noch unklar.
- Roland tendiert zu wechselnden Facilitator
- **Webseite als Anlaufstelle für alles**
  - Logo

### TODO/TBD
- @Roland: Schutzhause Meidling
  - Bitte um vegane Speisen
- @Roland: Deewan
- @Roland: Frühstück
- @Roland: Tickets
  - Inkl. Anmeldung
- @Roland: Logos für Website und Ankündigung

### FOLLOW UP
- Frühstück im Zeitplan berücksichtigen.
- Programmentscheidung für Event (Ticket).
- Covid und Testen.


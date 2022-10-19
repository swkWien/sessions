# Program

Title: **Decoupled Design**

General considerations:
- Topic: Architecture
- Sessions: Following overarching topic, progressive
- Kata: Use a single kata for the entire day (avoid overhead, allow for progression)
- Target audience: Diverse, should be doable for beginners but provide enough
  challenge/room for experienced developers as well, e.g. through optional constraints

## Kata

**[Supermarket Receipt (Refactoring Kata)](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata)**

Possibly with slight modifications for our purposes (through fork).

Rationale for using this kata:
- It is a refactoring kata, hence there is starter code
- It is a system with input (catalogs for prices and discounts, involves IO),
  little bit of in-between logic and output (receipt, does not involve IO)
- Being able to retrieve data differently and being able to output a
  receipt to different formats is a natural requirement
- We can motivate design changes through requirements changes
- We can motivate design changes because of how the starter code looks
- We can use the requirements for pen & paper sessions
- We can use the starter code for a TDD intro session
  to warm up and identify design issues
- The Kata is available in many languages

The kata lends itself to discuss the following:
- How to introduce a new printer based on given ReceiptPrinter?
- How to untangle responsibilities between Teller and ShoppingCart?
- How to manage Catalog and discounts?
- Discarded: How to encapsulate business logic in ShoppingCart.handle_offers?

Claus:
Für mich sind folgende Fragen wichtig:
- Welche Design-orientierten Sessions gibt das Kata her?
- Wie sehr hängen wir an "hexagonal"? Macht es Sinn, evtl. den Fokus
  zu ändern, damit sie besser zum Kata passen?
- Wir könnten den Tag auch als "Decoupling Strategies" framen.

Meiner Meinung nach sollte die Design Änderung durch Änderungen in den
Anforderungen motiviert sein, weil das für alle Beteiligten leicht
nachzuvollziehen ist.

Hier sehe ich folgende Möglichkeiten:
- HTML Receipt (gibt schon, bietet sich an für "Introduce Layer")
- Feature Bundles (gibt schon, würde ich außer Acht lassen)
- Introduce Discount Catalog (könnte eine kleiner Änderung unsererseits sein)

## 1. Session: Sketching (Pen & Paper)

We get familiar with the requirements.
We introduce design as something to think about.
We try to sketch the system using pen and paper ("How would you do it?").
We identify components/parts/collaborators/actors that constitute the system.

Ideas for retro:
- How did you describe the design?
- Which components did you identify?
- Is there something like "no design"?
- ...

TODO:
- Description
- Constraints
- Facilitator

Claus:
Diese Session passt so.


## 2. Session: Facing Reality (Code Review, Refactoring, Pair Programming)

We face reality.
There is already code. It works, that's nice.
We identify design issues, we get into pair programming. The starter code makes that easy.
We get more familiar with the code by refactoring it.
We contrast how our initial design ideas relate to what we see.

Retro:
- Which design issues did you identify?
- On which part of the system did you work?
- How does you initial sketch compare to the implementation you saw?

TODO:
- Description
- Constraints
- Facilitator

Claus:
Diese Session passt so.


## n. Session: Untangling the Knot

Based on what we have seen in the previous session, we know we have
work to do before we can add new features.

We do preparatory refactoring.
Also, we ask ourselves "who is responsible for what?" and move code around to separate concerns.
We may introduce methods to highlight intent.

Claus:
Hier könnten wir Discount Katalog einführen.
Wir könnten die Verantwortlichkeiten zwischen Teller und ShoppingCart klären.
Sollen wir zu Beginn die für später geplanten neuen Features präsentieren?

TODO
- Description
- Constraints
- Facilitator


## n. Session: Decoupling with Dependency Injection and Inversion

Requirement change: "New Discount catalog" (mMn zu klein)

Now that we have clarified which component is responsible for what,
we are ready to decouple.

Claus:
Auf welchen fachlichen Part wollen wir die Aufmerksamkeit lenken?
Anleitung mit Erklärungen zu DIs.

TODO
- Description
- Constraints
- Facilitator


## Session: Introducing Layers

Requirement change: "New feature: HTML receipt"

We want a new HTML printer and at the same time try to avoid duplication.

To prepare for this change, we need to review ReceiptPrinter
to separate the parts that relate to the ASCII-template and
the parts that relate to data preparation.

We then split it up and introduce new classes.

The steps could look like:
1. Split ReceiptPrinter into ASCIIPrinter and Format
1. Split ASCIIPrinter into ASCIITemplate and Printer
1. Introduce Interface for template and let Printer use it
1. Introduce HTMLTemplate


## n. Session: Introducing Ports and Adapters

Claus
Wenn wir dorthin wollen, bieten sich fachlich für mich "nur" die
Kataloge (Preise und Discounts) an, weil hier der IO Part klar ist.
Ist das interessant genug? Nehmen wir mit Dependency Injection/Inversion
zu viel vorweg?

TODO
- Description
- Constraints
- Facilitator

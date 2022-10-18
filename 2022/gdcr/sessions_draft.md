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
- It is a system with input (catalogs for prices and discounts),
  little bit of in-between logic and output (receipt)
- Being able to retrieve data differently and being able to output a
  receipt to different formats is a natural requirement
- We can motivate design changes through requirements changes
- We can motivate design changes because of how the starter code looks
- We can use the requirements for pen & paper sessions
- We can use the starter code for a TDD intro session
- The Kata is available in many languages

Claus:
Beim Kata wichtig zu klären, welchen Branch wir nehmen.
Wenn wir auch den Printer angreifen wollen, evtl. den mit entsprechenden Tests.

Mögliche Requirement Changes
* Introduce Discount Catalog (neu, einfach)
* HTML Receipt (gibt es schon)

Mögliche Anpassung im Vergleich zum Original
* New feature discount bundles raus nehmen damit keine Verwirrung entsteht


## 1. Session: Sketching (Pen & Paper)

We get familiar with the requirements.
We introduce design as something to think about.
We try to sketch the system using pen and paper (how would you do it).
We identify components/parts/collaborators/actors that comprise the system.
What is the alternative to no design? Bad design.

TODO:
- Description
- Constraints
- Facilitator


## 2. Session: Facing Reality (Code Review, Refactoring, Pair Programming)

We face reality.
There is already code. It works, that's nice.
We get familiar with the code by refactoring it, we get into pair
programming. The starter code makes that easy.
We contrast how our initial design ideas relate to what we see.
We identify various properties and flaws.

Claus:
Siehe Teller bzw die zugehörigen Tests.
Hier kann Teil der Retro sein, auf welchen Aspekt sie sich fokussiert haben.
Manche der später angestrebten Änderungen werden womöglich vorweg
genommen, das ist okay.

TODO:
- Description
- Constraints
- Facilitator


## 3. Session: Untangling the Knot (Separation of Concerns)

Claus:
Zu Beginn dieser Session könnten wir die
angestrebten Requirement Changes einführen damit klar ist,
wohin die Reise geht.
Gleichzeitig wissen wir an dem Punkt schon, die Code Base
ist noch nicht bereit für neue Features.

We want to improve the design.
We do some preparatory refactoring.
We ask ourselves "who is responsible for what?", "what is weird? ;)" and move code around to separate concerns.
Also we introduce methods to highlight intent.

Claus
Man kann sich hier auf zwei unterschiedliche Aspekte fokussieren,
alles vor/nach dem Teller.
Vor dem Teller ist offensichtlicher finde ich weil der ReceiptPrinter
etwas mühsam zu lesen ist.

TODO
- Description
- Constraints
- Facilitator


## 4. Session: Introducing Dependency Injection & Dependency Inversion

Now that we have clarified which component is responsible for what,
we are ready to decouple.

We have the following strategies that we can apply:
- Inject dependencies
- (and/or go a step further) invert dependencies

We can do that easily for the teller with the catalog and discounts.

Claus
Zu den DIs gibt es Erklärung.
Auch hier wieder die beiden oben genannten Optionen um den inhaltlichen
Schwerpunkt zu setzen. Sollen wir das vorgeben?

TODO
- Description
- Constraints
- Facilitator


## 5. Session: Introducing Ports and Adapters

Claus
Fällt mir schwer. Sollten wir den fachlichen Schwerpunkt tauschen?
"Ports and Adapters" mit dem Input und "DIs" mit dem Output?

Using what we practiced already, we continue focusing
on another part of the system.

We try another strategy:
- We introduce a receipt* port
- We introduce adapters for different receipt representations

https://github.com/swkBerlin/ports-and-adapters

> - The application itself does not depend directly on any external systems, but only on ports
> - The protocol for a port is given by the purpose of the conversation it describes
> - For each external system there is an ‘’adapter’’ that converts the API definition to the format needed by that system and vice versa

This is only copy-paste, needs to be updated, as stated too abstract, requires context/background.

TODO
- Description
- Constraints
- Facilitator


## 5. Session: Alternativszenario

Im Moment kommen wir für mich nicht richtig bei "Ports and Adapters" an. Wenn du keinen passenden Weg findest...
Wenn man sich auf HTML Receipt fokussiert, ergibt sich dort ein neuer Zwischenschritt. Dann könnten wir quasi zwei Mal Session 4 machen
aber mit einem anderen fachlichen Schwerpunkt.

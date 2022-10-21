# Program

Title: **Decoupled Design**

General considerations:
- Topic: Software Design
- Sessions: Following overarching topic, progressive
- Kata: Use a single kata for the entire day (avoid overhead, allow for progression)
- Target audience: Diverse, should be doable for beginners but provide enough
  challenge/room for experienced developers as well, e.g. through optional constraints

## Kata

**[Supermarket Receipt (Refactoring Kata)](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata)**

Possibly with slight modifications for our purposes (through fork).

Rationale for using this kata:
- It is a refactoring kata, hence there is starter code
- We can safely evolve the system because we have tests
- It is a system with input (catalogs for prices and discounts, involves IO),
  little bit of convoluted in-between logic and output (receipt, does not involve IO)
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


## 1. Session: Sketching (Pen & Paper)

We get familiar with the requirements.
We introduce design as something to think about.
We try to sketch the system using pen and paper ("How would you do it?").
We identify components/parts/collaborators/actors that constitute the system.

[Beginning of requirements](http://codekata.com/kata/kata01-supermarket-pricing/)

Requirements limited to
* an_empty_shopping_cart
* one_normal_item, two_normal_items
* buy_two_get_one_free, buy_five_get_one_free
* item product i.e. book, loose_weight_product i.e. apple
* percent_discount
* xForY_discount, FiveForY_discount_withSix, FiveForY_discount_withFour

Task description/questions
* How would we design such a system?
  * Maybe verb-noun analysis.
  * Which actions/events are there?
* Specific questions to hint at the larger picture
  * Which domains/subdomains are involved?
  * Do we need to get data from somewhere? Do we need to write/print/format data somewhere?
  * Are Stock and Shop the same domain? No, how do we handle it?
  * Which "concerns" are there (if concern means anything to you)

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

Task description/questions
* Read the code ("read by refactoring")
* Which design elements (aka classes) are there?
* How are they connected? Which classes hold which data?
* Which classes are doing what?
* Compare with your diagrams from session 1.

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


## i. Session: Untangling the Knot

Based on what we have seen in the previous session, we know we have
work to do before we can add new features.

We do preparatory refactoring.
Also, we ask ourselves "who is responsible for what?" and move code around to separate concerns.
We may introduce methods to highlight intent.

We clarify responsibilities between Teller and ShoppingCart.
And maybe other places as well.

Task description/questions

* Reduce Coupling, improve Cohesion:
  * Put things that do the same thing together.
  * Separate things that are different into separate classes.

Maybe as hint during the session if few people are doing it:

* Hint: We clarify responsibilities between Teller and ShoppingCart. And maybe other places as well.
* Hint: What about Law of Demeter violations in `ReceiptPrinter`?

TODO
- Description
- Constraints
- Facilitator


## j. Session: Decoupling with SOLID (Dependency Injection and Inversion)

What if we had a requirement change: discounted bundles. We are not ready for that.

Now that we have clarified which component is responsible for what,
we are ready to decouple.

Task description/questions

* Can we decouple further? Let's follow the solid principles.
* All classes less than 50 LoC.
* Cart is not responsible for discounts. (SRP) - Already done.
* Discount calculation is not responsible for individual discounts.
* All collaborators are injected into the constructor. (OCP)
* All collaborators are behind interfaces. (DIP)
* Some classes might have multiple interfaces depending on their usage. (ISP)

Maybe as hint during the session if few people are doing it:

* Hint: `handleOffers` is doing too much.
* Hint: `printReceipt` is doing too much.
* Hint: Move code related to different discount options into subclasses.

TODO
- Description
- Constraints
- Facilitator


## k. Session: Introducing Layers

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


## l. Session: Introducing Layers/Modules (maybe even Ports and Adapters)

Peter: Ich sehe jetzt dass das Beispiel nicht ausreicht, weil es gibt keine Infrastruktur, so wie Roland auch schon gemeint hat. Printer und Teller sind nicht verbunden. Es gibt keinen Einstiegspunkt. Es ist auch zu viel Code um in allen Sprachen noch eine Main Klasse hinzuzufuegen. Seufz. Aber jetzt ist es zu spaet um noch umzulenken. Ich hab schon zu viel Zeit investiert. ;-)

Are we done we decoupling? What else could we do? We have separated classes. What about domains?

Task description/questions

* Create modules (packages, folder, depending on language) for infrastructure: formatting
* Make sure you have a layered infrastructure. The `ReceiptPrinter` concept is part of Sales, but the implementation to plain text is part of (command line) infrastructure.
* (maybe to end here) Now We want a new HTML printer and at the same time try to avoid duplication.
* Create modules (packages, folder, depending on language) for each different domain
concept (aka bounded context): Stock (Catalog and Products), Sales.

Maybe as addition  during the session if people are struggling:

* What is the functionality we use of the Catalog? We are only interested in prices. Let's have our own interface `ProductPrices` which simplifies the usage, maybe this is a reduced version of `Catalog`. (This is a driven port.)
* Create the adapter which implements `ProductPrices` and delegates to `Catalog`. (This is the adapter.)

Rules to validate against (maybe Retro questions):

* The application itself does not depend directly on any external systems, but only on ports.
* The protocol for a port is given by the purpose of the conversation it describes.
* For each external system there is an "adapter" that converts the API definition to the format needed by that system and vice versa.

TODO
- Description
- Constraints
- Facilitator

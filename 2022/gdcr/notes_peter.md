# Notes Peter CR

## Preparation

Every facilitator should work through the [kata](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) twice.

1. just refactor around and explore the code.
1. decouple stuff and  get to a clear architecture.

Bonus

* try the setup and learn about setup issues people will face
* maybe fix setup/code issues and send back PR to Emily

Then and only then read [Johan's facilitatorsNotes](https://github.com/martinsson/SupermarketReceipt-Refactoring-Kata/tree/facilitatorsNotes)

## Domain Supermarket Pricing

pricing goods at supermarket with all kind of discounts like

* three for a dollar (so what’s the price if I buy 4, or 5?)
* $1.99/pound (so what does 4 ounces cost?)
* buy two, get one free (so does the third item have a price?)

Domain Questions

* Does fractional money exist?
* tbd

### Subdomains

* Stock (Product, Unit, Catalog)
* Sales/Pricing (Price, Offer)
* Sales/Shopping (Cart, Quantity, Teller, Receipt/Discount)
* Math (percent and mod for discounts)
* Formatting/Layout/i18n (Printer)

## Existing Code

Existing code handles cases

* an_empty_shopping_cart
* one_normal_item, two_normal_items
* buy_two_get_one_free, buy_five_get_one_free
* loose_weight_product
* percent_discount
* xForY_discount, FiveForY_discount_withSix, FiveForY_discount_withFour

### Existing classes

* `Teller` is main entry class, maybe also the `Printer`.
* `Catalog` contains `Product`, `Product` has a `Unit`.
* `Teller` takes `Cart` and fills `Receipt`.
* `ReceiptPrinter` formats the `Receipt` for display.
* `Cart` calculates `Discount`s - `theCart.handleOffers(receipt, this.offers, this.catalog);` is offensive ;-)

### Existing Design

* Cart handles Discount, not in responsibility - inline this method in the teller.
* Printer violates Law of Demeter.

## Motto Software Design/ Decoupling

Application Architecture = Software Design. Design is here to allow change. Design should be decoupled.

Things we can decouple

* "Concerns" (UI, Logic, Storage, Printing) -> Separation of Concerns
* from creation (Open Closed Principle) -> Dependency Injection
* from public APIs (DIP, ISP) -> extract interfaces, interfaces based on client needs
* from other subdomains -> Bounded Contexts with ACL (like ports)
* from mutation -> functional core/imperative shell

### Hexagonal Architecture

Hexagonal is just "decoupling of certain things up to a certain higher level".

1. Concerns, so we end up with different classes for different "things", aka Logic, UI, etc.
1. DI, so we end up with collaborators independent in constructors.
1. Layering, we move collaborators into different components/packages based on technical infrastructure, hidden behind interfaces.
1. Slicing, we move collaborators into different components/packages based on domains.
1. Modules, we define the public APIs of the components with Facades (incoming or driven ports) and the data objects they provide or need.
1. Hexagon, we invert the dependencies for outgoing/driving collaborators by defining our own domain based abstraction (port) and an adapter connecting it to the API of the used module.

So we end (maybe) at Hexagonal Architecture

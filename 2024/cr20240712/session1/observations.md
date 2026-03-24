1. Iteration
Copy-paste from ChatGPT gives result
2. Iteration
Without context, new implementation not related to existing one
With context, implementation is correct but test cases fail
We are still in the same session

We change session:
* Code != functionality, i.e. how do we reference the existing implementation in the prompt
  how do we relate to it when we say it should be extended?
* New session leads to new implementation

We cannot prompt to force adjustment of existing tests
Again difficult to force the creation of a valid test case for a specific
requirement
By copy-pasting error messages, we finally get a "correct" test case

TBD:
* Effect of session (fresh vs ongoing)
* With or without tests

Comments
* Tasks with a lot of numbers, rules, etc. (complexity) it is tedious
  * Should we have used a different kata?
* Production code (algorithm) was correct but test cases were a trouble
  * Update old tests was tricky
  * Generating minimal tests for edge cases not as easy as expected
* Zu ungeduldig um das durchzuziehen (wo ist der Erfolg?)
* Mix von Feature vs Guiding Test
  * Sehr naheliegend, einfach alles in den prompt zu schmeiﬂen
  * ANdere Inkremente?
* Idee: TDD via prompting
  * Muss man aufpassen wegen Naming
* Idee: JetBrains AI ausprobieren
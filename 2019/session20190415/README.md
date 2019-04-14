# TCR: "test && commit || revert"

>I introduced “test && commit”, where every time the tests run correctly the code is committed.
>Oddmund Strømmer, the first programmer I’ve found as obsessed with symmetry as I am, suggested that if the tests failed the code should be reverted.

>The full command then is “test && commit || revert”. If the tests fail, then the code goes back to the state where the tests last passed.

For the full story, see [Kent Beck's blog post](https://medium.com/@kentbeck_7670/test-commit-revert-870bbd756864).


## Setup

To make `test && commit || revert` work as intended you need a setup to 
automate the procedure. Below is a very simple configuration. 
The example section refers to a JavaScript and Java setup.


Utility to `run_tests`:
```bash
#!/bin/sh

your-test-runner-executable
error=$?

exit $error
```

Utility to `git_commit` changes:
```bash
#!/bin/sh

git stage -A
git commit -m "working"

exit 0
```

Utility to `git_revert` changes:
```bash
#!/bin/sh

git checkout -b broken_`date +%s`  # only if you want to keep your changes
git stage -A                       # only if you want to keep your changes
git commit -m "broken tests"'   '  # only if you want to keep your changes
git checkout master
```

Utility to `test && commit || revert`:
```bash
#!/bin/sh

./run_tests && ./git_commit || ./git_revert
```

### Examples

- [ladders.js: A ladders game for a "test && commit || revert" kata](https://github.com/dtanzer/ladders.js) by [dtanzer](https://github.com/dtanzer) and [codecop](https://github.com/codecop)
- [jLadders: A ladders game (in Java) for a "test && commit || revert" kata](https://github.com/dtanzer/jLadders) by [dtanzer](https://github.com/dtanzer) and [codecop](https://github.com/codecop)


## Kata

*Before you start, get your TCR setup running.*

If you want/need to exchanges code snippets, you can use this [Piratenpad](https://piratenpad.de/p/mkjGRMyWot19R9GolP) for copy-paste (use at own responsibility).

### 1. Round

We work on the [Tennis Refactorign Kata](https://github.com/emilybache/Tennis-Refactoring-Kata).
If you are not already familiar with this kata, start with the class "TennisGame1", otherwise choose the version you find most interesting.

### 2. Round

If you want to continue with a refactoring exercise do so, otherwise 
implement the scoring system from scratch using TCR.

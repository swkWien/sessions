# Quarto Learnings and Questions

`quarto render --output-dir` is ignored, unless the the content to render is part of a project.
To turn a directory into a project, run `create-project`; hence the `_quarto.yml`.

Is there a different way to compose slides from various files other that using the include directive?

You need to **run `quarto publish gh-pages` once**, see [here](https://github.com/quarto-dev/quarto-actions/blob/main/examples/example-01-basics.md). Seems to be doing quite a lot...

You can include fontawesome through an extension https://github.com/quarto-ext/fontawesome

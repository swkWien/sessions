# Global Day of Coderetreat 2023 by Softwerkskammer Wien

Hosted by [Nagarro](https://www.nagarro.com/de).

**Landing page and facilitation slides.**

## Contributing

### Setup

Download and install [Quarto](https://quarto.org/), a Markdown-oriented publishing system.

(Installation is only necessary if you want to build the slides locally. You can also inspect
the rendered slides [here](https://swkwien.github.io/gdcr23/).)

### Add Content

To add your showcase
1. Copy-paste `template/` folder in the `sessions/` directory and rename it after your showcase and your name,
   e.g. `demo_octopus`.
1. Adjust the `_content.qmd` according to guide your presentation/discussion.
1. Add a corresponding include directive in `index.qmd`.

*Feel free to adjust the template if you feel more comfortable with a different format. We do not aim for
identically looking presentations. However, please make sure that you answer the core questions regarding
your motivation of using the tools and your experience with them.*

### Learn more

Copy-pasting sections from other contributors should work just fine.
If you want to know more about Quarto, take a look at the official docs regarding
* [presentations](https://quarto.org/docs/presentations/) and at the
* [revealjs](https://quarto.org/docs/presentations/revealjs/) section if you want to leverage
  specific [reveal.js](https://revealjs.com/) features for your presentation.

To build/render the slides locally, run the `render.sh` or `render_on_save.sh` scripts
(or use whatever technique you prefer).

## Publishing

No action is required on your side. The slides are automatically build and deployed
using GitHub Actions.

## Authors

*If you contributed to this repository, add your name here.*

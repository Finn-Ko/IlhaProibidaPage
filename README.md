# Ilha Probida

This repository contains the result of a student project as part of the POO course at UFRJ
(see also https://github.com/kwarwp/radia and https://github.com/Finn-Ko/IlhaProibida).

We present this as the final result of the group Fogo.

The game can be accessed on the GitHub Page for this repository [here](https://finn-ko.github.io/IlhaProibidaPage/).

## Technologies

- Brython: the game logic is written using [Brython](https://brython.info/) (this does not need to be installed).
- Sphinx: for automated generation of html and md documentation from docstrings we use [Sphinx](https://www.sphinx-doc.org/en/master/).
- PyCharm: to run a local server and for ease of use it is highly recommended to install [PyCharm](https://www.jetbrains.com/pycharm/), 
however this is technically not mandatory.

## Usage

To run the game, simply start a webserver in this parent directory, you can do so easily by opening the `index.html` 
in PyCharm and then clicking on the icon referring to your browser in the top right of the editor.

For documentation generation the process is a bit more complicated:
As sphinx has trouble with the imports, it is best to comment all of the import statements in the code,
before running the automatic doc generation.
To do so, follow [this tutorial](https://stackoverflow.com/questions/36237477/python-docstrings-to-github-readme-md) to
autogenerate markdown files. This is best done in a `_docs` folder, which will be excluded by the gitignore automatically.
Generate html and md files and then copy the html and markdown folder in `_build/` into the actual `docs` folder.
Now you need to refactor the names of the three subdirectories to have the same name without the "`_`", because GitHub
Pages refuses to serve files in a directory starting with "`_`".

## Documentation

The documentation can either be found as a webpage [here](https://finn-ko.github.io/IlhaProibidaPage/docs/html/index.html), or as markdown [here](https://github.com/Finn-Ko/IlhaProibidaPage/blob/main/docs/markdown/index.md).

## Folder structure

This parent folder contains the `index.html`, as well as license details. 

The `page` folder contains everything necessary for the game page to work,
like the images under `page/img`, the python/brython code under 
`page/pySrc` and the `game.html` page, which displays the main game canvas.

The `docs` folder contains the documentation as html or md under `docs/[html, markdown]`.

The `.idea` folder contains IDE project information which comes in handy if you use PyCharm.
## Contributions

You are very welcome to help us out, by forking and creating a MR with new features or fixes. :)

## Known Bugs

While there is a huge amount of work still to be done until this is a finished product and we have a huge list of known
bugs, that we can't possibly completely list here, we want to note one that is
particularly annoying:

Sometimes loading the game page results in an "Aw, Snap!" error in chromium based browsers, preventing the entire
game to work. We are not able to pinpoint where this bug stems from, as it occurs only on some machines in some browsers.
If you have any suggestions, on the origins of this bug, please let us know. If you yourself experience the bug and just
want to see our product, try a different browser.


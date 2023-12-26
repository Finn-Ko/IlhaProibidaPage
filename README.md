# Ilha Probida

This repository contains the result of a student project as part of the POO course at UFRJ
(see also https://github.com/kwarwp/radia).

We present this as the final result of the group Fogo.

The game can be accessed on the GitHub Page for this repository [here](https://finn-ko.github.io/IlhaProibidaPage/).

## Technologies

- Brython: the game logic is written using [Brython](https://brython.info/)
- Sphinx: for automated generation of html and md documentation from docstrings we use [Sphinx](https://www.sphinx-doc.org/en/master/)
- PyCharm: to run a local server and for ease of use it is highly recommended to install [PyCharm](https://www.jetbrains.com/pycharm/), however this is technically not mandatory.

## Usage

To run the game, simply start a webserver in this parent directory, you can do so easily by opening the `index.html` 
in PyCharm and then clicking on the icon refering to your browser in the top right of the editor.

For documentation generation the process is a bit more complicated:
As sphinx has trouble with the imports, it is best to comment all of the import statements in the code,
before running the automatic doc generation.
To do so, simply run `make html`, or `make markdown` respectively in the `docs/` folder.
It is necessary to install the [sphinx markdown extension](https://pypi.org/project/sphinx-markdown-builder/) 
to also autogenerate .md files.

## Folder structure

This parent folder contains the `index.html`, as well as license details. 

The `page` folder contains everythin necesarry for the game page to work,
like the images under `page/img`, the python/brython code under 
`page/pySrc` and the `game.html` page, which displays the main game canvas.

The `docs` folder contains all the necessary files for the build process of the documentiation,
as well as the documentation as html under `docs/_build/[html, markdown]`.
These build files need to be included for the access under GitHub Pages to work, as well as to view the docs here
on GitHub as markdown.

## Contributions

You are very welcome to help us out, by forking and creating a MR with new features or fixes. :)


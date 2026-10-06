# Add tutorials, how-to guides and explanations

Written pages are Markdown files (`.md`) or Jupyter notebooks (`.ipynb`) stored in
your tool's folder. They become part of the site: same look, in the sidebar and
in the search.

## Where to put them

```
docs/tools/<your-tool>/
├── index.md            # what the tool is, when to use it
├── tutorials/
│   ├── index.md        # lists the pages of this folder
│   └── first-steps.md  # ← your pages go here
├── how-to/
│   ├── index.md
│   └── ...
├── explanation/
│   ├── index.md
│   └── ...
└── reference/
    └── index.md        # see the reference guides
```

Pick the folder by asking what the reader wants:

| The reader wants to... | Folder |
|---|---|
| learn the tool from zero, following along | `tutorials/` |
| get a specific task done | `how-to/` |
| understand why or how something works | `explanation/` |

## Add a page

1. Create the file, for example `docs/tools/<your-tool>/how-to/export-results.md`.
   Start it with a single `#` title:

   ````markdown
   # Export results to CSV

   Run:

   ```bash
   my-tool export --format csv results.csv
   ```
   ````

2. Add it to the list in the `index.md` of the same folder, **without** the `.md` extension:

   ````markdown
   ```{toctree}
   :maxdepth: 1

   measure-a-route
   export-results
   ```
   ````

   A page that is not listed there does not appear in the sidebar, and the build
   warns about it.

## Images

Put images next to the page, or in an `images/` subfolder, and reference them with
a relative path:

```markdown
![The export dialog](images/export-dialog.png)
```

## Notebooks

1. Put the `.ipynb` file in `tutorials/` (or `how-to/`).
2. **Run all cells and save the notebook with its outputs.** The site never runs
   notebooks, it shows what is saved in the file.
3. Add it to the folder's `index.md` like any page.

## Links

| Link to | Write |
|---|---|
| Another page | `[text](../how-to/export-results.md)` |
| A section of a page | `[text](../how-to/export-results.md#options)` |
| A Python object documented in this site | ``{func}`geokit.haversine` `` or ``{class}`geokit.Polygon` `` |
| A Python or NumPy object | ``{func}`numpy.mean` `` (resolved through intersphinx) |
| Any website | `[text](https://example.com)` |

## Useful blocks

````markdown
```{note}
Something the reader should know.
```

```{warning}
Something that can go wrong.
```

::::{tab-set}
:::{tab-item} Linux
...
:::
:::{tab-item} Windows
...
:::
::::
````

More options: [MyST syntax guide](https://myst-parser.readthedocs.io/en/latest/syntax/typography.html)
and [sphinx-design components](https://sphinx-design.readthedocs.io/en/latest/).

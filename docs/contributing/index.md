# Contributing to these docs

This section explains how to add a tool to the site or update its pages.
It is written for the developers of each tool.

## The two kinds of content

Every tool section has four parts. Three of them are **written pages** and one is the **reference**:

| Part | What it is | How it gets here |
|---|---|---|
| Tutorials | Learning by doing, step by step | You write Markdown pages in this repo. See [](written-pages.md). |
| How-to guides | Solving a specific task | Same as above. |
| Explanation | Concepts, background, design decisions | Same as above. |
| Reference | Exact facts: API, CLI options, endpoints | Depends on the tool, see below. |

## Which reference method to use

```{list-table}
:header-rows: 1
:widths: 40 60

* - Your tool
  - Reference method
* - Python package
  - Generated from the source code, nothing installed. See [](python-reference.md).
* - Any other tool **with** published docs (its own website, docs.rs, ReadTheDocs, Swagger UI of a service, third-party docs)
  - Link to them. See [](external-reference.md#option-a-link-to-published-docs).
* - Any other tool **without** published docs (Rust, TypeScript, C++, etc.)
  - Paste the HTML your doc generator produces. See [](external-reference.md#option-b-paste-generated-html).
* - Web application with no API (used only through its interface)
  - A hand-written reference page in Markdown (the screens, options and file formats), plus a link to the app.
```

## Checklist: add a new tool

1. Copy the folder of the most similar sample tool in `docs/tools/` and rename it,
   for example `docs/tools/my-tool/`.
2. Edit `docs/tools/my-tool/index.md`: what the tool is, when to use it, links.
3. Write or paste the written pages. See [](written-pages.md).
4. Set up the reference using the table above.
5. Add the tool to the sidebar: in `docs/index.md`, add `tools/my-tool/index` to
   the `Tools` toctree, and add a card for it in the grid.
6. Preview locally (below), then open a pull request.

## Preview your changes locally

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
sphinx-autobuild docs docs/_build/html --ignore docs/api --ignore docs/_sources
```

Open <http://127.0.0.1:8000>. The page reloads every time you save.

```{toctree}
:hidden:

written-pages
python-reference
external-reference
```

# Welcome

This repository builds a single public documentation site for the MultiRoofs project. It 
covers the project knowledge (concepts and background behind the project, such as 
digital twins) and the documentation of every tool used in the project, both in-house 
and third-party. Each tool section follows the
same structure: **Tutorials**, **How-to guides**, **Explanation** and **Reference**.
Developers can contribute written pages as Markdown files or notebooks. API references 
are either generated from the source code without installing anything (for Python 
tools), linked to the tool's own published docs, or pasted as pre-built HTML when no 
published docs exist. The site is built with Sphinx and rebuilds automatically on 
every push to the repository.

New here? Start with [Getting started](getting-started/index.md).
Adding or updating a tool? See [Contributing to these docs](contributing/index.md).

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} UICityJSON
:link: tools/geokit/index
:link-type: doc

In-house Python library and guide to extract a 3D model of buildings given LiDAR cloud of points
and building footprints.
+++
{bdg-secondary}`Python, Roofer`
:::

:::{grid-item-card} MRIO
:link: tools/mapview/index
:link-type: doc

In-house TypeScript library. Draws building footprints on a web map.
+++
{bdg-primary}`in-house` {bdg-secondary}`TypeScript` {bdg-light}`pasted reference`
:::

:::{grid-item-card} Roofy
:link: tools/inventory-api/index
:link-type: doc

In-house REST service. Stores and queries inventory items.
+++
{bdg-primary}`in-house` {bdg-secondary}`web service` {bdg-light}`linked reference`
:::

:::{grid-item-card} Urban Challenge assessment
:link: tools/numpy/index
:link-type: doc

Third-party library. How the project uses it, with links to the official docs.
+++
{bdg-warning}`third-party` {bdg-light}`linked reference`
:::
::::

```{toctree}
:hidden:
:caption: Project background

getting-started/index
```

```{toctree}
:hidden:
:caption: Tools

tools/geokit/index
tools/mapview/index
tools/inventory-api/index
tools/numpy/index
contributing/index
```

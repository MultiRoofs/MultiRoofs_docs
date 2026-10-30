# Welcome

MultiRoofs helps cities turn their rooftops into multifunctional spaces that address
urban challenges such as heat, flooding, energy demand, housing shortage, and
biodiversity loss. This site brings together the knowledge behind the project and the
documentation of the tools developed or used in it.

It is written for local authorities, trainers, data analysts, and developers working
on rooftop activation.

- **Project background** explains the concepts: the urban challenges cities face,
  what rooftops and buildings can offer, the owners and incentives that shape
  decisions, and the digital twins that support analysis.
- **Tools** explains how to install and use each MultiRoofs tool, from first
  tutorial to full reference.

New here? Start with [Getting started](getting-started/index.md).
Adding or updating a tool? See [Contributing to these docs](contributing/index.md).

::::{grid} 1 2 2 2
:gutter: 3

:::{grid-item-card} MultiRoofs Builder
:link: tools/CityJSON/index
:link-type: doc

In-house Python library and user guide to extract a 3D model of buildings given LiDAR cloud of points
and building footprints.
+++
{bdg-secondary}`Python, Roofer`
:::

:::{grid-item-card} MRIO
:link: tools/mrio/index
:link-type: doc

description
+++
{bdg-primary}`in-house` {bdg-secondary}`TypeScript` {bdg-light}`pasted reference`
:::

:::{grid-item-card} Roofy
:link: tools/roofy/index
:link-type: doc

description
+++
{bdg-primary}`in-house` {bdg-secondary}`web service` {bdg-light}`linked reference`
:::

:::{grid-item-card} Urban Challenges assessment
:link: tools/challenge_assessment/index
:link-type: doc

description
+++
{bdg-warning}`third-party` {bdg-light}`linked reference`
:::
::::

```{toctree}
:hidden:

getting-started/index
```

```{toctree}
:hidden:
:caption: Project background

about-multiroofs/index
urban-challenges/index
rooftops-and-buildings/index
owners-and-incentives/index
from-priorities-to-action/index
digital-twins/index
training-path/index
glossary/index
references/index
```

```{toctree}
:hidden:
:caption: Tools

tools/CityJSON/index
tools/mrio/index
tools/roofy/index
tools/challenge_assessment/index
contributing/index
```

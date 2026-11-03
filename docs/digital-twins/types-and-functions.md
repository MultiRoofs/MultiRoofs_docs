# Types and functions of digital twins

```{admonition} Learning objectives
:class: tip
After reading this page, you will be able to:
- Name the main types of digital twins, based on what they represent.
- Describe the three building blocks of a digital twin: data, model and software.
- Explain the main functions of a digital twin: describing, predicting and recommending.
```

## What can be twinned?

Digital twins can represent almost anything. Depending on what they mirror, four types are commonly distinguished ([Matta and Lugaresi, 2024](https://doi.org/10.1109/WSC63780.2024.10838793)):

| Type | What it mirrors | Main purpose | Urban example |
|---|---|---|---|
| **Product twin** | A single object across its life cycle | Improve design, use and maintenance | A building, or a solar installation on a roof |
| **System twin** | A set of parts working together | Improve operations, efficiency and costs | A drainage network, an energy grid, a traffic system |
| **Environment twin** | A place | Offer an immersive view in which the place can be explored and evaluated | A district or a whole city |
| **Biological twin** | A living being or biological system | Support health and life sciences | Urban vegetation or a green roof ecosystem |

City digital twins usually combine several types. A city twin can include product twins of individual buildings, system twins of infrastructure networks, and an environment twin of the city as a whole.

## The building blocks: data, model and software

Building on the general [Digital Twin cycle](./what-is-a-digital-twin.md) presented before, we can identify of three essential building blocks ([Zhang, 2024](https://doi.org/10.1007/978-3-031-51819-5)):

- **Data is the foundation.** A digital twin relies on historical and current data about its physical counterpart. Without reliable data, the twin cannot represent reality.
- **Models are the core.** Models turn data into understanding. *Theory-based models* follow known principles, such as physics. *Data-driven models* learn patterns from large amounts of data, for example with machine learning.
- **Software is the carrier.** Software makes the models usable and provides the interface between people, the physical world and the digital twin.


```{figure} ./images/data-model-software.png
:alt: Data, model, and software in a Digital Twin
:width: 100%
:align: center
:name: fig-data-model-software

Data, model, and software in a Digital Twin. Taken from [Zhang, Y. (2024)](https://doi.org/10.1007/978-3-031-51819-5).
```

## What a digital twin can do

The functions of a digital twin are delivered as **services** used by people or by other systems. They fall into three main groups.

### Describing: what is happening?

Descriptive services show the current state of the physical counterpart. They include visualisation, monitoring, performance indicators, alerts and dashboards.

*Rooftop example:* a 3D map showing every roof in a district, coloured by its current use, slope or solar irradiation.

### Predicting: what will happen?

Predictive services use models to estimate future states or test what-if scenarios. They are often combined with optimisation methods that search for the best configuration. Predictive analytics, based on data and machine learning, can also detect patterns and anticipate problems before they occur.

*Rooftop example:* estimating how much rainwater a district could retain, or how much energy it could produce, if a given share of its flat roofs became blue or yellow roofs.

### Recommending: what should we do?

Prescriptive services go one step further and suggest actions, for example by comparing scenarios against objectives.

*Rooftop example:* ranking roofs or districts where a green-blue combination would contribute most to reducing heat stress and flood risk.


```{figure} ./images/life-cycle-DT.png
:alt: Life cycle view of Digital Twins
:width: 100%
:align: center
:name: fig-life-cycle-dt

Life cycle view of Digital Twins. Reproduced from [Matta, A. and Lugaresi, G. (2024)](https://doi.org/10.1109/WSC63780.2024.10838793).
```

In MultiRoofs, the digital twin focuses on describing rooftop potential and comparing scenarios. Recommendations support the discussion, but decisions remain with the public authority.

```{admonition} Key takeaways
:class: important
- Digital twins can mirror products, systems, environments or living things; city twins combine several types.
- Every digital twin rests on data, models and software.
- Its functions describe the present, predict the future and recommend actions.
- In MultiRoofs, these functions support decisions; they do not replace them.
```

## Sources

- Matta, A. and Lugaresi, G. (2024). An introduction to digital twins. In *Proceedings of the 2024 Winter Simulation Conference*, <https://doi.org/10.1109/WSC63780.2024.10838793>.
- Zhang, Y. (2024). *Digital Twin: Architectures, Networks, and Applications*, Vol 16. Springer Nature, <https://doi.org/10.1007/978-3-031-51819-5>.
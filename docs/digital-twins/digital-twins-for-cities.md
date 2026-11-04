# Digital twins for cities and rooftops

```{admonition} Learning objectives
:class: tip
After reading this page, you will be able to:
- Describe how cities use digital twins.
- Give examples of urban digital twins relevant to rooftops.
- Explain what the MultiRoofs digital twin does and does not do.
- Identify trends that will shape urban digital twins.
```

## How cities use digital twins

Digital twins help cities plan, build and manage the urban environment. Common applications include:

- **Urban planning and land use.** Simulating plans before they are implemented, for example to optimise the location of housing, public transport, antennas or solar panels.
- **Mobility and housing.** Testing changes to traffic systems or new housing developments, and anticipating problems before they occur.
- **Sustainability and infrastructure.** Monitoring urban assets, supporting maintenance and analysing energy and climate performance.
- **Participation.** Giving residents and stakeholders a shared, visual picture of proposed changes, which makes it easier to discuss them.

Many urban digital twins remain fragmented: they are built project by project, at different scales, with little interaction between them. Shared data models and standards would allow them to work together and multiply their impact.

## Examples relevant to rooftops

**3DBAG, the Netherlands.** Developed by the 3D Geoinformation research group at TU Delft, 3DBAG is an open dataset containing 3D models of all buildings in the Netherlands, including LoD2.2 models with roof shapes. The models are generated automatically by combining two national open datasets: the building register (BAG) and the national elevation data (AHN). Such datasets are a foundation on which rooftop analyses can be built. <https://3dbag.nl>

**Helsinki Energy and Climate Atlas, Finland.** Based on Helsinki's semantic 3D city model, this free online service shows energy information for nearly every building in the city, and the solar energy potential of all roof and wall surfaces. Its open data supports property owners, city planners and companies offering energy services. <https://kartta.hel.fi/3d/atlas>

**Herrenberg, Germany.** The small city of Herrenberg developed an urban digital twin that combines a 3D city model with simulations, such as traffic and air flow, and uses it to involve residents in urban planning ([Dembski et al., 2020](https://doi.org/10.3390/su12062307)).

```{figure} ./images/3dbag.png
:alt: 3DBAG
:width: 100%
:align: center
:name: fig-3dbag

3DBAG view. <https://3dbag.nl>
```

## The MultiRoofs digital twin

In MultiRoofs, the digital twin is a data- and policy-driven set of tools that helps public authorities determine the best multifunctional use of specific roofs in their city.

**What it combines.** A 3D city model with LoD2.2 roof shapes, enriched with 2D GIS layers (for example heritage, flood, heat or green corridors), local priorities set by experts, and preferences collected from stakeholders during interactive sessions.

**How it is built.** Where cities already have LoD2.2 models, these are converted to CityJSON, the project's standard 3D format. Where they don't, models are reconstructed from building footprints and aerial LiDAR with Roofer, an open-source tool developed at TU Delft. Cities with limited data can start with open data and add more detail as their capacity grows.

**What it does.** It visualises the potential of rooftops, classifies them by possible functions using the seven-colour system, supports the comparison of scenarios, and serves as a communication tool between departments and with stakeholders.

**What it does not do.** It does not make decisions. The digital twin structures and informs judgement, shows where uncertainties remain, and leaves political and organisational choices to the public authority.

**Where it sits.** Following the classification in [What is a digital twin?](what-is-a-digital-twin.md), the MultiRoofs digital twin is closest to a **digital model or digital shadow** of the city's roofs: it is updated when new data becomes available, rather than continuously, and it informs people rather than acting on roofs directly. For planning decisions, this is appropriate: the building stock changes slowly, and the value lies in the analysis and the shared picture rather than in real-time control.

The [MultiRoofs Builder](../tools/CityJSON/index.md) supports the first step by generating 3D building models from LiDAR and building footprints. Then, additional attributes can be incorporated to the model by using [MRIO](../tools/mrio/index.md) and the resulting enriched CityJSON can be used to [visualize rooftop potential](../tools/roofy/index.md) and [align priorities](../tools/challenge_assessment/index.md) for its activation.

```{figure} ../about-multiroofs/images/mrtools.png
:alt: A diagram showing the MultiRoofs tools developed in the consortium.
:width: 80%
:align: center
:name: fig-mrtools

Set of tools developed in MultiRoofs (*work in progress*).
```

## Where digital twins are heading

Several trends will shape urban digital twins in the coming years:

- **Artificial intelligence.** Machine learning will automate more tasks, from reconstructing 3D buildings to detecting roof uses and predicting future conditions.
- **More sensors.** Wider use of connected sensors will make it possible to monitor rooftop performance, such as water retention, energy production or temperature.
- **More interaction.** Digital twins will become more interactive, making them easier to use for non-specialists and in participatory processes.
- **More autonomy, within limits.** In some fields, digital twins already take certain decisions automatically. In urban policy, where trade-offs involve public values, decisions will remain with people, supported by increasingly capable tools.

```{admonition} Key takeaways
:class: important
- Cities use digital twins for planning, infrastructure management, sustainability and participation.
- Open 3D building data and city models, such as 3DBAG and Helsinki's atlas, show what is possible for rooftop analysis.
- The MultiRoofs digital twin combines 3D models, GIS data, local priorities and stakeholder input to support, not replace, decisions.
- AI and sensors will expand what urban twins can do, but public choices stay human.
```

## Sources

- Dembski, F., Wössner, U., Letzgus, M., Ruddat, M. and Yamu, C. (2020). Urban digital twins for smart cities and citizens: the case study of Herrenberg, Germany. *Sustainability*, 12(6), 2307, <https://doi.org/10.3390/su12062307>.
- Sabri, S., Alexandridis, K. and Lee, N. (eds.) (2024). *Digital Twin: Fundamentals and applications*. Springer Nature Switzerland, <https://doi.org/10.1007/978-3-031-67778-6>.
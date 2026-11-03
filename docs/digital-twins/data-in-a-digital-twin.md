# Data in a digital twin

```{admonition} Learning objectives
:class: tip
After reading this page, you will be able to:
- List the main types of data used in an urban digital twin.
- Describe the three sources of data: dynamic, static and expert.
- Explain how data is collected, transferred and managed.
- Recognise the data MultiRoofs relies on.
```

## Types of data in an urban digital twin

An urban digital twin combines many kinds of data into one model of the city. Each type plays a different role.

| Data type | Role | Examples | Use in rooftop activation |
|---|---|---|---|
| **Foundational geospatial data** | Anchors all other data to real locations | Topographic and cadastral maps, satellite images, aerial photographs, GIS layers | Building footprints, parcel boundaries, district boundaries |
| **3D and elevation data** | Adds height and shape | LiDAR point clouds, 3D city models, building information models (BIM), digital elevation and terrain models | Roof shape, slope, height and area |
| **Real-time sensor data** | Shows current conditions | Internet of Things (IoT) sensors, weather stations, traffic counters | Soil moisture on green roofs, water levels in blue roofs, solar panel output |
| **Time series and historical data** | Reveals trends and feeds predictions | Energy use, water flows, rainfall and temperature records | Past rainfall extremes, heatwave frequency |
| **Infrastructure and operational data** | Describes how the built environment works | Water, energy and telecom networks, transport systems, asset performance | Grid capacity, sewer overflow points |
| **Environmental and climate data** | Supports sustainability analysis | Temperature, humidity, precipitation, vegetation cover, biodiversity | Heat maps, green corridors, flood maps |
| **Regulatory and compliance data** | Ensures alignment with rules | Ownership and cadastral data, building codes, permits, heritage protection | Heritage restrictions, height limits, owner types |
| **Demographic and socio-economic data** | Supports planning and policy | Population, land use, zoning, employment | Population density, lack of public facilities |
| **Predictive and simulation data** | Enables what-if analysis | Flood risk models, traffic models, climate and development scenarios | Rooftop scenarios for a district |

## Three sources of data

The data in a digital twin comes from three sources ([Matta and Lugaresi, 2024](https://doi.org/10.1109/WSC63780.2024.10838793)):

- **Dynamic data:** data that changes over time and is regularly updated from the physical world, such as sensor readings or new aerial surveys.
- **Static (baseline) data:** data used to build the model the first time, such as building footprints or the construction year.
- **Expert knowledge:** information provided by people, such as local priorities or the assessment of a planner.

MultiRoofs uses a similar distinction. Its digital twin relies on three data families:

- **Geospatial data** forms the objective basis for calculating rooftop capacity, by combining a 3D city model with 2D GIS layers.
- **Expert data** captures local needs, such as the urban challenges a city prioritises and the targets it sets.
- **Collaborative data** captures what stakeholders want, collected during interactive sessions in which participants set ambitions, draw activation zones and prioritise roofs.

## How data is collected

### Sensors

Data about the physical world can be collected in three ways:

- **Built-in sensors** are already part of the object or system, such as the inverter of a solar installation, a smart meter or a building management system. They are quick to use, but not available for every purpose.
- **Added sensors** are installed to collect extra information, such as soil moisture sensors on a green roof or water level sensors in a blue roof. They require extra hardware and maintenance.
- **Virtual sensors** estimate a feature that is hard to measure directly from other data. For example, roof slope and area can be derived from LiDAR, and the solar irradiation of a roof can be simulated from its shape, orientation and surroundings.

For city-wide analysis, most data does not come from sensors but from periodic surveys and registers: aerial LiDAR and imagery, cadastral data, building registers and municipal datasets.

### 3D building models and levels of detail

Rooftop analysis requires 3D models of buildings that represent the shape of their roofs. The level of detail (LoD) of a 3D model describes how much of the building's geometry it contains. LoD1 models represent buildings as blocks with flat tops, while LoD2 models include roof shapes. MultiRoofs works with **LoD2.2** models, which represent roof shapes in enough detail to analyse each roof surface. Where such models do not exist, they can be reconstructed automatically from building footprints and classified aerial LiDAR (preferably at least 10 points per m²).

See [3D city models and CityJSON](../tools/CityJSON/explanation/index.md) for more information.

## How data is transferred

Data must travel from its source to the digital twin. Two issues matter here:

- **Communication technology and protocols.** City sensors typically use wireless networks, from short-range technologies to cellular and low-power wide-area networks, and standard messaging protocols such as HTTP or MQTT. Datasets are best exchanged through standards-based services, such as OGC web services and APIs.
- **Security.** Data must be protected during transfer and storage, especially when it concerns people or critical infrastructure.

## How data is managed and analysed

Urban data is often **big data**: large in volume, fast-changing (velocity) and highly varied in format and source (variety). Managing it requires:

- **Storage.** Cloud storage offers accessibility, scalability and processing power. Local storage gives more control over security. Hybrid approaches combine both.
- **Integration.** Datasets from different sources must be combined, which requires common formats, coordinate reference systems and identifiers. MultiRoofs uses CityJSON as its standard 3D format and links datasets through persistent building identifiers, or by matching geometries where identifiers are missing.
- **Metadata.** Each dataset should describe its content, coverage, update frequency, licence and provenance, so that others can find and reuse it.
- **Privacy.** Some data, such as ownership or cadastral records, is personal or sensitive under the GDPR. It may require anonymisation, aggregation or controlled access.

```{admonition} Key takeaways
:class: important
- An urban digital twin combines geospatial, 3D, sensor, historical, infrastructure, environmental, regulatory, socio-economic and simulation data.
- Data comes from dynamic sources, static baselines and expert knowledge.
- For rooftop analysis, 3D building models with roof shapes (LoD2.2) are essential.
- Integration depends on standards, identifiers, metadata and careful handling of personal data.
```

## Sources

- Armendia, M., Ghassempouri, M., Ozturk, E. and Peysson, F. (eds.) (2019). *Twin-Control: A Digital Twin Approach to Improve Machine Tools Lifecycle*. Springer. <https://doi.org/10.1007/978-3-030-02203-7>
- Matta, A. and Lugaresi, G. (2024). An introduction to digital twins. In *Proceedings of the 2024 Winter Simulation Conference*, <https://doi.org/10.1109/WSC63780.2024.10838793>.
# What is a digital twin?

```{admonition} Learning objectives
:class: tip
After reading this page, you will be able to:
- Define a digital twin and its main components.
- Describe how the concept evolved from computer simulation.
- Distinguish a digital model, a digital shadow and a digital twin.
- Explain the three essential features of a digital twin.
```

## Definition

A **digital twin** is a digital representation of a physical object, system or place that uses data to represent its current state, performance and behaviour as accurately as possible ([IBM, 2025](https://www.ibm.com/think/topics/digital-twin)). What distinguishes it from an ordinary model is the **connection** with its real counterpart: the digital twin is regularly updated with data from the real world, and its results can be used to act on the real world.

Digital twins are used in almost every sector, including manufacturing, transportation, energy, healthcare, agriculture, construction and urban planning. Their value lies in supporting faster, cheaper and better-informed decisions based on facts rather than assumptions. They also allow low-risk experimentation: testing an idea on the digital twin before trying it in reality ([Apte and Spanos, 2021](https://sloanreview.mit.edu/article/the-digital-twin-opportunity/)).

In its simplest form, a digital twin has three parts:

- the **physical part**: the real object, such as a building or a roof;
- the **digital part**: its digital representation, such as a 3D model enriched with data;
- the **connection**: the flow of data between the two.

{numref}`fig-dt` is based on a model developed by Deloitte for manufacturing ([Parrott and Warshaw, 2017](https://www.deloitte.com/content/dam/insights/articles/2024/3833_industry4-0_digital-twin-technology/dup-industry-4.0-digital-twin-technology.pdf)), here applied to a city. It shows a city block split in two. On the left is the **physical** city: its buildings, roofs, streets and vegetation. On the right is its **virtual** counterpart: a digital copy of the same block. A digital twin is the combination of both halves and of the connection between them.

```{figure} ./images/DT.png
:alt: Digital Twins in the context of cities
:width: 100%
:align: center
:name: fig-dt

The digital twin cycle. Adapted from [Urban Design Lab (2025)](https://urbandesignlab.in/digital-twins-pioneering-sustainable-and-smart-urban-futures/), based on the digital twin model of [Parrott and Warshaw (2017)](https://www.deloitte.com/content/dam/insights/articles/2024/3833_industry4-0_digital-twin-technology/dup-industry-4.0-digital-twin-technology.pdf).
```

### The inner loop

Four elements connect the physical and virtual sides:

1. **Sensors** capture information about the physical world. In a city, these are not only devices such as weather stations or water level sensors, but also aerial LiDAR surveys, aerial photographs and public registers.
2. **Data** from these sources is transferred to the virtual side, where it is combined with other information, such as plans, regulations or local priorities. 
3. **Analytics** turn the data into information, using models, algorithms and visualisations.
4. **Actions** bring the results back to the physical world, where they change what happens on the ground. The changes are captured again by the sensors, and the loop starts over.

### The six stages

The outer ring breaks the same loop into six stages. The table shows what each stage means for rooftops.

| Stage | What happens | Rooftop example |
|---|---|---|
| **Create** | Ways to capture data about the physical world are put in place, and complemented with data from other systems | A city commissions an aerial LiDAR survey, or installs moisture sensors on a green roof, and gathers its building and heritage registers |
| **Interact** | Data is exchanged securely between the physical world and the digital side (called *communicate* in the original model) | The LiDAR point cloud and the register data are delivered to the team that maintains the twin |
| **Aggregate** | Data from different sources is prepared, combined and stored, locally or in the cloud | Building footprints, LiDAR, heritage status and flood maps are merged into a 3D city model |
| **Analyze** | Data is analysed and visualised, by analysts or with the help of decision-support tools | The slope, area and solar irradiation of each roof surface are calculated |
| **Insight** | Results highlight where attention is needed and what could be improved | A map shows which roofs could become green, blue or yellow roofs, and how scenarios compare |
| **Decision** | People decide what to do and put it into practice (called *act* in the original model) | The city selects a priority district and offers an incentive; owners install new rooftop functions |

The cycle never ends: every decision changes the physical city, and the next survey or sensor reading captures those changes. How fast the cycle turns depends on the purpose of the twin. A twin that steers the valves of a blue roof before a storm needs data within minutes. A twin used to plan rooftop activation across a city can be updated when new surveys or register data become available.

In the original model, the last stage depends entirely on human intervention: the twin provides insights, and people decide whether and how to act. MultiRoofs follows the same principle. The twin supports the public authority, which remains responsible for the decision.

### The five dimensions

The elements of {numref}`fig-dt` correspond to a widely used model that describes a digital twin through five dimensions ([Tao and Zhang, 2017](https://doi.org/10.1109/ACCESS.2017.2756069)):

| Dimension | In the figure | Rooftop example |
|---|---|---|
| **Physical entity** | The left half of the block | The roofs of a district |
| **Virtual entity** | The right half of the block | A 3D model of the buildings and their roof surfaces |
| **Data** | Sensors and data | Roof geometry, construction year, solar irradiation, flood risk |
| **Services** | Analytics and insight | Visualising rooftop potential, comparing scenarios |
| **Connection** | The dashed arrows linking both halves | Regular updates of the model with new LiDAR or register data |

The page [Building a digital twin](building-a-digital-twin.md) explains each dimension in more detail.

## Origins

Computers have been used to simulate complex products and systems since the 1960s. These **digital models** were mostly used offline, to compare design alternatives before something was built. They did not need to represent an existing object.

The idea closest to today's digital twins dates back to NASA's Apollo missions in the 1960s. Simulators adapted to the conditions of the real spacecraft were used to train astronauts and mission controllers, giving rise to the idea of a "living model". Several developments followed:

- **1980s.** With computer-integrated manufacturing, data started to flow automatically from physical systems into digital models, and **real-time simulation** became common in industry and entertainment.
- **1990s.** David Gelernter described "mirror worlds": software models of parts of reality, constantly updated with real-time information. Around the same time, **symbiotic or online simulation** introduced systems in which measurements feed a simulation, which then runs what-if experiments to steer the real system.
- **2000s.** Michael Grieves introduced the concept, later called the **digital twin**, in the context of product lifecycle management: a real space mirrored by a virtual space, with data flowing between them throughout the life of the product.

Definitions have since multiplied. They differ in detail, but share common elements: a virtual representation of a real counterpart, data that keeps the two aligned, and the use of that representation to understand, predict or improve the real one. Some definitions also stress that a digital twin must follow data governance rules and be interoperable with other systems ([van der Valk et al., 2021](https://doi.org/10.1007/s12599-021-00727-7)).

## Digital model, digital shadow or digital twin?

Not every digital representation is a digital twin. A common classification distinguishes three levels, based on how data flows between the physical object and its digital counterpart ([Kritzinger et al., 2018](https://doi.org/10.1016/j.ifacol.2018.08.474)):

| | Digital model | Digital shadow | Digital twin |
|---|---|---|---|
| **Data flow** | No automatic exchange; data is entered manually | Automatic flow from physical to digital | Automatic flow in both directions |
| **Represents** | An existing or planned object | The current state of an existing object | The current state of an existing object, and acts on it |
| **Typical use** | Design, offline analysis | Monitoring, visualisation, alerts, prediction | Optimisation and control |
| **Rooftop example** | A 3D model used to compare rooftop designs or estimate solar potential | A green roof whose soil moisture sensors update a dashboard | A blue-green roof whose valves release stored water automatically before forecast heavy rain |

In practice, the term "digital twin" is often used more broadly, especially for cities, where many urban digital twins are digital models or shadows that are updated periodically. Knowing these levels helps you understand what a given tool can and cannot do.

## Essential features

Three features characterise a digital twin:

1. **It is a data platform.** It collects, stores and processes data and information about its physical counterpart.
2. **It hosts models.** These models describe the current situation of the physical counterpart, or possible future situations.
3. **It is synchronised with reality.** The twin must reflect the state of the physical counterpart at any moment that matters for its purpose.

Synchronisation does not always mean real time. A twin of a power plant may need updates every second, while a twin of a city's building stock may only need updates when new aerial surveys or register data become available. Information from the physical to the digital side should flow automatically, but actions from the digital to the physical side can be delayed, and are often carried out by people.

```{admonition} Key takeaways
:class: important
- A digital twin connects a physical object with its digital representation through data.
- It grew out of computer simulation, from NASA's "living models" to Grieves' digital twin.
- A digital model has no automatic data flow, a digital shadow has a one-way flow, and a digital twin has a two-way flow.
- Synchronisation must match the purpose: a city-scale twin does not need second-by-second updates.
```

## Sources

- Apte, P. and Spanos, C. (2021). The digital twin opportunity. *MIT Sloan Management Review*, 63(1), 15–17.
- IBM (2025). *What is a digital twin?* <https://www.ibm.com/think/topics/digital-twin>
- Kritzinger, W., Karner, M., Traar, G., Henjes, J. and Sihn, W. (2018). Digital twin in manufacturing: a categorical literature review and classification. *IFAC-PapersOnLine*, 51(11), 1016–1022, <https://doi.org/10.1016/j.ifacol.2018.08.474>.
- Matta, A. and Lugaresi, G. (2024). An introduction to digital twins. In *Proceedings of the 2024 Winter Simulation Conference*.
- Parrott, A. and Warshaw, L. (2017). *Industry 4.0 and the digital twin: manufacturing meets its match*. Deloitte Insights. <https://www.deloitte.com/content/dam/insights/articles/2024/3833_industry4-0_digital-twin-technology/dup-industry-4.0-digital-twin-technology.pdf>
- Tao, F. and Zhang, M. (2017). Digital twin shop-floor: a new shop-floor paradigm towards smart manufacturing. *IEEE Access*, 5, 20418–20427, <https://doi.org/10.1109/ACCESS.2017.2756069>.
- Urban Design Lab (2025). *Digital twins: pioneering sustainable and smart urban futures*. <https://urbandesignlab.in/digital-twins-pioneering-sustainable-and-smart-urban-futures/>
- van der Valk, H., Haße, H., Möller, F. and Otto, B. (2021). Archetypes of digital twins. *Business & Information Systems Engineering*, 64, 375–391, <https://doi.org/10.1007/s12599-021-00727-7>.

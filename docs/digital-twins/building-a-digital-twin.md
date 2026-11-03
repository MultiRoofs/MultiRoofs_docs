# Building a digital twin

```{admonition} Learning objectives
:class: tip
After reading this page, you will be able to:
- Describe what each of the five dimensions requires when building a digital twin.
- Distinguish model-based and model-free digital twins.
- Identify the main challenges, risks and limitations of digital twins in cities.
```

## The five dimensions in practice

Building a digital twin means making each of its five dimensions concrete: the physical entity, the virtual representation, the services, the data and the connections ([Tao and Zhang, 2017](https://doi.org/10.1109/ACCESS.2017.2756069)). Once these are defined for a given purpose, they
are implemented as software components in an architecture adapted to the use case.

### Physical dimension

The physical dimension is the real-world object, system or place to be twinned, for example the building stock of a district. Knowledge about it is never perfect: data may be missing, outdated or inaccurate. The digital twin itself can help improve this knowledge over time, for instance when new surveys reveal roofs that were wrongly classified.

### Virtual dimension

The virtual dimension is the set of digital models that describe the physical entity. Several models can coexist, each dedicated to a specific question. The choice of model depends on the service it supports. There are two main approaches.

**Model-based twins** use models built on known principles, such as physical laws or engineering rules. A simple example is checking whether a roof can carry the weight of a green roof, based on its structure and materials. A more complex one is simulating how much solar radiation each roof surface receives during the year, or how much rainwater a blue roof retains during a storm. These models work well when the underlying behaviour is well understood.

**Model-free twins** use data-driven methods, such as machine learning, to detect patterns without an explicit model of the system. For example, a model trained on aerial images can detect existing green roofs or solar panels, or estimate a missing construction year. These methods are useful when a system is too complex to model explicitly, or when large amounts of data are available.

Many digital twins combine both approaches.

### Service dimension

Services make the functions of the twin available to people or other systems (see [Types and functions](types-and-functions.md)). Each service needs its own model. A typical example is a **scenario manager** that runs what-if analyses: for instance, comparing how different combinations of rooftop functions would contribute to a district's targets. The results are then translated into information that decision-makers can use.

### Data dimension

A digital twin must be able to acquire and update data as automatically as possible. Its data comes from dynamic sources, static baselines and expert knowledge (see [Data in a digital twin](data-in-a-digital-twin.md)). The data requirements of the twin determine how its databases are designed and where they are hosted: in the cloud, locally, or in a hybrid setup.

### Connection dimension

Connections keep the physical and digital sides aligned. They define which data is exchanged, how often and through which technologies and protocols. There is a trade-off: exchanging large amounts of data can slow the system down, while exchanging too little can make the twin drift away from reality. A twin of a city's building stock connects to data sources very differently from a twin of a single building with sensors.

## Challenges

Building a digital twin is demanding. Three challenges are particularly common:

- **Data integration.** Data comes from many sources, in different formats, often from older systems. A common data platform and shared standards simplify integration.
- **Cybersecurity.** Digital twins handle large amounts of data, which makes them targets for attacks. Encryption, access control and continuous monitoring are needed.
- **Costs.** Developing and maintaining a digital twin requires investment in hardware, software and expertise. Starting with small pilots that demonstrate their value, before scaling up, reduces this risk.

The MultiRoofs partner cities experienced these challenges directly. Their data inventories showed that 3D building models are available city-wide in some cities but only partially in others; that building identifiers often differ between datasets; that data comes in many formats and coordinate systems; that ownership and cadastral data is often private or sensitive; and that technical capacity varies between authorities.

## Risks in an urban context

Digital twins of cities bring specific risks ([Sabri et al., 2024](https://doi.org/10.1007/978-3-031-67778-6)):

- **Privacy and data protection.** Collecting large amounts of data about places and people creates a risk of misuse or data breaches.
- **Cybersecurity.** Manipulated data or disrupted systems can harm public safety and public trust.
- **Over-reliance.** If city operations depend too heavily on a digital twin, a system failure can disrupt them.
- **Digital divide.** People with limited access to technology may be further excluded from decisions informed by digital twins.
- **Costs.** High development and maintenance costs can put digital twins out of reach for cities with limited budgets.
- **Interoperability.** Different data sources, real-time processing, scalability and the lack of standard protocols complicate integration.

Common data models, open interfaces (APIs) and robust security practices help to manage these risks.

## Limitations

Even a well-built digital twin has limitations:

- **Data quality.** A digital twin is only as good as its data. Inaccurate or incomplete data leads to misleading results.
- **Scalability.** Scaling a twin to a whole city means integrating many systems and datasets, which is complex and resource-intensive.
- **Expertise.** Designing and maintaining a digital twin requires specialised skills that not every authority has in-house.
- **Keeping up to date.** Cities change constantly. Keeping the twin aligned with new buildings, renovations and land use changes is an ongoing effort.
- **Ethics and law.** Data collection, surveillance concerns and the fair distribution of benefits across neighbourhoods must be addressed.
- **Representativeness.** Data collected in small areas or from small samples may not reflect the wider population or city.
- **Legacy data.** Older datasets and systems often need cleaning, conversion or migration before they can be used.

These limitations are a reason for caution, not for avoiding digital twins. They are also why MultiRoofs treats its digital twin as support for decisions rather than a source of answers.

```{admonition} Key takeaways
:class: important
- Building a digital twin means defining its physical, virtual, service, data and connection dimensions for a specific purpose.
- Model-based twins rely on known principles; model-free twins learn from data.
- Data integration, cybersecurity and cost are the most common challenges; starting small reduces risk.
- Data quality, upkeep, expertise and ethics limit what a city digital twin can deliver.
```

## Sources

- Matta, A. and Lugaresi, G. (2024). An introduction to digital twins. In *Proceedings of the 2024 Winter Simulation Conference*, <https://doi.org/10.1109/WSC63780.2024.10838793>.
- Sabri, S., Alexandridis, K. and Lee, N. (eds.) (2024). *Digital Twin: Fundamentals and applications*. Springer Nature Switzerland, <https://doi.org/10.1007/978-3-031-67778-6>.
- Tao, F. and Zhang, M. (2017). Digital twin shop-floor: a new shop-floor paradigm towards smart manufacturing. *IEEE Access*, 5, 20418–20427, <https://doi.org/10.1109/ACCESS.2017.2756069>.
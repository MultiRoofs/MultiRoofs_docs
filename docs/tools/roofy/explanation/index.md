# Background

## What is [MultiRoofs tool](https://urbis.open3d.city/)?

MultiRoofs tool is an interactive web application for visualizing, exploring, and analyzing 3D city and building data, with a particular focus on buildings and their roof surfaces. MultiRoofs tool works with existing building and geospatial datasets that are loaded into the application.

After a dataset is loaded, the buildings are displayed in an interactive 3D viewer. Users can navigate around the model, select complete buildings or individual surfaces, inspect their available properties and attributes, and use different visualization and analysis functions.

MultiRoofs tool provides tools for classifying roof surfaces, inspecting building information, performing measurements and analyses, filtering data, and exporting results.

The general MultiRoofs tool workflow consists of loading an existing dataset, exploring it in the 3D viewer, inspecting its information, performing analysis or classification, and exporting the required results.

## Why Do We Need MultiRoofs tool?
MultiRoofs tool is useful for comparing and classifying roof surfaces. Roofs can be displayed using different colors according to characteristics such as surface type or user-defined rules. Rules can use properties such as roof area, inclination, or azimuth to identify roof surfaces that satisfy particular conditions.

3D city models can contain detailed geometric and attribute information that may be difficult to understand by examining the data file directly. MultiRoofs tool provides a graphical environment in which this information can be explored visually.

The tool therefore provides a more accessible way to explore 3D building information without requiring the user to manually inspect the underlying data structure.

## Required Input Files

To work with MultiRoofs tool, the user needs an existing building or geospatial dataset in a format supported by the application. The Add layer window provides support for the following file types:

| Format | File extension |
|---|---|
| CityJSON | `.city.json` |
| CityJSONSeq | `.city.jsonl` |
| FlatCityBuf | `.fcb` |
| CityGML | `.gml` |
| Parquet | `.parquet` |
| GeoJSON | `.geojson` |

CityParquet data can also be added by selecting its folder through the Add layer interface.


## Understanding Layers

Data added to MultiRoofs tool is organized into layers. A layer represents a dataset loaded into the application and does not necessarily represent a single building. One layer can contain multiple buildings or other geographic features.
Additional datasets can be added as separate layers using Add layer.

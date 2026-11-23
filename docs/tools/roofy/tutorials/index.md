# Roofy Documentaion
A step-by-step guide for viewing, analysing, classifying and exporting
3D building and rooftop data
# 1. Introduction to Roofy

[Roofy website](https://urbis.open3d.city/)  is an interactive web application for visualizing, exploring, and analyzing 3D city and building data, with a particular focus on buildings and their roof surfaces. It allows users to load supported 3D and geospatial datasets, display buildings on an interactive 3D map, select individual buildings or surfaces, and inspect their associated properties and attributes. 

Roofy mainly provides tools for classifying and coloring roof surfaces according to predefined or user-defined rules, such as roof slope, orientation, area, and solar suitability. 

## Roofy Main Page

After opening the Roofy web application, the main page is displayed, as shown in the {numref}`fig-roofy-20` . The interface is organized into several areas that provide access to the main functions of the tool.


```{figure} images/roofy_figure_20.png
:alt: Roofy interface
:width: 80%
:align: center
:name: fig-roofy-20

Roofy interface.
```

 **On the left side**, the Add layer button  is used to loaded the datasets  into the workspace. After you upload your file, it is used to visualize the buildings and roof surfaces from the loaded dataset.  



# 2. Upload your data 
To start working with your own data in Roofy, the dataset must first be added to the workspace. Click the **Add layer** button located in the Layers panel on the left side of the main interface. The Add layer window will then open.

```{figure} images/roofy_figure_22.png
:alt: Add layer window for uploading data to Roofy
:width: 80%
:align: center
:name: fig-roofy-22

Add layer window for uploading data to Roofy.
```

The Add layer window provides several methods for adding data: File, URL, Catalog, and Draw. 

To upload a file dataset stored on your computer, select File. You can either drag and drop the file into the upload area or click **Browse files** to locate it on your computer. 

```{note}
Roofy accepts CityJSON (.city.json), CityJSONSeq (.city.jsonl), FlatCityBuf (.fcb), CityGML (.gml), Parquet (.parquet), and GeoJSON (.geojson) files. If the data is stored as a CityParquet folder, click Choose folder instead
```

After selecting the file, Roofy loads the dataset into the workspace. The uploaded dataset then appears as a new layer in the Layers panel, and its available geographic or 3D content can be displayed in the main viewer.

Roofy displays the selected file in the lower part of the Add layer window, as shown in the {numref}`fig-roofy-23` below. The file name and the detected file type are displayed so that you can verify that the correct dataset has been selected. In this example, Roofy detects the uploaded `3dbag_b2.modified.city.json` file as CityJSON. Once you have confirmed that the file and detected format are correct, click the **Add layer** button to load the dataset into the Roofy workspace. Roofy will then process the file and display the available buildings and data in the main viewer.

```{figure} images/roofy_figure_23.png
:alt: Selected CityJSON file ready to be added as a new layer in Roofy
:width: 80%
:align: center
:name: fig-roofy-23

Selected CityJSON file ready to be added as a new layer in Roofy.
```


# 4. Understanding the Roofy workspace

In the example used throughout this guide, Roofy loads a CityJSON model
containing two buildings at LoD 2.2 Using the example CityJSON dataset
`3dbag_b2.modified.city.json` shown in the {numref}`fig-roofy-1`.

```{figure} images/roofy_figure_1.png
:alt: Roofy after loading a CityJSON model
:width: 80%
:align: center
:name: fig-roofy-1

Roofy after loading a CityJSON model: the layer is listed on the left and the two LoD 2.2 buildings are displayed on the 3D map.
```

After a model is loaded, the workspace is divided into a layer panel on
the left and a 3D map in the centre. Depending on the action being
performed, additional information can appear as a legend, a table below
the map, or a property panel on the right.

### Main Areas of the Roofy Interface

After a dataset is loaded, the Roofy interface is divided into several main areas. **The left side** is mainly used to manage and configure the loaded layers. It provides access to functions such as Zoom to layer, Open table, Export, Style, Filter, and Details.  The Details section provides information about the loaded dataset, such as its source, format, and coordinate reference system (CRS).

The **center** of the interface contains the interactive 3D map, where the loaded buildings are displayed in their geographic location. The user can navigate around the model, zoom in or out, and select buildings or individual surfaces. A legend is also displayed on the map to explain the colors currently used for the model.

At the **top of the interface**, the Mode control allows the user to choose how elements are selected. 

```{figure} images/roofy_figure_3.png
:alt: Roofy workspace showing the Style panel, rule-based roof colours, legend, table, and selected-object information
:width: 80%
:align: center
:name: fig-roofy-3

Roofy workspace with the Style panel, rule-based roof colours, legend, table, and selected-object information visible at the same time.
```

 {numref}`table-roofy-workspace` below describes the workspace for the Roofy website.

```{table} Main areas of the Roofy workspace
:name: table-roofy-workspace

| Area | Position | Purpose |
|---|---|---|
| Layers panel | Left | Displays the datasets that have been added to Roofy. After selecting a layer, the user can access functions such as Zoom to layer, Open table, Export, Style, Filter, and Details. |
| Add layer | Upper left | Opens the Add layer window. The window provides the File, URL, Catalog, and Draw options for adding data. |
| Style | Left, inside the selected layer | Controls how the loaded model is visually represented. The Color by option provides Surface type, Rules, and Single colour options. |
| Details | Left, inside the selected layer | Displays additional information about the selected layer. |
| Mode | Upper center | Controls how elements are selected in the 3D model. Pick feature is used to select a complete feature, such as a building, while Pick surface is used to select an individual surface, such as a roof surface. |
| Tools | Upper center; panel opens on the right | Opens the Tools panel. The available tools include Roof metrics to attributes, Measure solids, Validate solids, Height from extent, Join attributes by location, Aggregate buildings per area, and Distance to nearest. |
| Search | Upper center | Provides the search function in the map interface. |
| 3D viewer | Center | Displays the loaded 3D buildings. The user can navigate around the model, zoom, rotate the view, and interact with the displayed buildings and surfaces. |
| Legend | Lower-left area of the 3D viewer | Shows the colors used in the current visualization. When Rules are used, the legend shows the rule categories and the number of surfaces assigned to them. |
| Open table | Bottom center |  Opens the attribute table for the selected layer. Each row represents a building record, while the columns display its available attributes, such as ID, status, roof area, mean slope, and number of parts. |
| Navigation controls | Right side of the 3D viewer | Provide controls for navigating the 3D scene, including zooming and changing the view. |
| Property/selection panel | Right | Displays information about a selected building or surface. For a selected roof surface, the panel can display information such as area, slope, azimuth, surface type, rule match, and attributes. |
| Sun & shade | Upper right | Opens the Sun & shade controls for the 3D scene. |
| Scene settings | Upper right | Opens the Scene settings panel. |
| Export scene | Upper right | Captures the current view of the 3D scene with map attribution. The current view can be saved as a PNG image or opened in the print view for printing or saving as a PDF. |
| Export data | Left, inside the selected layer | Opens the data export window for the selected layer. It provides options for choosing which records and attributes to export, the output format, and the available Level of Detail (LoD). |
```

## Features and Surfaces

An important concept when using Roofy is the distinction between a feature and a surface.  `Pick feature` is used to select a complete feature such as a building, while `Pick surface` is used to select an individual surface of the 3D model. Other controls, such as Tools, Search, Sun & shade, and Scene settings, provide additional analysis, navigation, and visualization functions.

A feature represents a complete object in the dataset, such as a building. 
A surface represents an individual part of the 3D geometry. You can choose to select either the Pick Feature or the Pick Surface mode.

```{figure} images/roofy_feature_pick.png
:alt: Select the pick feature or the pick surface
:width: 80%
:align: center
:name: roofy_feature_pick

Select the pick feature or the pick surface
```
## Roof Properties and Attributes

Depending on the loaded dataset and the selected element, Roofy can display geometric properties and other attributes associated with buildings and roof surfaces.

For a roof surface, the displayed information can include properties such as:

- Area
- Slope
- Azimuth
- Surface type
- Rule match
- Associated attributes

## Roof Classification and Visualization

Roofy provides different methods for controlling how the model is visually represented through the Style section.
The Color by option can display the model using Surface type, Rules, or Single colour. 

```{figure} images/color_by.png
:alt: Select the pick feature or the pick surface
:width: 80%
:align: center
:name: roofy_coloryby

Roofy Color Options for Visualizing and Classifying Roof Surfaces
```

**Surface type** uses colors to distinguish semantic surfaces such as roofs, walls, and ground surfaces.
**Single colour** provides a uniform visualization. **Rules** provide a more analytical form of visualization by assigning colors to roof surfaces according to defined conditions.
 Rules can be created using properties such as area, inclination, and azimuth. This makes it possible to visually identify roof surfaces with particular characteristics.

## Analysis Tools

Roofy also contains a Tools panel that provides additional functions for working with the loaded data. The tools visible in the interface include Roof metrics to attributes, Measure solids, Validate solids, Height from extent, Join attributes by location, Aggregate buildings per area, and Distance to nearest.

```{figure} images/roofy_tool.png
:alt: Select the pick feature or the pick surface
:width: 80%
:align: center
:name: roofy_roofy_tool_pick

 The Tools panel
```
## Output and Export

Roofy provides different types of output depending on what the user wants to obtain.
The layer-level data **export function** is used to export building/model data. The export interface provides options for selecting the records and attributes to include, choosing an output format, and selecting an available Level of Detail (LoD).

```{figure} images/export1.png
:alt: Select the pick feature or the pick surface
:width: 80%
:align: center
:name: roofy_export1

 Data Export Interface
```

The **Export scene** function in the upper-right part of the interface serves a different purpose. It captures the current visual view of the scene. The scene can be saved as a PNG image or opened in the print view for printing or saving as a PDF.


```{figure} images/export2.png
:alt: Select the pick feature or the pick surface
:width: 80%
:align: center
:name: roofy_export1

Export scene function
```
It is therefore important to distinguish between exporting data and exporting the visual scene: one produces data for further use, while the other captures the current visualization.


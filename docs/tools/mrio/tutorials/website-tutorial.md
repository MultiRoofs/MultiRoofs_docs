# Web-based MRIO

This tutorial provides a guide to help users understand how to interact with the [web-based MRIO](https://multiroofs.github.io/mrio/) and use its main functionalities. It explains how to upload CityJSON or CityJSONSeq files, inspect building information, prepare datasets for the MultiRoofs workflow, validate files, manage building attributes, calculate roof areas and building volumes, and download the processed results. {numref}`fig-web-mrio-welcome` below illustrates the web-based MRIO welcome page.


```{figure} ./images/figure_01.png
:alt: Web-based MRIO welcome page
:width: 400px
:align: center
:name: fig-web-mrio-welcome

The web-based MRIO welcome page.
```

## What you need

- A stable Internet conexion to access the web-based MRIO
- A CityJSON (`.city.json`) or CityJSONSeq (`.city.jsonl`) file. If you don't have one, you can use the example file `3dbag_b2.city.json`, included in the `data`
  folder of the MRIO project.

% TODO: complete the requirements and, if possible, provide a downloadable sample
% file and CSV file, as in the MultiRoofs Builder tutorials.

## Uploading your data

1. Open the [MRIO website](https://multiroofs.github.io/mrio/).

2. Click **Browse files** and select a *.city.json* or *.city.jsonl* file, or drag it onto the upload area. 


```{figure} ./images/figure_02.png
:width: 600px
:align: center
:alt: Upload a CityJSON or CityJSONSeq file
:name: fig-web-mrio-upload

Upload the CityJSON or CityJSONSeq file.
```

3. Wait for the **File Overview** to appear. Check that the format, number of objects, vertices, and CRS are shown.

```{note}
If the data in the **File Overview** and **Attributes** sections of your website differ from what is shown in the screenshot, it is because you uploaded a different type of file containing different data.
```

```{figure} ./images/figure_03.png
:width: 700px
:align: center
:alt: File Overview after uploading
:name: fig-web-mrio-overview

File Overview after uploading.
```

## Understanding the main workspace

After uploading a CityJSON or CityJSONSeq file, the web-based MRIO displays the main interface as shown in {numref}`fig-web-mrio-main` below, which is divided into two sections: the **Operations** panel on the left-hand side and the **File Overview** panel and the **Attributes** section in the right-hand side of the screen.

```{figure} ./images/figure_04.png
:width: 700px
:align: center
:alt: Web-based MRIO main workspace
:name: fig-web-mrio-main

The main workspace, showing the **Operations** panel on the left-hand side and the **File Overview** panel and the **Attributes** section in the right-hand side of the screen.
```


The **Operations** panel provides the functionalities for processing and modifying the uploaded file. Users can calculate roof surface areas and building volumes, delete or rename existing attributes, convert Roofer output into the MultiRoofs format, import additional attributes from CSV files, update the Coordinate Reference System (CRS),  and validate the dataset. The panel also includes a **Download** button to save the processed file and a **Load different file** button to upload another dataset. The workflow is to first prepare the file for MultiRoofs and run validation. 

```{note}
Once the data has been uploaded, we recommend to first prepare the file for MultiRoofs by clicking on the button **Prepare file for MultiRoofs** (see {ref}`mrio-prepare-file`) and then validating the output with **Validate file** button (see {ref}`mrio-validate-file`).
```

The **File Overview** panel provides a summary of the uploaded dataset. At the top, four information boxes show the file format, total number of City Objects, number of vertices, and Coordinate Reference System (CRS). In the example shown in {numref}`fig-web-mrio-main`, the uploaded file is in CityJSON version 2.0 format (**FORMAT** field) and contains 4 CityObjects (**OBJECTS** field, not necessarily the number of buildings), 127 vertices (**VERTICES** field as the number of coordinate points used to describe objects' geometry), and a CRS identified by EPSG code 7415 (**CRS** field). 

Below these boxes, the **Object Types** section displays the different types of objects contained in the dataset and their quantities. In this example, the file contains 2 Building objects and 2 BuildingPart objects. Buildings represent the main building entities, while BuildingParts represent individual parts of buildings that may contain their 3D geometry. A BuildingPart can hold the 3D roof/wall geometry while its parent Building holds descriptive information. Each of these objects has a set of attributes representing pieces of information attached to them, for example construction year, roof type, or volume.

The **Attributes** section lists the available attributes associated with the CityObjects. Each row displays the attribute name, an example value (from the uploaded data), and the number and percentage of CityObjects containing that attribute. For example, the attribute **b3_dak_type** has the displayed value *slanted*, while *2 (50%)* indicates that 2 out of the 4 CityObjects contain this attribute, representing 50% of the CityObjects in the dataset. 

```{note}
The displayed value of each attribute is just an example and does not necessarily represent the value for every object.
```

Overall, this interface allows users to understand the structure and contents of their uploaded dataset before applying any modifications. Users can review the available building information, select the required processing operation, validate the results, and download the updated file for further use.

(mrio-prepare-file)=
## Preparing the 3D model for MultiRoofs

The **Prepare file for MultiRoofs** operation converts the structure of the uploaded 3D building model into a format suitable for the MultiRoofs workflow. 

%TODO: add extra information obtained from Hugo regarding issue 6 in Github

Once the data has been prepared using this functionality, read the success message and compare the Object Types and total object count. Here, the MultiRoof extension will be added to the website, confirming that the file has been converted to MultiRoof successfully.

```{figure} ./images/figure_05.png
:width: 600px
:align: center
:alt: Data after preparation for MultiRoofs
:name: fig-web-mrio-prepare-file

After preparation, BuildingParts are merged into their Buildings, and Building objects remain.
```

```{admonition} Warning
:class: important
We recommend to validate the file both before and after preparation to ensure that the processing has been completed correctly.
```

(mrio-validate-file)=
## 3D model validation

**Validate file** checks whether the 3D model follows important CityJSON structural rules. Use it before editing and again after any major operation. Green check marks indicate passed checks; red symbols identify findings that need review.

```{figure} ./images/figure_06.png
:width: 500px
:align: center
:alt: MRIO validation dialog
:name: fig-web-mrio-validation

Validation dialog
```
(attributes-from-CSV)=
## Importing attributes from a CSV file

You can use this operation if you have an attribute that you want to add to your 3D model. A CSV file is a table in which each row represents a single CityObject. The first column must contain the exact ID of that CityObject. The remaining columns become new attributes. The ID column is used for matching, not copied as a new attribute. If you have a CSV file containing attributes that you want to add to your file, you need to follow these steps:

1. Click on **Import attributes from CSV**.

2. Choose a CSV file with matching CityObject IDs in the first column.

3. Click **Add attributes** and check the results in the **Attributes** section.

4. Validate the file after importing (see {ref}`mrio-validate-file`).

```{figure} ./images/figure_6csv.png
:width: 600px
:align: center
:alt: Import attributes from a CSV file
:name: fig-web-mrio-import-csv

Importing new attributes from a CSV file
```

## Managing attributes

### Renaming an attribute

Click **Rename attribute** to rename an attribute in your 3D model. First, you need to select the attribute you want to rename and then enter a new name. Click on **Rename** to save the new name.  try to use meaningful name.

```{figure} ./images/figure_07.png
:width: 600px
:align: center
:alt: Rename Attribute dialog
:name: fig-web-mrio-rename

**Rename Attribute** dialog: select an existing attribute and type its new name.
```

```{note}
Pick a name your future self will thank you for."attr1" helps no one.
```

### Deleting an attribute

Click **Delete attribute** to remove an existing attribute in your 3D model. First, choose the attribute to be removed, and then confirm its deletion by clicking on **Delete**. 

```{figure} ./images/figure_08.png
:width: 600px
:align: center
:alt: Delete Attribute dialog
:name: fig-web-mrio-delete

**Delete Attribute** dialog.
```

```{admonition} Warning
:class: important
Once it's gone, it's gone. Double-check before you confirm.
```

## Adding attributes roof area and building volume

The functionality **Add roof area** calculates roof surface information and stores it as an attribute (**+roof-total-area** in {numref}`fig-web-mrio-add-attribute`). Similarly, the **Add volume** functionality add a new attribute representing the volume of each object. 

```{figure} ./images/figure_09.png
:width: 600px
:align: center
:alt: Result of adding the roof area attribute
:name: fig-web-mrio-add-attribute

Attribute **+roof-total-area** added with the roof area.
```

## Setting the Coordinate Reference System (CRS)

The Coordinate Reference System (CRS) describes how coordinates relate to locations on Earth. Click **Set CRS**, enter the intended EPSG code, and confirm. For example, EPSG:28992 is used for the Dutch national coordinate system. This feature changes the CRS identifier in the metadata; it does not reproject the coordinate values. Only set a code that correctly describes the coordinates already in your file.


```{figure} ./images/figure_10.png
:width: 500px
:align: center
:alt: Set EPSG Code dialog
:name: fig-web-mrio-epsg

Set EPSG Code dialog
```

## Downloading the 3D model

The following steps describes how to download the resulting 3D model after performing some of the functionalities described above.

1. Click **Download** in the **Operations** panel.

2. Select CityJSON or CityJSONSeq, depending on the type of your original file.

3. Check the filename and extension: .city.json for CityJSON, .city.jsonl for CityJSONSeq.

4. Click **Download**, then reopen the saved file in MRIO or another compatible viewer to verify that was correctly downloaded.

{numref}`fig-web-mrio-download` shows an example where the file is in CityJSON format (.city.json). Therefore, the **CityJSON** option should be selected when the model is downloaded. Alternatively, if your 3D model is in CityJSONSeq format (.city.jsonl), the option **CityJSONSeq** should be selected.

```{figure} ./images/figure_11_cityjson.png
:width: 500px
:align: center
:alt: Download file based on selected format
:name: fig-web-mrio-download

Download the file based on the selected output format.
```

```{admonition} Warning
:class: important

When downloading the processed 3D model, make sure to select the correct output format in the **Download File** window. If your file is in CityJSON format (.city.json), select CityJSON. If your file is in CityJSONSeq format (.city.jsonl), select CityJSONSeq. The selected format should match the file type you intend to use. You can also modify the filename before downloading. 
```


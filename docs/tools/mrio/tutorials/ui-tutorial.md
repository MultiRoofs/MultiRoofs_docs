(mrio-cli-tutorial)=
# CLI-based MRIO

This tutorial explains how to use the CLI-based MRIO, a version of MRIO that runs in a terminal. It covers how to open CityJSON or CityJSONSeq files, inspect building information, prepare datasets for the MultiRoofs workflow, validate files, manage attributes, calculate roof areas and building volumes, and save the results. You interact with all functionalities using your keyboard.

## What you need

- MRIO installed on your computer. If you have not installed it yet, follow {ref}`mrio-cli-install`.
- A CityJSON (`.city.json`) or CityJSONSeq (`.city.jsonl`) file. If you don't have one, you can use the example file `3dbag_b2.city.json`, included in the `data`
  folder of the MRIO project.

% TODO: complete the requirements and, if possible, provide a downloadable sample
% file and CSV file, as in the CityJSON Generator tutorials.

(mrio-cli-start)=
## Starting MRIO

### Place your file in the data folder

Place the file you want to process in the `data` folder of the MRIO project ({numref}`fig-cli-mrio-data-folder`). This folder is a convenient location for your
input files, and keeps the commands short.

```{figure} ./images/data_folder.png
:width: 700px
:align: center
:alt: Data folder inside the MRIO project folder
:name: fig-cli-mrio-data-folder

The `data` folder inside the MRIO project folder.
```

For example:

```text
mrio
└── data
    ├── 3dbag_b2.city.json
    └── my_buildings.city.json
```

### Run MRIO

Open a terminal in the MRIO project folder (see {ref}`mrio-cli-install`) and run MRIO with the file you want to open. This tutorial uses the example file:

```bash
cargo run -p mrio-cli -- data/3dbag_b2.city.json
```

Press **Enter**. If the command succeeds, the MRIO terminal user interface appears directly in the terminal ({numref}`fig-cli-mrio-run`).

```{figure} ./images/build.png
:width: 700px
:align: center
:alt: Running MRIO with the example CityJSON file
:name: fig-cli-mrio-run

Running MRIO with the example CityJSON file.
```

To open your own file, replace the path after `--` with the path of your file. For example, for a CityJSON file:

```bash
cargo run -p mrio-cli -- data/my_buildings.city.json
```

And for a CityJSONSeq file:

```bash
cargo run -p mrio-cli -- data/my_buildings.city.jsonl
```

### Choose the output format at start-up

MRIO can open CityJSON and CityJSONSeq files, and save them in either format. You can specify the output format when starting MRIO. For example, this command opens a CityJSONSeq file and saves it as CityJSON:

```bash
cargo run -p mrio-cli -- data/3dbag_b2.city.jsonl --output-format cityjson
```

You can also change the output format when saving (see {ref}`mrio-cli-save`).

## Understanding the terminal user interface

Once MRIO starts, the terminal changes into an interactive interface with two panels: the **Operations** panel on the left and the **File Overview** panel on the right ({numref}`fig-cli-mrio-tui`).

```{figure} ./images/mrio_ui.png
:width: 700px
:align: center
:alt: MRIO terminal user interface
:name: fig-cli-mrio-tui

The MRIO terminal user interface, with the **Operations** panel on the left and the **File Overview** panel on the right.
```

The **Operations** panel provides the functionalities for processing and modifying the file. You can calculate roof surface areas and building volumes, delete or rename attributes, convert Roofer output into the MultiRoofs format, import attributes from CSV files, set the Coordinate Reference System (CRS), and validate the dataset. The panel also includes **Save**, to save the processed file, and **Load different file**, to open another dataset.

The **File Overview** panel summarises the loaded dataset: the CityJSON version, the Coordinate Reference System (CRS), the extensions, the number of objects and vertices, the object types and the available attributes.

The **Object Types** section shows the types of objects in the dataset and how many there are of each. In this example, the file contains 2 Building objects and 2 BuildingPart objects. Buildings represent the main building entities, while BuildingParts represent parts of buildings. A BuildingPart can hold the 3D roof and wall geometry, while its parent Building holds descriptive information. Each object has attributes: pieces of information attached to it, such as construction year, roof type or volume.

```{note}
Once the data has been loaded, we recommend to first prepare the file for MultiRoofs (see {ref}`mrio-cli-prepare-file`) and then to validate the result (see {ref}`mrio-cli-validate-file`).
```

### Keyboard controls

MRIO is controlled with the keyboard:

| Key | Function |
|---|---|
| `↑` / `↓` | Move through operations or lists |
| `Enter` | Select or confirm the highlighted item |
| `Esc` | Cancel the current dialog |
| `Tab` | Switch to the File Overview panel, or toggle the output format in the Save dialog |
| `PgUp` / `PgDn` | Move faster through a long overview |
| `s` | Open the Save dialog |
| `q` | Quit; MRIO warns you if there are unsaved changes |

```{admonition} Warning
:class: important
Changes are kept in the current MRIO session until you save them. An asterisk (`*`) next to the filename in the blue title bar indicates that the loaded dataset has unsaved changes.
```

(mrio-cli-prepare-file)=
## Preparing the 3D model for MultiRoofs

The **Prepare file for MultiRoofs** operation converts the structure of the 3D building model into the format required by the MultiRoofs workflow.

Select **Prepare file for MultiRoofs** with `↑`/`↓`, then press `Enter`. MRIO shows a success message describing the changes ({numref}`fig-cli-mrio-prepare`).

```{figure} ./images/mrfigure_03.png
:width: 700px
:align: center
:alt: Preparing a file for MultiRoofs
:name: fig-cli-mrio-prepare

Success message after preparing the file for MultiRoofs.
```

In this example, MRIO:

- merged 2 BuildingPart objects into their Buildings;
- removed the LoD 0 geometry;
- renamed 0 attributes;
- added the `+roof-total-area` attribute; and
- added the MultiRoofs extension.

This operation therefore modifies the structure and metadata of the dataset, not only its format. Press `Enter` to close the message and return to the main interface. The **File Overview** now shows the updated object types and the MultiRoofs extension ({numref}`fig-cli-mrio-prepared-overview`).

```{figure} ./images/mrfigure_04.png
:width: 700px
:align: center
:alt: File Overview after preparation
:name: fig-cli-mrio-prepared-overview

File Overview after preparation: BuildingParts are merged into their Buildings.
```

```{admonition} Warning
:class: important
We recommend to validate the file both before and after preparation to ensure that the processing has been completed correctly.
```

(mrio-cli-validate-file)=
## 3D model validation

**Validate file** checks whether the 3D model follows the CityJSON structural format. Use it before editing, and again after any major operation.

Select **Validate file** and press `Enter`. MRIO shows the results of its checks ({numref}`fig-cli-mrio-validation`). Green check marks indicate passed checks; red symbols indicate findings that need review.

```{figure} ./images/mrfigure_09.png
:width: 700px
:align: center
:alt: CityJSON validation results
:name: fig-cli-mrio-validation

CityJSON validation results.
```

The checks include JSON syntax, schema, extensions, parent and child consistency, vertex indices, semantics arrays, textures, materials, extra root properties, duplicate vertices and unused vertices. Investigate any check reported as an error or warning before using the dataset further.

## Importing attributes from a CSV file

You can use this operation to add attributes to your 3D model from a CSV file. A CSV file is a table in which each row represents a single CityObject. The first column must contain the exact ID of that CityObject. The remaining columns become new attributes. The ID column is used for matching, and is not copied as an attribute.

1. Select **Import attributes from CSV** and press `Enter`.
2. Type the path to the CSV file ({numref}`fig-cli-mrio-csv-path`), for example:

   ```text
   data/attributes.csv
   ```

3. Press `Enter`. MRIO reports how many objects received the new attributes ({numref}`fig-cli-mrio-csv-success`).
4. Validate the file after importing (see {ref}`mrio-cli-validate-file`).

```{figure} ./images/mrfigure_05.png
:width: 700px
:align: center
:alt: CSV file path dialog
:name: fig-cli-mrio-csv-path

Entering the path to the CSV file.
```

```{figure} ./images/mrfigure_08.png
:width: 700px
:align: center
:alt: Successful CSV import
:name: fig-cli-mrio-csv-success

Attributes successfully imported into 2 objects.
```

```{admonition} Warning
:class: important
The IDs in the first column of the CSV must match CityObject IDs that exist in the loaded dataset. Otherwise, MRIO cannot tell which objects should receive the new attributes, and reports `Added attributes to 0 object(s) from CSV` ({numref}`fig-cli-mrio-csv-error`). In that case, correct the IDs in the CSV file and import it again.
```

```{figure} ./images/mrfigure_07.png
:width: 700px
:align: center
:alt: CSV import with no matching objects
:name: fig-cli-mrio-csv-error

The CSV file refers to CityObjects `5`, `10`, `11` and `12`, which do not exist in  the loaded dataset, so no attributes were imported.
```

## Managing attributes

### Viewing all attributes

The File Overview may contain more attributes than fit on the screen. Press `Tab` to move to the File Overview panel. The help bar at the bottom then shows the navigation controls:

- `↑` / `↓` to scroll line by line;
- `PgUp` / `PgDn` to move faster through a long list; and
- `Tab` again to return to the Operations panel.

This is the easiest way to check new, imported, renamed or calculated attributes before saving.

### Renaming an attribute

1. Select **Rename attribute** and press `Enter`. MRIO shows the attributes that can be renamed.
2. Use `↑`/`↓` to highlight the attribute and press `Enter` ({numref}`fig-cli-mrio-rename-select`).
3. Type the new name ({numref}`fig-cli-mrio-rename-dialog` and {numref}`fig-cli-mrio-rename-name`) and press `Enter`.

```{figure} ./images/mrfigure_11.png
:width: 700px
:align: center
:alt: Selecting the attribute to rename
:name: fig-cli-mrio-rename-select

Selecting `+roof-total-area` from the list of attributes.
```

```{figure} ./images/mrfigure_12.png
:width: 700px
:align: center
:alt: New attribute name dialog
:name: fig-cli-mrio-rename-dialog

Dialog to enter the new attribute name.
```

```{figure} ./images/mrfigure_13.png
:width: 700px
:align: center
:alt: Entering the new attribute name
:name: fig-cli-mrio-rename-name

Entering `top_area` as the new name.
```

MRIO confirms the change and reports how many objects contained the attribute ({numref}`fig-cli-mrio-rename-success`). In this example, `+roof-total-area` was renamed to `top_area` in 2 objects.

```{figure} ./images/mrfigure_14.png
:width: 700px
:align: center
:alt: Attribute renamed successfully
:name: fig-cli-mrio-rename-success

Attribute renamed successfully.
```

```{note}
Pick a name your future self will thank you for. "attr1" helps no one.
```

### Deleting an attribute

1. Select **Delete attribute** and press `Enter` ({numref}`fig-cli-mrio-delete-before`). MRIO shows the attributes that can be removed.
2. Use `↑`/`↓` to highlight the attribute and press `Enter` ({numref}`fig-cli-mrio-delete-select`).

```{figure} ./images/mrfigure_18.png
:width: 700px
:align: center
:alt: File Overview before deleting an attribute
:name: fig-cli-mrio-delete-before

File Overview before deleting an attribute.
```

```{figure} ./images/mrfigure_19.png
:width: 700px
:align: center
:alt: Selecting the attribute to delete
:name: fig-cli-mrio-delete-select

Selecting `b3_h_dak_50p` for deletion.
```

In this example, MRIO reports that `b3_h_dak_50p` was removed from 2 objects.

```{admonition} Warning
:class: important
Once it's gone, it's gone. Double-check before you confirm.
```

## Adding roof area and building volume

### Roof area

Select **Add roof area** and press `Enter`. MRIO calculates the roof area of each applicable object and stores it in the `+roof-total-area` attribute ({numref}`fig-cli-mrio-roof-area`).

```{figure} ./images/mrfigure_15.png
:width: 700px
:align: center
:alt: Roof area calculation
:name: fig-cli-mrio-roof-area

Roof area added to 2 objects.
```

```{note}
**Prepare file for MultiRoofs** already adds `+roof-total-area`. In this tutorial, the attribute is added again because it was renamed in the previous step.
```

After closing the message, the new attribute appears in the File Overview with an example value, such as `186.711`, and the number and percentage of objects that contain it.

### Building volume

Select **Add volume** and press `Enter` ({numref}`fig-cli-mrio-volume`). MRIO calculates the volume of each applicable object and stores it in the `+building-volume` attribute ({numref}`fig-cli-mrio-volume-success`).

```{figure} ./images/mrfigure_16.png
:width: 700px
:align: center
:alt: Add volume operation
:name: fig-cli-mrio-volume

Selecting **Add volume**.
```

```{figure} ./images/mrfigure_17.png
:width: 700px
:align: center
:alt: Volume calculated successfully
:name: fig-cli-mrio-volume-success

Building volume added to 2 objects.
```

## Setting the Coordinate Reference System (CRS)

The Coordinate Reference System (CRS) describes how coordinates relate to locations on Earth. **Set CRS** changes the CRS identifier in the file's metadata; it does not reproject the coordinate values. Only set a code that correctly describes the coordinates already in your file. For example, EPSG:28992 is the Dutch national coordinate system.

% TODO: add the steps and a screenshot of the Set CRS dialog in the CLI version.

(mrio-cli-save)=
## Saving the 3D model

1. Select **Save** in the Operations panel, or press `s` ({numref}`fig-cli-mrio-save`).
2. Check the **Path**, the name and location of the output file, for example `data/3dbag_b2.modified.city.json`. Edit it if needed.
3. Press `Tab` to toggle the **Output format** between CityJSON and CityJSONSeq.
4. Press `Enter` to save. A green success message confirms that the file was saved. Press `Enter` again to close it.

```{figure} ./images/mrfigure_20.png
:width: 700px
:align: center
:alt: Save As dialog
:name: fig-cli-mrio-save

The Save dialog. Edit the output path, and press `Tab` to toggle the output format.
```

```{admonition} Warning
:class: important
Make sure the output format matches the file extension: `.city.json` for CityJSON, `.city.jsonl` for CityJSONSeq.
```
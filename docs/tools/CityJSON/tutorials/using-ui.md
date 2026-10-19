# Generate CityJSON using an user interface

This tutorial shows how to reconstruct LoD2.2 building models from a classified LiDAR point
cloud and 2D building footprints using the MultiRoofs LoD 2.2 CityJSON Generator, a graphical
user interface for Roofer. It uses the same small demo dataset as
[Generate CityJSON on a terminal](./using-cli.md), so you can check that
everything works before using your own data.

The workflow has six steps:

1. Install Roofer and the LoD 2.2 CityJSON Generator.
2. Download the demo data.
3. Tell the application where Roofer is installed (only needed once).
4. Prepare the MultiRoofs configuration file.
5. Run the reconstruction. This produces a CityJSONSeq file (`.city.jsonl`).
6. Check the result in a web viewer.

```{note}
This tools has been tested on Windows 11 and Ubuntu 14.04
```

## What you need

- A classified point cloud in LAS or LAZ format, with at least the classes Ground (2) and Building (6).
- Building footprints in GeoPackage format (`.gpkg`), with one unique identifier per building.
- Roofer v1.0.0 or later.
- The MultiRoofs LoD 2.2 CityJSON Generator. <!-- TODO: add download link -->
- A web browser, to view the result.

## Step 1: Install Roofer and the application

See [Installing dependencies](./install-dependencies.md) for more details.

## Step 2: Download the demo dataset

Download the [Wippolder dataset](./wippolder.zip) and unzip it. It covers a neighbourhood next
to TU Delft with 60 buildings, and contains:

- `wippolder.las`: the classified point cloud
- `wippolder.gpkg`: the building footprints

## The interface

The main window of the LoD 2.2 CityJSON Generator contains the following parts:

| # | Part | Purpose |
|---|---|---|
| 1 | LiDAR point cloud(s) | Select one or more `.las` or `.laz` files, or a folder that contains only `.las` or `.laz` files. Use the drop-down menu to choose between files and a folder. |
| 2 | Building footprints | Select the `.gpkg` file with the 2D building footprints. |
| 3 | Output folder | Select the folder where the results are stored. |
| 4 | Generate LoD 2.2 CityJSON | Starts the reconstruction. |
| 5 | View with CityJSON Ninja | Opens the ninja viewer and the folder containing the result. |
| 6 | Processing messages | Shows the messages printed by Roofer while it runs. Use **Copy log** or **Save log...** to keep them. |
| 7 | Configuration file | Optional. Selects a Roofer `.toml` configuration file. **Clear** removes the selection. |
| 8 | File > Settings | Selects the Roofer executable. |
| 9 | Help > About | Shows information about the tool and the MultiRoofs project. |

```{figure} ../images/ui_overview.png
:alt: Main window of the LoD 2.2 CityJSON Generator with its parts numbered
:width: 90%
:align: center
:name: fig-ui-overview

The main parts of the LoD 2.2 CityJSON Generator.
```

## Step 3: Select the Roofer executable

Before the first reconstruction, the application needs to know where Roofer is installed.

1. Open **File > Settings** and verify that the path to Roofer is correct.

```{figure} ../images/ui_settings.png
:alt: Settings window for selecting the Roofer executable
:width: 90%
:align: center
:name: fig-ui-settings

The Settings window.
```

2. If the field is empty or the path is incorrect, click **Browse** and select `roofer.exe` in the `bin/` folder from Step 1.

```{figure} ../images/ui_select_roofer.png
:alt: File dialog selecting roofer.exe
:width: 90%
:align: center
:name: fig-ui-select-roofer

Selecting `roofer.exe`.
```

```{note}
If `roofer.exe` is not listed in the file dialog, set the file filter to
**Executable Files (\*.exe)** or **All Files**.
```

```{figure} ../images/ui_file_filter.png
:alt: File filter set to show executable files
:width: 90%
:align: center
:name: fig-ui-file-filter

Changing the file filter to show executable files.
```

3. Confirm the selection. The application remembers this path, so you only need to select it
   again if Roofer is moved or replaced.

```{figure} ../images/ui_roofer_saved.png
:alt: Settings window showing the saved path to roofer.exe
:width: 90%
:align: center
:name: fig-ui-roofer-saved

The saved Roofer path.
```

## Step 4: Prepare the configuration file

The application can run without a configuration file, but Roofer then uses default settings.
MultiRoofs provides a configuration file that produces a better model and the attribute
names used in the project, so it is advised to always use it.

1. Download the [MultiRoofs configuration file](https://github.com/multiroofs/cityjson-extension/blob/main/roofer-config/config_mr.toml)
   (`config_mr.toml`) and save it in the same folder as `wippolder.las` and `wippolder.gpkg`.

```{figure} ../images/ui_config_download.png
:alt: MultiRoofs configuration file on GitHub
:width: 100%
:align: center
:name: fig-ui-config-download

Downloading the MultiRoofs configuration file.
```

2. Open it in a text editor and check these lines:

| Setting | Meaning | Value for Wippolder |
|---|---|---|
| `polygon-source` | Path to the building footprints | `"wippolder.gpkg"` |
| `source` (under `[[pointclouds]]`) | Path to the point cloud | `["wippolder.las"]` |
| `output-directory` | Folder where the result is written | `"output/"` |
| `id-attribute` | Column of the footprints with the unique building ID | `"fid"` |
| `srs` | Coordinate reference system of the input data | `"EPSG:7415"` |
| `ground_class`, `building_class` | LAS class codes for ground and buildings | `2` and `6` |

```{figure} ../images/ui_config_edit.png
:alt: Configuration file with the paths to the footprints, point cloud and output folder
:width: 100%
:align: center
:name: fig-ui-config-edit

Setting the paths in the configuration file.
```

The files referenced in the configuration file must exist at those locations, otherwise Roofer
cannot read them. If Roofer reports that it cannot find the input files, replace the paths with
full paths, for example `"C:/Data/wippolder/wippolder.las"`.  

## Step 5: Run the reconstruction

1. In the **Configuration file** section, click **Browse** and select `config_mr.toml`.
   Because the paths to the point cloud and the footprints are defined in the configuration
   file, you do not need to select them in the interface.
2. Click **Generate LoD 2.2 CityJSON**.

```{figure} ../images/ui_config_select.png
:alt: Configuration file selected in the interface before starting the reconstruction
:width: 90%
:align: center
:name: fig-ui-config-select

Selecting the configuration file and starting the reconstruction.
```


3. Follow the progress in **Processing messages**. When the reconstruction is finished, a
   confirmation message appears. Click **OK**.

```{figure} ../images/ui_generate.png
:alt: Processing messages during the reconstruction and the confirmation message
:width: 90%
:align: center
:name: fig-ui-generate

Running the reconstruction and the confirmation message.
```

The result is a [CityJSONSeq](https://www.cityjson.org/cityjsonseq/) file (`.city.jsonl`). Each
run is stored in a separate timestamped folder inside the output folder, so earlier results are
not overwritten.

The sequence diagram below shows what happens between clicking **Generate LoD 2.2 CityJSON**
and the creation of the `.city.jsonl` file.

```{figure} ../images/ui_sequence_diagram.png
:alt: Sequence diagram of the LoD 2.2 CityJSON generation process
:width: 90%
:align: center
:name: fig-ui-sequence

Sequence diagram of the LoD 2.2 CityJSON generation process.
```

### Running without a configuration file

If you do not select a configuration file, select the inputs in the interface instead:

1. In **LiDAR point cloud(s)**, select `wippolder.las`. You can also select several files, or
   choose a folder in the drop-down menu. A folder must contain only `.las` or `.laz` files.
2. In **Building footprints**, select `wippolder.gpkg`.
3. In **Output folder**, select the folder where the result should be stored.
4. Click **Generate LoD 2.2 CityJSON**.

```{figure} ../images/ui_select_inputs.png
:alt: Point cloud, footprints and output folder selected in the interface
:width: 90%
:align: center
:name: fig-ui-select-inputs

Selecting the input files and the output folder.
```

Roofer then uses its default settings, and the MultiRoofs attribute names are not added.

## Step 6: Check the result

1. Click **View with CityJSON Ninja**. This opens [ninja](https://ninja.cityjson.org/), the
   online CityJSON viewer, in your browser, and opens the folder containing the result in the
   file manager.

```{figure} ../images/ui_view_ninja.png
:alt: ninja opened in the browser and the result folder opened in the file manager
:width: 90%
:align: center
:name: fig-ui-view-ninja

Opening ninja and the result folder.
```

2. In ninja, click **Browse** and select the generated file, or drag it from the file manager
   into the viewer.

```{figure} ../images/ninja_overview.png
:alt: LoD2.2 building models displayed in the ninja viewer
:width: 80%
:align: center
:name: fig-ninja

The reconstructed LoD2.2 buildings in ninja.
```

Click on a building to see its attributes, and on a roof surface to see attributes of that
surface, such as its slope (`roof-gradient`) and orientation (`roof-azimuth`).

```{figure} ../images/ninja_attributes.png
:alt: Attributes of a selected building and roof surface in ninja
:width: 80%
:align: center
:name: fig-ninja-attributes

Inspecting the attributes of a building and of a roof surface.
```

```{note}
Some CityJSON tools only read regular CityJSON files (`.city.json`), not CityJSONSeq. To convert
the result, use cjseq as described in
[Generate CityJSON on a terminal](./using-cli.md##Step 5: Convert the result to CityJSON with cjseq).
```

## Using your own data

To use your own point cloud and footprints, change the configuration file as follows:

- Set `polygon-source` and `source` to your own files.
- Set `id-attribute` to the column of your footprints that contains a **unique ID for each
  building**. This ID is essential: it is used later to link extra attributes to both the 2D
  footprint and the 3D model of each building.
- Set `srs` to the coordinate reference system of your data (for example `"EPSG:28992"`
  for the Dutch RD New system, or the relevant EPSG code for your country).
- Check that `ground_class` and `building_class` match the class codes in your point cloud.

These settings cannot be changed in the interface, so a configuration file is needed when your
data differs from the defaults.

```{figure} ../images/uniqueid.png
:alt: Attribute table of the footprints showing a column with a unique ID per building
:width: 80%
:align: center
:name: fig-uniqueid

The footprints must contain a column with a unique ID for each building.
```

The resulting CityJSON file can then be enriched with additional attributes for the MultiRoofs
tools (see .....)
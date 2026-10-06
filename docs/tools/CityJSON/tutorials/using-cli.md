# Generate CityJSON on a terminal

This tutorial shows how to reconstruct LoD2.2 building models from a classified LiDAR point
cloud and 2D building footprints using Roofer, and how to convert the result into a CityJSON
file. It uses a small demo dataset so you can check that everything works before using your
own data.

The workflow has four steps:

1. Install Roofer and download the demo data.
2. Run Roofer with the MultiRoofs configuration file. This produces a CityJSONSeq file (`.city.jsonl`).
3. Convert the CityJSONSeq file into a CityJSON file (`.city.json`) with cjseq.
4. Check the result in a web viewer.

The instructions are written for Windows. On macOS and Linux the steps are the same, but the
installation of Roofer differs; see the [Roofer documentation](https://innovation.3dbag.nl/roofer/getting_started.html).

## What you need

- A classified point cloud in LAS or LAZ format, with at least the classes Ground (2) and Building (6).
- Building footprints in a format that GDAL/OGR can read (for example GeoPackage), with one
  unique identifier per building.
- Roofer v1.0.0 or later.
- cjseq, which requires the Rust compiler to install.

## Step 1: Install Roofer and cjseq

See [Installing dependencies](./install-dependencies.md) for more details.

## Step 2: Download the demo datase

Download the [Wippolder dataset](./wippolder.zip) and unzip it. It covers a neighbourhood next 
to TU Delft with 60 buildings, and contains:

- `wippolder.las`: the classified point cloud
- `wippolder.gpkg`: the building footprints

```{figure} ../images/wippolder-roofer.las.png
:alt: Classified point cloud of the Wippolder neighbourhood
:width: 80%
:align: center
:name: fig-wippolder

The Wippolder demo point cloud.
```

## Step 3: Prepare the configuration file

Roofer can be run with only an input and output path, but it then uses default settings.
MultiRoofs provides a configuration file that produces a better model and the attribute
names used in the project, so it is advised to always use it.

1. Download the [MultiRoofs configuration file](https://github.com/multiroofs/cityjson-extension/blob/main/roofer-config/config_mr.toml)
   (`config_mr.toml`) and save it in the same folder as `wippolder.las` and `wippolder.gpkg`.
2. Open it in a text editor and check these lines:

| Setting | Meaning | Value for Wippolder |
|---|---|---|
| `polygon-source` | Path to the building footprints | `"wippolder.gpkg"` |
| `source` (under `[[pointclouds]]`) | Path to the point cloud | `["wippolder.las"]` |
| `output-directory` | Folder where the result is written | `"output/"` |
| `id-attribute` | Column of the footprints with the unique building ID | `"fid"` |
| `srs` | Coordinate reference system of the input data | `"EPSG:7415"` |
| `ground_class`, `building_class` | LAS class codes for ground and buildings | `2` and `6` |

For the demo data you do not need to change anything if the configuration file sits next to
the data. If you prefer to keep it elsewhere, replace the paths with full paths, for example
`"C:/Data/wippolder/wippolder.las"`.

## Step 4: Run Roofer

1. Open **Command Prompt** (in Windows, search for `cmd` in the Start menu).
2. Go to the folder containing the data and the configuration file with the `cd` command:

```
   cd C:\Data\wippolder
```

3. Run Roofer, using the full path to `roofer.exe` (or just `roofer` if its path was added to the 
environment variables) from Step 1:

```
   C:\Tools\roofer-Windows-Release-v1.0.0\bin\roofer.exe -c config_mr.toml
```

Roofer prints its progress (region of interest, number of footprints, reconstruction). When it
finishes, the output folder contains a file such as `085289_447042.city.jsonl`. The numbers in
the name come from the coordinates of the area that was processed, so they will differ for your
own data.

This file is a [CityJSONSeq](https://www.cityjson.org/cityjsonseq/) file: the same content as
CityJSON, but with one building per line. Most viewers and tools expect a regular CityJSON
file, so it must be converted in the next step.

```{figure} ../images/roofer_run.png
:alt: Command Prompt showing Roofer running with the MultiRoofs configuration file
:width: 90%
:align: center
:name: fig-roofer-run

Running Roofer from the Command Prompt.
```

```{warning}
Roofer writes its result to the output folder without asking. If you run it again with the
same output folder, the previous result can be overwritten. To keep and compare several runs,
change `output-directory` in the configuration file before each run, for example to
`"output_1/"` and then `"output_2/"`.
```

## Step 5: Convert the result to CityJSON with cjseq

1. In Command Prompt, go to the output folder:

```
   cd C:\Data\wippolder\output
```

2. Run the `collect` command, replacing the input name with the name of your file:

```
   cjseq collect 085289_447042.city.jsonl > wippolder.city.json
```

The file `wippolder.city.json` is your LoD2.2 building model in CityJSON format.

```{note}
Use Command Prompt rather than Windows PowerShell for this command. In Windows PowerShell 5.1
the `>` symbol saves the file in UTF-16 encoding, which some CityJSON tools cannot read.
```

```{figure} ../images/cjseq_run.png
:alt: Command Prompt showing the cjseq collect command converting city.jsonl into city.json
:width: 80%
:align: center
:name: fig-cjseq

Converting the CityJSONSeq file into a CityJSON file with cjseq. Nothing is printed on the terminal.
```

## Step 6: Check the result

Open [ninja](https://ninja.cityjson.org/), the online CityJSON viewer, and drag your
`.city.json` file into it. You should see the 3D buildings, and you can switch between the
available LoDs at the bottom of the viewer.

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

## Using your own data

To use your own point cloud and footprints, change the configuration file as follows:

- Set `polygon-source` and `source` to your own files.
- Set `id-attribute` to the column of your footprints that contains a **unique ID for each
  building**. This ID is essential: it is used later to link extra attributes to both the 2D
  footprint and the 3D model of each building.
- Set `srs` to the coordinate reference system of your data (for example `"EPSG:28992"`
  for the Dutch RD New system, or the relevant EPSG code for your country).
- Check that `ground_class` and `building_class` match the class codes in your point cloud.

```{figure} ../images/uniqueid.png
:alt: Attribute table of the footprints showing a column with a unique ID per building
:width: 80%
:align: center
:name: fig-uniqueid

The footprints must contain a column with a unique ID for each building.
```

The resulting CityJSON file can then be enriched with additional attributes for the MultiRoofs tools (see .....)
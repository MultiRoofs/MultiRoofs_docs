# Background

## 3D city models and CityJSON

A 3D city model is a digital representation of buildings and other city objects, where each
object has both a 3D geometry and descriptive attributes (for example, an identifier, a
construction year, or a roof type). Because each building is a separate object rather than
just a visual mesh, the model can be used for analyses such as solar potential, energy
demand, or roof suitability.

[CityJSON](https://www.cityjson.org/) is an open, JSON-based format for storing 3D city
models. It is an OGC Community Standard and follows the data model of CityGML, but it is
more compact and easier to read and write with standard programming tools. The tools
developed in the MultiRoofs project expect their input in this format.

## Level of Detail (LoD)

The same building can be modelled with more or less geometric detail. This is described by
its **Level of Detail (LoD)**. The original CityGML standard defines broad levels (LoD0 to
LoD4), which are refined into sub-levels in the framework of
[Biljecki et al. (2016)](https://doi.org/10.1016/j.compenvurbsys.2016.04.005), as shown in
{numref}`fig-lod`.

The levels most relevant to this guide are:

- **LoD1.2**: the building is a simple block (the footprint extruded to one height), with no
  roof shape. Small building parts are included.
- **LoD1.3**: the building is split into several blocks of different heights, so that parts
  with clearly different heights are distinguished, but all roofs are still flat.
- **LoD2.2**: the actual roof shape is modelled (sloped, gabled, hipped, and so on), including
  roof superstructures such as dormers when they are large enough. Walls are vertical, and
  roof overhangs are not modelled, so the roof edges follow the footprint.

LoD2.2 is the level that roofer produces and the level used in the 3DBAG. It is the most
relevant level for MultiRoofs, because roof analyses depend on knowing the slope,
orientation, and area of each individual roof surface, which LoD1 models do not provide.

```{figure} ../images/fig-lod.jpg
:alt: Visual example of the refined LODs for a residential building.
:width: 80%
:align: center
:name: fig-lod

Visual example of the refined LODs for a residential building.
```

## From input data to a 3D model

3D building datasets such as those available for The Netherlands ([3DBAG dataset](https://3dbag.nl/)) 
are often unavailable or limited to specific cities or regions. In such cases, 3D building models 
can still be generated automatically using ‘[roofer](https://doi.org/10.14358/PERS.21-00032R2)’, a 
reconstruction algorithm developed in TU Delft and used for the generation of 
3DBAG. The source code of ‘roofer’ is publicly available under the GPL-3.0 license, 
see [https://github.com/3DBAG/roofer](https://github.com/3DBAG/roofer). Roofer, as shown in 
{numref}`fig-roofer`, reconstructs each building automatically from two main inputs: a building footprint,
which tells it where the building is and gives it a unique identifier, and a classified
point cloud, which tells it the height and shape of the roof. The output is a CityJSON file
containing the 3D model of each building at several LoDs. The following sections describe
these input datasets and the requirements they must meet. 


```{figure} ../images/roofer.png
:alt: 3D reconstruction using aerial point clouds and building footprints resulting to LoD2.2
:width: 80%
:align: center
:name: fig-roofer

3D reconstruction using aerial point clouds and building footprints resulting to LoD2.2.
```

### Building footprints

Accurate 2D building outlines {numref}`fig-building-footprints` with unique identifiers that can be used for linking to other 
building data. Common formats include Shapefiles, GeoJSON, DXF/DWG, GeoPackage, or WFS services, 
typically provided by national mapping agencies or municipalities.

```{figure} ../images/building_footprints.png
:alt: Building footprints for Dutch buildings available from bag.nl
:width: 80%
:align: center
:name: fig-building-footprints

Building footprints for Dutch buildings available from bag.nl.
```

Similar to footprints, *roofprints* represent the ground projection of a building's roof. Though less 
commonly available, they provide detailed roof structure information that greatly aids 3D 
reconstruction. They are generally available in the same formats as footprints. 

### Classified LiDAR point clouds 

Point cloud data is usually provided in .las or .laz format, which are open standards. Reconstruction 
quality is highly dependent on point cloud density and coverage – sparse or occluded datasets 
significantly reduce accuracy. Thus, the point clouds should have sufficient density (≥10 pts/m²), 
and they should be inspected for occlusions. 

Regarding the classification, ‘Ground’ (class=2), ‘Building’ (class=6), and ‘Vegetation’ (class=3/4/5) 
classes are required for ‘roofer’, and they should be labelled based on the [standard LAS 
specification](https://www.ogc.org/standards/las/) code numbers ({numref}`fig-LiDAR`). These are required to prevent overhanging trees 
from being used to reconstruct the roof shape, enable the filtering of non-building elements, and 
improve the overall accuracy of the reconstruction process.


```{figure} ../images/LiDAR.png
:alt: Example of a classified aerial point cloud and the standard LAS classification codes
:width: 80%
:align: center
:name: fig-LiDAR

Example of a classified aerial point cloud and the standard LAS classification codes.
```

Typically, point clouds are generated using airborne lidar systems. However, if a lidar dataset is 
not available, point clouds can also be generated with dense image matching (DIM) techniques using 
aerial or even street view images. Such imaging datasets are useful for the generation of 
point clouds and for extracting additional information about the buildings and the roofs. 

Aerial images, captured from either a straight-down (nadir) or angled (oblique) perspective, provide 
rich radiometric data of building exteriors and their surroundings. The exterior orientation 
(position and angle of the camera when the image was taken) and its interior orientation (the 
intrinsic parameters of the camera) are crucial for accurate 3D photogrammetric processing. These 
images are often used for generating point clouds with a dense matching method, for detecting roof 
elements (such as chimneys or solar panels), for classifying roof materials, and for texturing 3D 
reconstructions.

Lastly, Orthophotomosaic (or true ortophotos) are high-resolution, geometrically corrected aerial 
images where all distortions from terrain and camera tilt have been removed, resulting in a uniform 
scale and orthographic projection. True orthophotos preserve vertical features and eliminate the 
parallax, which makes them suitable for overlaying with vector data. Resolution is a key factor – 
Ground Sampling Distance (GSD) should be ≤ 8 cm to ensure sufficient detail for tasks such as roof 
element detection, roof material classification, and realistic 3D model texturing.


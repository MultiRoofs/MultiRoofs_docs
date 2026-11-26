# How to import your data from a CSV

The **Import attributes from CSV** functionality in MRIO, which described in {ref}`MRIO website <attributes-from-CSV>` and the {ref}`MRIO CLI <attributes-cli-CSV>` documentation allows users to add additional attribute data from a CSV file to existing CityObjects in a CityJSON or CityJSONSeq fil.


## CSV file structure
After uploading your CityJSON or CityJSONSeq file to [MRIO website](https://multiroofs.github.io/mrio/), make sure that the CSV file containing the attributes to be added is available.

```{important}
The CityObject IDs in the **CSV file** must match the IDs in the **CityJSON file**. MRIO uses these IDs to find the correct CityObject for each row in the CSV file. The ID column is used for matching, while the other columns contain the new attributes that will be added to the CityObject.
```

{numref}`mrio-cityjsonandcsv`  illustrates the structure of the CityJSON and CSV files and shows how the CSV columns are used to associate new attributes with the corresponding CityObjects.

```{figure} ./images/cityjsonandcsv.png
:width: 700px
:align: center
:alt: CityJSON csv results
:name: mrio-cityjsonandcsv

Matching CSV Data with CityObject IDs
```


```{note}
The attribute columns in the CSV file do not need to already exist in the CityJSON file. They can represent new information that will be added to the corresponding CityObjects during the import process. For example, a CSV file may contain new attributes such as `solar_potential` and `owner_type`, even if these attributes are not currently present in the CityJSON file. 
```

The remaining columns contain the attributes that will be added to the
corresponding CityObjects.

For example:

| id | attribute_1 | attribute_2 |
|---|---|---:|
| NL.IMBAG.Pand.0503100000028341 | building_A | 100 |
| NL.IMBAG.Pand.0503100000028341-0 | building_part_A | 110 |
| NL.IMBAG.Pand.0503100000031927 | building_B | 200 |
| NL.IMBAG.Pand.0503100000031927-0 | building_part_B | 210 |

The CityObject ID is used for matching and is not added as a new
attribute.

## Import the CSV file
This section was discussed on the  {ref}`MRIO website <attributes-from-CSV>`  and in the {ref}`MRIO CLI <attributes-cli-CSV>`.


1.  Click **Import attributes from CSV** in the Operations panel.
2.  Select the CSV file containing the attributes.
3.  Confirm the import by clicking **Add attributes**.
4.  Wait for MRIO to process the file.

## Check the imported attributes

After the import is completed, check the **Attributes** section in the File Overview. You will also see a success message on the right corner indicating that the attribute has been successfully added to the CityJSON file.

```{figure} ./images/addedattribute.png
:width: 700px
:align: center
:alt: CityJSON csv attribute
:name: mrio-addedattribute

The imported attributes are shown in the screenshot.
```
The newly imported attributes should appear together with the existing
attributes of the dataset.

```{warning}
If the CityObject IDs in the CSV file do not match the IDs in the uploaded CityJSON file, MRIO cannot determine where the new attributes should be added. In this case, an **Operation failed** message is displayed. The message indicates that the CityObjects with the specified IDs were not found and shows how many attributes were successfully added. If this error occurs, check the IDs in the CSV file and make sure they match the corresponding CityObject IDs in the uploaded file before trying the import again.
```

```{figure} ./images/faild.png
:width: 700px
:align: center
:alt: CityJSON csv failed attribute
:name: mrio-failedttribute

Failed to import the attributes.
```

## Validate the result

After importing the CSV attributes, click **Validate file** to check the
resulting file structure. Validation can help identify problems in the processed dataset before
downloading it.


## Key takeaways

-   The CityObject IDs in the CSV must correspond to IDs in the uploaded
    CityJSON or CityJSONSeq file.
-   Check the CSV structure before importing it.
-   Verify the newly added attributes after the import.
-   Validate the file after making changes.
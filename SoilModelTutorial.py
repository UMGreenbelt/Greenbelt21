# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2021-04-09 14:27:31
"""
import arcpy

'''
INSTRUCTIONS:
Below is a list of property path names for all existing Greenbelt properties. These shapefiles were created using "Select By Attributes", 
with soil_carbon as Input Table and Site Owner as Split Fields. Property names containing "-" were renamed to "_" manually in ArcCatalog and 
some property names were shortened because there is a limit on number of characters in a name. Property names (A, B, C) are omitted for 
privacy reasons.

'''

existing_properties = ["D:\\Greenbelt\\Properties\\A.shp",
"D:\\Greenbelt\\Properties\\B.shp",
"D:\\Greenbelt\\Properties\\C.shp"]

def Model(property_path):  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\GeoAnalytics Desktop Tools.tbx")
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx")
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx")

    soil_carbon = "soil_carbon"

    property_shp = property_path
    property_name = property_path[24:-4] # extracts property name from path string

    # Process: Clip Layer (Clip Layer) 
    property_soil_shp = "D:\\Greenbelt\\soils\\April\\Soil\\" + property_name + "_Soil.shp"
    arcpy.gapro.ClipLayer(input_layer=soil_carbon, clip_layer=property_shp, out_feature_class=property_soil_shp)

    # Process: Add Fields (multiple) (Add Fields (multiple)) 
    Property_1 = arcpy.AddFields_management(in_table=property_soil_shp, field_description=[["low_kg", "FLOAT", "", "", "", ""], ["med_kg", "FLOAT", "", "", "", ""], ["high_kg", "FLOAT", "", "", "", ""], ["Area_m2", "FLOAT", "", "", "", ""]])[0]

    # Process: Calculate Geometry Attributes (Calculate Geometry Attributes) 
    Property_1 = arcpy.management.CalculateGeometryAttributes(in_features=Property_1, geometry_property=[["Area_m2", "AREA"]], length_unit="", area_unit="SQUARE_METERS", coordinate_system="", coordinate_format="SAME_AS_INPUT")[0]

    # Process: Calculate Field (Calculate Field) 
    Property_1 = arcpy.management.CalculateField(in_table=Property_1, field="low_kg", expression="!low_Carbon! * !Area_m2!", expression_type="PYTHON3", code_block="", field_type="TEXT")[0]

    # Process: Calculate Field (2) (Calculate Field) 
    Property_1 = arcpy.management.CalculateField(in_table=Property_1, field="med_kg", expression="!med_Carbon! * !Area_m2!", expression_type="PYTHON3", code_block="", field_type="TEXT")[0]

    # Process: Calculate Field (3) (Calculate Field) 
    Property_1 = arcpy.management.CalculateField(in_table=Property_1, field="high_kg", expression="!high_Carbo! * !Area_m2!", expression_type="PYTHON3", code_block="", field_type="TEXT")[0]

    # Process: Summary Statistics (Summary Statistics) 
    property_soil_carbon = "D:\\Greenbelt\\soils\\April\\SoilCarbon\\" + property_name + "_SoilCarbon"
    arcpy.Statistics_analysis(in_table=Property_1, out_table=property_soil_carbon, statistics_fields=[["low_kg", "SUM"], ["med_kg", "SUM"], ["high_kg", "SUM"]], case_field=["Cover"])

    # Process: Table To Excel (Table To Excel) 
    property_soil_carbon_xlsx = "D:\\Greenbelt\\soils\\April\\SoilCarbonTables\\" + property_name + "_SoilCarbon.xlsx"
    arcpy.conversion.TableToExcel(Input_Table=property_soil_carbon, Output_Excel_File=property_soil_carbon_xlsx, Use_field_alias_as_column_header="NAME", Use_domain_and_subtype_description="CODE")


if __name__ == '__main__':
    # Global Environment settings
    for property_path in existing_properties:
        with arcpy.EnvManager(scratchWorkspace=r"D:\Greenbelt\soils\April\April Soils.gdb", workspace=r"D:\Greenbelt\soils\April\April Soils.gdb"):
            Model(property_path)

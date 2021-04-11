## Greenbelt21
This repository is the home of the code we used for our SEAS Master of Science at the Univistsity of Michigan

### Soil Carbon Estimation by Jackie Edinger

### EGAL Water Ecosytem Services Website by Sebastian Kasparian

### Lidar Biomass Estimation Modeling by Lavran Pagano
Scripts:

Creating_Plot_Polygons = R script that creates plot polygons from the southwest corner of a plot. Greatly inspired by https://www.neonscience.org/resources/learning-hub/tutorials/field-data-polygons-centroids.

Extracting_Lidar_Predictor_Variables = R script for extracting the pixel distribution of a plot from a canopy height file(CHM). Then calculates various height precentiles and crown geometric volume of a plot.

Model_Comparison_Final = Using the created training data from Extracting_Lidar_Predictor_Variables a multiple linear regression, log-linear, random forest, and support vector regression model via a 10-fold cross-validation were compared to determine the most effective predictive model. 

Biomass_Function = A function used to make a canopy height model (CHM) into a biomass estimation raster with 10 meter by X 10 meter cell size using a log-linear model.

SoilModelTutorial = Python script for estimating belowground carbon storage (soil organic carbon) for existing Greenbelt properties.


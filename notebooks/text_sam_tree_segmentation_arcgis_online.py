"""
Text SAM Tree Segmentation in ArcGIS Online (ArcGIS Notebooks)

This script is designed to be copied into ArcGIS Online Notebook cells.
It retrieves an imagery layer from your ArcGIS Online content, loads the
Text SAM deep learning package hosted on ArcGIS Online, runs tree
segmentation using a text prompt, and visualizes the output polygons.

Author(s): Yifan Yang, Dominic Borrelli
"""

# ============================================================
# 0) Connect to GIS (ArcGIS Online Notebook default pattern)
# ============================================================
# In ArcGIS Online Notebooks, `gis` is typically available by default after you authenticate.
# If not, uncomment the following:
#
# from arcgis.gis import GIS
# gis = GIS("home")

from arcgis.learn import detect_objects

# ============================================================
# 1) Locate your imagery layer in ArcGIS Online content
# ============================================================
# IMPORTANT: Ensure you have already published your GeoTIFF as an Imagery Layer.
# You may need to adjust the search query to match your item name.

IMAGERY_ITEM_NAME = "Estella Public School"   # Change as needed

imagery_items = gis.content.search(IMAGERY_ITEM_NAME)
imagery_items

# Select the first matched item (adjust if multiple items returned)
study_area_item = imagery_items[0]
study_area_item

# The imagery layer is typically accessed via layers[0]
imagery_layer = study_area_item.layers[0]
imagery_layer

# ============================================================
# 2) Retrieve the Text SAM deep learning package from ArcGIS Online
# ============================================================
# This query searches across ArcGIS Online, not only your org.
# If the owner name or item name changes in the future, you may need to update this.

model_item = gis.content.search(
    'Segment Anything Model owner:esri_analytics',
    item_type="Deep Learning Package",
    outside_org=True
)[0]
model_item

# ============================================================
# 3) Run Text SAM detection/segmentation with a text prompt
# ============================================================
# Key parameters to consider tuning:
# - padding
# - batch_size
# - box_threshold
# - text_threshold
# - cellSize (spatial resolution for processing)

prompt = "tree"

trees = detect_objects(
    input_raster=imagery_layer,
    model=model_item,
    model_arguments={
        "text_prompt": prompt,
        "padding": "256",
        "batch_size": "4",
        "box_threshold": "0.24",
        "text_threshold": "0.24"
    },
    output_name="detectedTrees",
    context={
        "processorType": "GPU",
        "cellSize": "1"
    }
)

trees

# ============================================================
# 4) Visualize results in an interactive map
# ============================================================
m = gis.map()
m

m.add_layer(study_area_item)  # imagery
m.add_layer(trees)            # polygons
m.zoom_to_layer(trees)
m

# If polygons are not visible, try reordering layers in the map UI so polygons draw on top.

# ============================================================
# 5) (Optional) Notes for ArcGIS Pro usage
# ============================================================
# In ArcGIS Pro:
# - Map tab -> Add Data -> ArcGIS Online
# - Search for "detectedTrees" (or your output_name)
# - Add the feature layer to your map
#
# You may need to export features and project the data before area/distance analysis.

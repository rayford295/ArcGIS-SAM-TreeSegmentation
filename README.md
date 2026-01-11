# 🌳 Object Detection and Segmentation of Trees using Text SAM in ArcGIS Online

🚀 This repository provides an **English-only**, step-by-step **GeoAI workflow** for **tree object detection and segmentation** from **high-resolution aerial imagery** using **Text SAM (Segment Anything Model)** within **ArcGIS Online Notebooks** and the **ArcGIS API for Python**.

🧠 The workflow outputs **vectorized tree polygons**, enabling advanced **spatial analysis**, **urban greening assessment**, and **decision support** in **ArcGIS Pro**.

---

## 📚 Related Publication (Official / Legitimate Sources)

- 📘 **Esri Press — Book Page**  
  https://www.esri.com/en-us/esri-press/browse/security-first-geospatial-workflows-for-a-safe-and-equitable-world

- 📄 **ResearchGate — Chapter Page**  
  https://www.researchgate.net/publication/396514864_Object_detection_and_segmentation_of_trees_using_Text_SAM_in_ArcGIS_Online

> ⚠️ **Note**  
> This repository supports **learning, reproducibility, and teaching** for the workflow described in the chapter.  
> Please consult the links above for the **official and legitimate publication record**.

---

## 🎯 What You Will Do

By following this workflow, you will:

1. 🛰️ Upload a high-resolution aerial image as an **Imagery Layer** in ArcGIS Online  
2. ⚡ Launch an **ArcGIS Online Notebook (Advanced with GPU support)**  
3. 🤖 Retrieve the **Text SAM deep learning package** hosted on ArcGIS Online  
4. 🌲 Perform **tree segmentation** using a natural-language text prompt (e.g., `"tree"`)  
5. 🗺️ Export and analyze **vector tree polygons** in **ArcGIS Pro**

---

## 🧰 Requirements

### 🧭 ArcGIS / Esri
You will need:
- An **ArcGIS Online** account with access to:
  - ✅ **ArcGIS Notebooks for ArcGIS Online**
  - ✅ **ArcGIS Image for ArcGIS Online** *(required for Imagery Layer publishing)*

### 📦 Data
- High-resolution aerial imagery (GeoTIFF recommended)  
- Example source: **OpenAerialMap**  
- Chapter example: *Estella Public School (New South Wales, Australia)*

---

## ⚡ Quick Start (ArcGIS Online)

### 🟢 Step 1 — Upload imagery as an Imagery Layer
1. Download an aerial image (GeoTIFF recommended).
2. In ArcGIS Online: **Content → New Item → Imagery Layer**
3. Select:
   - **Tiled Imagery Layer**
   - **One Image**
4. Upload and publish the imagery.

---

### 🟢 Step 2 — Create a GPU Notebook
1. Navigate to **Notebooks** in ArcGIS Online.
2. Select **New Notebook → Advanced with GPU support**  
   > ⚠️ *Note: GPU notebooks consume ArcGIS credits.*

---

### 🟢 Step 3 — Run the workflow
📂 Open:
➡️ Copy each section into **ArcGIS Notebook cells** and run sequentially.

---

## 📤 Output

- 🌳 **`detectedTrees`** — Feature Layer (tree polygons)
- 👀 Viewable in **ArcGIS Online Map Viewer**
- 🧮 Importable into **ArcGIS Pro** for:
  - Area calculation
  - Density analysis
  - Proximity & accessibility studies
  - Canopy coverage estimation

---

## 🔍 Recommended Follow-up Analyses (ArcGIS Pro)

Once tree polygons are generated, consider:

- 📐 **Tree canopy coverage** (aggregate polygon area)
- 📊 **Tree density surfaces** (kernel density, tessellation summaries)
- 🚸 **Proximity to infrastructure** (schools, roads, public facilities)
- 🌡️ **Equity & environmental exposure overlays**  
  (urban heat, air quality, vulnerable communities)

---

## 🎛️ Notes on Accuracy & Performance

Segmentation quality depends on:
- 🖼️ Imagery resolution
- 🧩 Scene complexity
- 📝 Text prompt specificity

Recommended tuning strategies:
- Adjust **box / text thresholds**
- Modify **padding** and **batch size**
- Apply **post-processing**:
  - Eliminate sliver polygons
  - Dissolve adjacent features
  - Simplify geometry
  - Run topology checks

---

## 📝 Citation

If you use or extend this workflow in **academic work**, please cite:
- The corresponding **book chapter**
- Relevant **SAM / Text SAM references**

---

## 📜 License

🔓 Add a license appropriate to your use case (e.g., **MIT License** for code).

> ⚠️ If figures or text from the book chapter are reused, ensure compliance with **Esri Press publisher permissions**.

---

## 📬 Contact

If you encounter:
- Missing code segments
- Reproducibility issues
- Questions about extending the workflow

📧 Please contact:  
**Yifan Yang**  
(see email in GitHub profile or publication contact information)

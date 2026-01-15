# Hydrochemical Variability in Southcentral Alaska  

This repository contains the code, dataset access instructions, and analysis for the research project:  

**“Analysis of Hydrochemical Variability in Southcentral Alaska Using Clustering Techniques and GIS”**  

The study applies clustering (K-Means, DBSCAN) and geospatial analysis (GIS, Kriging interpolation, Folium mapping) to investigate hydrochemical variability across Southcentral Alaska. It identifies distinct geochemical zones and contamination hotspots that can inform water resource management and environmental decision-making.  

---

## 📖 Project Overview  
- **Dataset**: Hydrochemical and geospatial data from Southcentral Alaska (HydroShare).  
- **Clustering Techniques**:  
  - K-Means → 5 distinct geochemical clusters  
  - DBSCAN → 2 dense clusters + anomalies (possible contamination hotspots)  
- **Spatial Analysis**:  
  - Kriging interpolation for unsampled regions  
  - Folium maps for interactive visualization  
- **Goal**: Combine clustering with GIS to reveal geochemical zones and contamination hotspots.  

---

## 📊 Dataset  

The dataset is publicly available on HydroShare under **CC BY 4.0 license**:  

Coombs & Carling (2025). *Water chemistry from Southcentral Alaska glacial watersheds*.  
🔗 DOI: [10.4211/hs.68cfd9f523794370bf1b750d48f05a90](https://doi.org/10.4211/hs.68cfd9f523794370bf1b750d48f05a90)  

### Download Instructions  
To download the dataset into the `data/` folder, run:  
```bash
python data/download_data.py
```
## 📂 Project Structure
```
alaska-hydrochem-clustering/
│── data/
│   ├── download_data.py      # Script to fetch dataset (must be run manually)
│   └── Raw_Data.xlsx         # Downloaded dataset (ignored in Git)
│
│── notebooks/
│   └── research.ipynb        # Main notebook with clustering + GIS analysis
│
│── results/
│   ├── figures/              # Cluster plots, kriging maps
│   │   ├── K-Means_Result.png
│   │   ├── DBSCAN_Result.png
│   │   └── Spatial_Interpolation_Results.png
│   └── interactive_map.html  # Exported Folium interactive map
│
│── README.md                 # Project documentation
│── requirements.txt          # Python dependencies
│── LICENSE                   # CC BY-NC-ND for code/results + dataset license note
```
## 🚀 Usage
### 1. Clone the repository
```bash
git clone https://github.com/abhinavflac/alaska-hydrochem-clustering.git
cd alaska-hydrochem-clustering
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Download dataset
```bash
python data/download_data.py
```
### 4. Run the notebook
```bash
jupyter notebook notebooks/research.ipynb
```
## 📌 Results  

### 🔹 K-Means Clustering  
Identified **5 geochemical zones** across Southcentral Alaska.  

![KMeans Clustering](results/figures/K-Means_Result.png)  

---

### 🔹 DBSCAN Clustering  
Detected **2 dense clusters** and several **noise points** (potential contamination anomalies).  

![DBSCAN Clustering](results/figures/DBSCAN_Result.png)  

---

### 🔹 Kriging Interpolation  
Predicted **pH distribution** at unsampled points, showing smooth transitions and contamination near urban/agricultural zones.  

![Kriging Interpolation](results/figures/Spatial_Interpolation_Results.png)  


### 🔹 Interactive Map  
An interactive Folium map visualizing hydrochemical zones:  
📍 [View Map on Figshare](https://figshare.com/articles/dataset/Hydrochemical_Clusters_Map_K-Means_Clustering_Results_for_Southcentral_Alaska/28188833)
Or open locally:
```bash
results/interactive_map.html
```
# 📜 License

**Code & Results:** Licensed under Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)  
You may share this work with attribution.  
You may not modify it.  
You may not use it commercially.

**Dataset:** Licensed separately under CC BY 4.0 (HydroShare).

**Citation:**  
Coombs & Carling (2025). Water chemistry from Southcentral Alaska glacial watersheds. HydroShare.  
DOI: 10.4211/hs.68cfd9f523794370bf1b750d48f05a90


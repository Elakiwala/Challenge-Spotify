# Spotify Top Hits — Unsupervised Learning Challenge

**IMT Atlantique — Unsupervised Learning Challenge**  
**Grade:** 9/10 — *Winning Team (1st place among 3 groups of 6 students each)*  
> “Complete and detailed analysis, diverse results, well-understood interpretations, and a clear report.”

---

## Project Overview

This repository presents a complete unsupervised learning pipeline applied to the **Spotify Top Hits (2000–2022)** dataset.  
The goal was to identify **latent musical structures** and **hidden relationships** among tracks using only audio and artist-related features, without any labels.

The pipeline was designed and executed in **Python (Jupyter Notebooks)**, following a modular structure:
1. Exploratory Data Analysis (EDA)
2. Data Preprocessing and Feature Scaling
3. Dimensionality Reduction (PCA)
4. Clustering (K-Means and Gaussian Mixture Models)
5. Nonlinear Projection (t-SNE)
6. Interpretation and Visualization

---

## Dataset Summary

| Category | Description |
|-----------|-------------|
| **Tracks** | 2,300 |
| **Period** | 2000–2022 |
| **Features** | 23 total (13 audio, 4 artist, 2 playlist, 1 album, 3 track metadata) |
| **Source** | Spotify Top Hits Playlists |
| **Format** | CSV — curated dataset of audio and artist attributes |

### Example Features
- **Audio descriptors:** danceability, energy, loudness, valence, acousticness, instrumentalness, liveness, tempo  
- **Artist attributes:** artist popularity, genre  
- **Temporal:** year of release  

---

## 1. Exploratory Data Analysis 

### Objectives
- Understand variable distributions, detect anomalies, and uncover trends over time.

### Highlights
- Only 1 missing row detected and removed.  
- Genre imbalance: *Pop* and *Dance Pop* dominate (>50%).  
- Positive correlation between **energy** and **loudness**.  
- Temporal trend: increasing energy and tempo from 2000 → 2020.

### Example Visualizations
- ![Feature Distributions](reports/figures/EDA/eda_feature_distributions.png)
- ![Energy Over Time](reports/figures/EDA/trend_energy_danceability.png)

---

## 2. Data Preprocessing

### Steps
1. Removed identifiers: `playlist_url`, `track_id`, `track_name`, `album`, `artist_id`, `artist_name`.  
2. Log transformed skewed variables:  
   `instrumentalness`, `speechiness`, `acousticness`, `liveness`, `duration_ms`.  
3. Scaled all numeric features using **StandardScaler**.  
4. Grouped similar genres into macro categories (Pop, Rock, Hip-Hop, EDM, R&B…).  
5. Saved final processed dataset to:  
   `data/processed/playlist_2000to2022_preprocessed_v2.csv`.

---

## 3. Principal Component Analysis

PCA was used to reduce dimensionality while preserving interpretability.

| Metric | Value |
|---------|-------|
| Number of components | 10 |
| Cumulative variance explained | 85.9% |

### Interpretation
- **PC1 — Energy / Production Intensity**  
  High energy, loudness, and valence → *energetic & happy* vs *soft & acoustic* songs.  
- **PC2 — Danceability / Positivity**  
  Driven by danceability, valence, tempo, and mode → *rhythmic & upbeat* dimension.

### Key Visualizations
- ![PCA Correlation Circle](reports/figures/Preprocessing/pca_correlation_circle.png)
- ![PCA Scatter by Genre](reports/figures/Preprocessing/pca_genre_scatter.png)

---

## 4. K-Means Clustering

K-Means was applied to the 10D PCA space to identify groups of similar songs.

### Methodology
- Tested k ∈ [2, 10]  
- Evaluated with **Elbow Method** and **Silhouette Score**  
- Optimal value: **k = 6**

### Example Results

| Cluster | Characteristics | Dominant Genres | Energy | Valence | Popularity |
|----------|----------------|-----------------|---------|----------|-------------|
| **C1** | Highly energetic and positive | Pop / Dance Pop | High | High | High |
| **C2** | Calm and acoustic | Indie / Folk | Low | Low | Medium |
| **C3** | Rhythmic and urban | Hip-Hop / Trap | Medium | Medium | High |
| **C4** | Aggressive and fast | Rock / Metal | Very High | Medium | Low |
| **C5** | Balanced mix | Pop / R&B / EDM | Medium | Balanced | Medium |
| **C6** | Electronic and upbeat | EDM / Electro | High | High | High |

### Visualizations
- ![KMeans Elbow and Silhouette](reports/figures/Clustering/kmeans_elbow_silhouette.png)
- ![Clusters in PCA Space](reports/figures/Clustering/pca_clusters.png)
- ![t-SNE Visualization colored by GMM Clusters](reports/figures/Clustering/tsne_gmm_clusters.png)


---

## 5. Gaussian Mixture Models (GMM)

To capture *softer boundaries* between musical styles, a **Gaussian Mixture Model (GMM)** was also trained.

### Methodology
- Model: `GaussianMixture(n_components=5, covariance_type='full', random_state=42)`
- Evaluated with **Silhouette Score**
- Result: `GMM Silhouette Score ≈ 0.32` (slightly lower than K-Means but more flexible)

### Interpretation
- Clusters **overlap strongly**: confirms that musical styles form a *continuum* rather than discrete categories.  
- Songs blend progressively between energetic pop, hip-hop, and acoustic tracks.

---

## 6. Nonlinear Projection with t-SNE

To further visualize high-dimensional patterns, **t-SNE** (t-Distributed Stochastic Neighbor Embedding) was applied.  
Unlike PCA, t-SNE is nonlinear and captures local neighborhood relationships.

### Configuration
```python
TSNE(n_components=2, perplexity=30, random_state=42)
```
---

## 7. Key Insights

1. **No sharp genre boundaries** — Audio features evolve smoothly across styles.  
2. **PCA + K-Means** yields interpretable, compact clustering (6 clusters).  
3. **GMM + t-SNE** provides a more continuous and realistic view of musical similarity.  
4. **Energy, Loudness, and Valence** are the most discriminative variables for musical clustering.  
5. The dataset confirms that *modern hits increasingly favor energetic, danceable sounds.*

---

## 8. Technical Stack

| Category | Tools |
|-----------|-------|
| **Language** | Python 3.11 |
| **Libraries** | pandas, numpy, scikit-learn, matplotlib, seaborn, missingno |
| **Methods** | StandardScaler, PCA, K-Means, GaussianMixture, t-SNE |
| **Visualization Tools** | matplotlib, seaborn |

---
---

## 9. Authors

**Team Spotify Top Hits — IMT Atlantique (2025)**  
- Achraf Essaleh  
- Sara ELBARI
- Nada ALEIAN
- Eva LANSALOT
- Houda DAOUAIRI
- Kalis KRAÏFI  

---

## 10. License

This project is for **educational and academic use** only.  
Dataset © Spotify — used under fair academic use for non-commercial research.

---
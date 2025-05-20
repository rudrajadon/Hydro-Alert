# System Architecture

## Data Pipeline

1. **Ingestion**
    - Download GPM IMERG precipitation data (NASA)
    - Download SRTM/AW3D30 (DEM/Elevation)
    - Download MODIS/Sentinel-1 SAR (flood extent)

2. **Preprocessing**
    - Harmonize spatial/temporal grids
    - Feature engineering (e.g., rainfall sums, elevation gradients)

3. **Modeling**
    - ML/DL model training (Random Forest, SVM, LSTM, CNN-LSTM)
    - Model evaluation and selection

4. **Serving**
    - Expose predictions via REST API (FastAPI/Flask)
    - Route requests via Node backend

5. **Visualization**
    - Real-time dashboard with map and alerts (React + Mapbox/Leaflet)

## Data Flow

```
Satellite APIs -> [Ingestion Scripts] -> data/raw/ -> [Preprocessing] -> data/processed/
-> [Model Training] -> model/ -> [Model API] -> backend/ -> frontend/
```

## Repositories

- **Main:** ai-flood-forecasting (monorepo)
- **Subdirectories:** model, data, scripts, backend, frontend

---
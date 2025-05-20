# Hydro-Alert Setup Guide

## 1. Clone or Initialize Repository

```bash
git clone https://github.com/[your-username]/Hydro-Alert.git
cd Hydro-Alert
# OR if already initialized:
git init
git add .
git commit -m "Initial commit: Project scaffold and Week 1 scripts"
```

## 2. Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install requests rasterio boto3
```

## 3. Directory Preparation

Folders will be created as needed by scripts in `scripts/`.

## 4. Data Acquisition

- Edit NASA and Copernicus credentials in scripts as required.
- Run scripts in order:
    - `download_gpm_imerg.py`
    - `download_srtm_dem.py`
    - `download_modis_flood.py`
- For MODIS/Sentinel-1, follow manual data download instructions if automation is not set up.

---
"""
Download SRTM DEM tiles using AWS Open Data.
This script uses rasterio to download a DEM tile by bounding box.
"""

import rasterio
from rasterio.session import AWSSession
import boto3
import os

def download_srtm_tile(lon, lat, out_dir="./data/raw/srtm/"):
    os.makedirs(out_dir, exist_ok=True)
    # SRTM tiles are named like N37E077
    lat_prefix = "N" if lat >= 0 else "S"
    lon_prefix = "E" if lon >= 0 else "W"
    tile = f"{lat_prefix}{abs(int(lat)):02d}{lon_prefix}{abs(int(lon)):03d}"
    url = f"s3://raster/SRTM3/{tile}.SRTMGL3.hgt.zip"
    out_path = os.path.join(out_dir, f"{tile}.hgt.zip")
    # Use AWS session (no credentials needed for public bucket)
    session = AWSSession(boto3.Session())
    with rasterio.Env(session):
        try:
            with rasterio.open(url) as src:
                data = src.read(1)
                print(f"Downloaded {tile}")
        except Exception as e:
            print(f"Failed to download {tile}: {e}")

# Usage (example for Delhi region):
# download_srtm_tile(77, 28)
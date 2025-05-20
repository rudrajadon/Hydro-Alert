"""
Download Sentinel-1 SAR data for flood mapping using the Copernicus Open Access Hub.
Requires: pip install sentinelsat
- Get a free account at https://scihub.copernicus.eu/dhus/#/self-registration
- Read sentinelsat docs: https://sentinelsat.readthedocs.io/
"""

from sentinelsat import SentinelAPI, geojson_to_wkt
from datetime import datetime
import os

def download_sentinel1(
    username,
    password,
    bbox,
    start_date,
    end_date,
    out_dir="./data/raw/sentinel1/"
):
    """
    Download Sentinel-1 SAR scenes within a bounding box and date range.
    bbox: (min_lon, min_lat, max_lon, max_lat)
    start_date, end_date: "YYYYMMDD"
    """
    os.makedirs(out_dir, exist_ok=True)
    api = SentinelAPI(username, password, 'https://apihub.copernicus.eu/apihub')

    # Convert bbox to geojson polygon WKT
    footprint = geojson_to_wkt({
        "type": "Polygon",
        "coordinates": [[
            [bbox[0], bbox[1]],
            [bbox[0], bbox[3]],
            [bbox[2], bbox[3]],
            [bbox[2], bbox[1]],
            [bbox[0], bbox[1]]
        ]]
    })
    products = api.query(
        footprint,
        date=(datetime.strptime(start_date, "%Y%m%d"), datetime.strptime(end_date, "%Y%m%d")),
        platformname='Sentinel-1',
        producttype='GRD',
        sensoroperationalmode='IW'
    )
    print(f"Found {len(products)} products. Downloading (this may take time and space)...")
    if not products:
        print("No products found for the specified region and date.")
        return
    api.download_all(products, directory_path=out_dir)
    print("Download complete.")

# Usage example (uncomment and enter your username/password and desired region/dates):
# download_sentinel1(
#     "YOUR_COPERNICUS_USERNAME",
#     "YOUR_COPERNICUS_PASSWORD",
#     (77, 28, 78, 29),          # bbox: min_lon, min_lat, max_lon, max_lat (example: Delhi region)
#     "20240501", "20240507"
# )
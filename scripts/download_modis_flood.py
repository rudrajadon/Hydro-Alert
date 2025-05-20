"""
Download MODIS Flood products from NASA FIRMS or LAADS.
This script provides a template for manual or API-assisted download.
"""

import os

def download_modis_flood(date, out_dir="./data/raw/modis/"):
    # For actual API/download automation, check https://firms.modaps.eosdis.nasa.gov/download/
    os.makedirs(out_dir, exist_ok=True)
    # Example product: MOD09A1 (8-day surface reflectance)
    file_name = f"MOD09A1.A{date}.h21v07.006.*.hdf"
    url = f"https://e4ftl01.cr.usgs.gov/MOLT/MOD09A1.006/{date}/"
    print(f"Please download {file_name} from {url} manually or use the LAADS API.")
    # You can automate this with authentication as needed

# Usage (prints instructions):
# download_modis_flood("20240101")
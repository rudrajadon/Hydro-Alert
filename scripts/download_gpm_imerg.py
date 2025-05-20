"""
Download GPM IMERG daily precipitation data from NASA GES DISC.
Requires NASA Earthdata account.
"""

import os
import requests
from datetime import datetime, timedelta

BASE_URL = "https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGDF.06"
DATA_DIR = "./data/raw/gpm_imerg/"
START_DATE = "2024-01-01"
END_DATE = "2024-01-07"

def daterange(start, end):
    for n in range(int((end - start).days)):
        yield start + timedelta(n)

def download_gpm_imerg(username, password, start_date, end_date):
    os.makedirs(DATA_DIR, exist_ok=True)
    session = requests.Session()
    session.auth = (username, password)
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    for date in daterange(start, end):
        date_str = date.strftime("%Y%m%d")
        file_name = f"3B-DAY.MS.MRG.3IMERG.{date_str}-S000000-E235959.V06.nc4"
        url = f"{BASE_URL}/{date.year}/{date.month:02d}/{file_name}"
        local_path = os.path.join(DATA_DIR, file_name)
        if not os.path.exists(local_path):
            print(f"Downloading {file_name}...")
            r = session.get(url)
            if r.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(r.content)
            else:
                print(f"Failed to download {file_name} ({r.status_code})")
        else:
            print(f"{file_name} already exists.")

# Usage (uncomment and fill credentials to run):
# download_gpm_imerg("YOUR_NASA_USERNAME", "YOUR_NASA_PASSWORD", START_DATE, END_DATE)
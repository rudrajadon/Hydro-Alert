import requests
from datetime import datetime, timedelta
import os

email = "rudrajadon18@gmail.com"  # <-- CHANGE THIS!
start_date = datetime(2024, 1, 1)
end_date = datetime(2024, 1, 7)
possible_versions = ["V07E", "V07D", "V07C", "V07B", "V07A"]  # Try most recent first!

base_url = "https://jsimpsonhttps.pps.eosdis.nasa.gov/imerg/gis"
output_dir = "data/raw/imerg_gis_1day_late/"
os.makedirs(output_dir, exist_ok=True)

for n in range((end_date - start_date).days + 1):
    date = start_date + timedelta(n)
    yyyy = date.strftime("%Y")
    mm = date.strftime("%m")
    yyyymmdd = date.strftime("%Y%m%d")
    found = False
    for version in possible_versions:
        filename = f"3B-DAY-L.GIS.IMERG.{yyyymmdd}.{version}.tif"
        url = f"{base_url}/{yyyy}/{mm}/{filename}"
        output_path = os.path.join(output_dir, filename)
        print(f"Trying {filename} ...")
        r = requests.get(url, auth=(email, email))
        if r.status_code == 200:
            with open(output_path, "wb") as f:
                f.write(r.content)
            print(f"Saved: {output_path}")
            found = True
            break
        else:
            print(f"Not found: {filename} (status {r.status_code})")
    if not found:
        print(f"No file found for {yyyymmdd} with any known version suffix.")
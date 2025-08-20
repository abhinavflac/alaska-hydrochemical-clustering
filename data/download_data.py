import requests
import os

# HydroShare resource download URL
url = "https://www.hydroshare.org/resource/68cfd9f523794370bf1b750d48f05a90/data/contents/SouthcentralAlaska_HydroShare.xlsx"

# Output file
out_file = os.path.join(os.path.dirname(__file__), "SouthcentralAlaska_HydroShare.xlsx")

print(f"Downloading dataset from HydroShare...")
response = requests.get(url, stream=True)

if response.status_code == 200:
    with open(out_file, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"✅ Dataset saved as {out_file}")
else:
    print(f"❌ Failed to download dataset (status {response.status_code})")

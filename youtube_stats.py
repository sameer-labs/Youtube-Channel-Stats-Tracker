import os
import csv
import requests
from datetime import date
from dotenv import load_dotenv

from pathlib import Path
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# -----------
# API SET-UP
# -----------

API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = "UCkzzNLnuM-VsATWC53ehwOQ" # Wemmbu
OUTPUT_DIR = "output"

# -----------
# FETCH STATS
# -----------

def fetch_channel_stats():
    url = "https://www.googleapis.com/youtube/v3/channels"
    params = {
        "part": "snippet,statistics",
        "id": CHANNEL_ID,
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    print("Status code:", response.status_code)

    data = response.json()
    if response.status_code != 200:
        print("Raw API response:")
        print(data)
        raise Exception("API request failed — see output above")



    if "items" not in data or not data["items"]:
        raise Exception(f"API Error: {data}")

    item = data["items"][0]


    return {
            "date": date.today().isoformat(),
            "channel_name": item["snippet"]["title"],
            "subscriber_count": item["statistics"]["subscriberCount"],
            "total_views": item["statistics"]["viewCount"],
            "video_count": item["statistics"]["videoCount"]
    }

# -----------
# WRITE CSV
# -----------

def save_csv(stats):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    filename = f"{OUTPUT_DIR}/youtube_stats_{stats['date']}.csv"

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=stats.keys())
        writer.writeheader()
        writer.writerow(stats)
    
    print(f"Saved report: {filename}")

# -----------
# MAIN CONSOLE
# -----------

def main():
    stats = fetch_channel_stats()
    save_csv(stats)

if __name__ == "__main__":
    main()

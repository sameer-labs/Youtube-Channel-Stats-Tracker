# 📊 YouTube Channel Stats Tracker

> Because manually checking subscriber counts every week is so 2015 😅

## 🎯 What Is This?

Ever wanted to track your favourite YouTube channels without opening 47 browser tabs? Same. 

This little Python script pulls **live YouTube channel stats** and dumps them into a clean, dated CSV file. No dashboards, no login walls—just pure data you can actually use.

Perfect for creators tracking competitors, marketers building reports, or devs who just love automating stuff (hi 👋).

## ✨ What It Does

- 🔌 Connects to the **YouTube Data API v3**
- 📥 Fetches channel-level stats (subs, views, video count)
- 💾 Saves everything to a timestamped CSV file
- 🚀 Runs in seconds

## 🧪 Input → Output

### Input
- YouTube channel ID (that weird `UC...` string)
- Your YouTube API key

### Output
A beautiful CSV with:
- 📅 `date` — when you ran this
- 🎮 `channel_name` — channel title
- 👥 `subscriber_count` — current subs
- 👀 `total_views` — all-time views
- 🎬 `video_count` — total videos uploaded

## 🚀 Quick Start
```bash
# Install the only dependency (yes, just one!)
pip install requests

# Set your API key
export YOUTUBE_API_KEY=your_api_key_here

# Run it!
python youtube_stats.py
```

That's it. Seriously. ✅

## 🔑 Getting Your API Key

1. Head to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or use an existing one)
3. Enable **YouTube Data API v3**
4. Generate an API key
5. Copy-paste into your environment

## 💡 Why I Built This

I was tired of manually checking stats on a dozen Minecraft YouTubers for a personal project. Figured other devs might find it useful too. Plus, it's a clean example of working with Google's APIs without overcomplicating things.

## 🛠️ Tech Stack

- **Python 3.x** — because life's too short for Python 2
- **Requests library** — HTTP made human-friendly
- **YouTube Data API v3** — Google's gift to data nerds

## 📝 Notes

- Free tier = 10,000 API quota units/day (plenty for tracking channels)
- Each channel stats call = ~3 units
- CSV gets prettier with each run 📈

---

Built with ☕ and curiosity. Feel free to fork, star, or roast my code—I'm here for it all. 🤙

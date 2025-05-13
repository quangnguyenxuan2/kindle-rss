import feedparser
import os

FEED_URL = "https://vnexpress.net/rss/tin-moi-nhat.rss"
feed = feedparser.parse(FEED_URL)

os.makedirs("public", exist_ok=True)

with open("public/index.html", "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='UTF-8'><title>Báo Mới</title></head><body>")
    f.write("<h1>Tin mới từ VnExpress</h1><ul>")
    for entry in feed.entries[:30]:
        f.write(f"<li><a href='{entry.link}'>{entry.title}</a></li>")
    f.write("</ul></body></html>")

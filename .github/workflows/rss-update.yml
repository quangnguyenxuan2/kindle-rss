import feedparser
import os

# Danh sách các nguồn báo
feeds = {
    "VnExpress": "https://vnexpress.net/rss/tin-moi-nhat.rss",
    "Tuổi Trẻ": "https://tuoitre.vn/rss/tin-moi-nhat.rss",
    "Thanh Niên": "https://thanhnien.vn/rss/home.rss",
    "24h": "https://cdn.24h.com.vn/upload/rss/trangchu24h.rss"
}

# Tạo thư mục xuất HTML
os.makedirs("public", exist_ok=True)

# Tạo file index
with open("public/index.html", "w", encoding="utf-8") as f:
    f.write("<html><head><meta charset='UTF-8'><title>Báo mới</title></head><body>")
    f.write("<h1>Tin tức mới nhất (Tự động cập nhật mỗi 2 tiếng)</h1>")

    for name, url in feeds.items():
        f.write(f"<h2>{name}</h2><ul>")
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:
            f.write(f"<li><a href='{entry.link}'>{entry.title}</a></li>")
        f.write("</ul>")

    f.write("</body></html>")

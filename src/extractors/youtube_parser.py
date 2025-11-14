thonpython
import logging

class YouTubeParser:
    def search(self, keyword: str) -> dict:
        logging.info(f"Mock scraping YouTube for '{keyword}'")
        return {
            "keyword": keyword,
            "exact_match": True,
            "username": f"{keyword}_yt",
            "followers": "2.3M",
            "raw_followers": 2300000,
            "network": "youtube",
            "name": f"{keyword.title()} YouTube",
            "is_visible": True,
            "engagement": 0.021,
            "location": ["United Kingdom"],
            "handle": f"@{keyword}_yt",
            "categories": ["Humor"],
            "bio": f"Mock YouTube profile for {keyword}.",
            "gallery": [
                {"comments": "3", "likes": "16", "code": "yt111", "url": "https://youtube.com/mock1"},
                {"comments": "4", "likes": "19", "code": "yt222", "url": "https://youtube.com/mock2"},
            ],
        }
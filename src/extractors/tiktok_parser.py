thonpython
import logging

class TikTokParser:
    def search(self, keyword: str) -> dict:
        logging.info(f"Mock scraping TikTok for '{keyword}'")
        return {
            "keyword": keyword,
            "exact_match": True,
            "username": f"{keyword}_tiktok",
            "followers": "1.2M",
            "raw_followers": 1200000,
            "network": "tiktok",
            "name": f"{keyword.title()} TikTok",
            "is_visible": True,
            "engagement": 0.045,
            "location": ["USA"],
            "handle": f"@{keyword}_tiktok",
            "categories": ["Entertainment"],
            "bio": f"This is a mock TikTok profile for {keyword}.",
            "gallery": [
                {"comments": "10", "likes": "200", "code": "abc123", "url": "https://tiktok.com/mock1"},
                {"comments": "14", "likes": "250", "code": "def456", "url": "https://tiktok.com/mock2"},
            ],
        }
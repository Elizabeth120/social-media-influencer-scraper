thonpython
import logging

class InstagramParser:
    def search(self, keyword: str) -> dict:
        logging.info(f"Mock scraping Instagram for '{keyword}'")
        return {
            "keyword": keyword,
            "exact_match": False,
            "username": f"{keyword}_ig",
            "followers": "850K",
            "raw_followers": 850000,
            "network": "instagram",
            "name": f"{keyword.title()} IG",
            "is_visible": True,
            "engagement": 0.061,
            "location": ["Canada"],
            "handle": f"@{keyword}_ig",
            "categories": ["Lifestyle"],
            "bio": f"Mock Instagram profile for {keyword}.",
            "gallery": [
                {"comments": "5", "likes": "120", "code": "xyz888", "url": "https://instagram.com/mock1"},
                {"comments": "3", "likes": "98", "code": "xyz999", "url": "https://instagram.com/mock2"},
            ],
        }
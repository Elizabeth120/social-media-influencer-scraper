thonpython
import json
import logging
from pathlib import Path
from extractors.tiktok_parser import TikTokParser
from extractors.instagram_parser import InstagramParser
from extractors.youtube_parser import YouTubeParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def load_keywords(input_path: str):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load inputs: {e}")
        return []

def main():
    base = Path(__file__).resolve().parent.parent
    input_file = base / "data" / "inputs.sample.json"
    output_file = base / "data" / "sample_output.json"

    keywords = load_keywords(str(input_file))
    results = []

    tik = TikTokParser()
    ig = InstagramParser()
    yt = YouTubeParser()

    for kw in keywords:
        logging.info(f"Processing keyword: {kw}")

        results.extend([
            tik.search(kw),
            ig.search(kw),
            yt.search(kw),
        ])

    Exporter.export_json(results, str(output_file))
    logging.info(f"Exported results to {output_file}")

if __name__ == "__main__":
    main()
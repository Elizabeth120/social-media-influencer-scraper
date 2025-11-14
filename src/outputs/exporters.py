thonpython
import json
import logging

class Exporter:
    @staticmethod
    def export_json(data, output_path: str):
        try:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logging.info("JSON export successful.")
        except Exception as e:
            logging.error(f"Failed to export JSON: {e}")
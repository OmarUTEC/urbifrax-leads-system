import json
import os
from typing import List, Dict


def _data_file_path() -> str:
	base = os.path.dirname(__file__)
	return os.path.join(base, "data", "leads.json")


def ensure_data_dir() -> None:
	path = os.path.join(os.path.dirname(__file__), "data")
	os.makedirs(path, exist_ok=True)
	file = _data_file_path()
	if not os.path.exists(file):
		with open(file, "w", encoding="utf-8") as f:
			json.dump([], f, ensure_ascii=False, indent=2)


def load_leads() -> List[Dict]:
	ensure_data_dir()
	try:
		with open(_data_file_path(), "r", encoding="utf-8") as f:
			return json.load(f)
	except (json.JSONDecodeError, FileNotFoundError):
		return []


def save_leads(leads: List[Dict]) -> None:
	ensure_data_dir()
	with open(_data_file_path(), "w", encoding="utf-8") as f:
		json.dump(leads, f, ensure_ascii=False, indent=2)

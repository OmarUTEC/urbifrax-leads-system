from typing import Dict, List, Optional
from datetime import datetime

from storage import load_leads, save_leads


def _now_iso() -> str:
	return datetime.utcnow().isoformat() + "Z"


def add_lead(lead: Dict) -> Dict:
	leads = load_leads()
	lead = lead.copy()
	# asignar un unico id
	max_id = max((l.get("id", 0) for l in leads), default=0)
	lead.setdefault("id", max_id + 1)
	lead.setdefault("created_at", _now_iso())
	leads.append(lead)
	save_leads(leads)
	return lead


def get_all_leads() -> List[Dict]:
	return load_leads()


def filter_by_state(state: str) -> List[Dict]:
	return [l for l in load_leads() if l.get("estado") == state]


def filter_by_origin(origin: str) -> List[Dict]:
	return [l for l in load_leads() if l.get("origen") == origin]


def find_by_name(name: str) -> List[Dict]:
	name_l = name.strip().lower()
	return [l for l in load_leads() if name_l in l.get("nombre", "").lower()]


def find_by_phone(phone: str) -> Optional[Dict]:
	phone_s = phone.strip()
	for l in load_leads():
		if l.get("telefono") == phone_s:
			return l
	return None

from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    data = read(path)
    result = []
    for industries in data:
        if industries["industry"] not in result:
            if industries["industry"] != "":
                result.append(industries["industry"])
    return result


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    result = []
    for industries in jobs:
        if industries["industry"] == industry:
            result.append(industries)
    return result

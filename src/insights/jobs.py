from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding="utf-8") as csv_file:
            jobs_data = csv.DictReader(csv_file, delimiter=",", quotechar='"')
            return [jobs for jobs in jobs_data]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")


def get_unique_job_types(path: str) -> List[str]:
    data = read(path)
    result = []
    for jobs in data:
        if jobs["job_type"] not in result:
            if jobs["job_type"] != "":
                result.append(jobs["job_type"])
    return result


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    result = []
    for job in jobs:
        if job["job_type"] == job_type:
            result.append(job)
    return result

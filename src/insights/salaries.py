from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    data = read(path)
    return max(
        [
            int(salary["max_salary"])
            for salary in data
            if (salary["max_salary"]).isdigit()
        ]
    )


def get_min_salary(path: str) -> int:
    data = read(path)
    return min(
        [
            int(salary["min_salary"])
            for salary in data
            if (salary["min_salary"]).isdigit()
        ]
    )


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if "max_salary" not in job or "min_salary" not in job:
        # verificar se as chaves existem no dict
        raise ValueError("Error")
    elif type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        # verifica os valores das chaves sao inteiros
        raise ValueError("Error")
    elif int(job["min_salary"]) > int(job["max_salary"]):
        # verifica se os valores das chaves satisfazem a condição
        raise ValueError("Error")
    elif int(job["min_salary"]) <= float(salary) <= int(job["max_salary"]):
        # verifica se o valor está entre min e max
        return True
    else:
        return False


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    result = []
    try:
        for job in jobs:
            if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
                result.append(job)
        raise ValueError("Error")
    finally:
        return result

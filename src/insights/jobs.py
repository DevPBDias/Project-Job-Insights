from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    # Referencia: https://docs.python.org/3/library/csv.html
    try:
        # leitura do csv passando como parametro
        with open(path, encoding='utf-8') as csvfile:
            # salvando numa variavel já no formato de dicionario
            jobs_data = csv.DictReader(csvfile, delimiter=',', quotechar='"')
            # criando uma lista para receber os dicts e salvando numa variavel
            jobs_list = []
            # fazendo um loop passando por todos os dicts
            #  e dar um 'push' na lista para cada um
            for row in jobs_data:
                jobs_list.append(row)
                # print(jobs_list)
            return jobs_list
    except FileNotFoundError:
        # Referencia: https://docs.python.org/3/library/exceptions.html
        raise FileNotFoundError(f'File not found: {path}')


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    raise NotImplementedError


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError

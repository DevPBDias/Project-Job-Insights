from src.pre_built.sorting import sort_by

# sort_by(jobs: List[Dict], criteria: str)

jobs = [
    {
        "job": "Dev",
        "date_posted": "2022-12-12",
        "max_salary": 5000,
        "min_salary": 3500,
    },
    {
        "job": "Eng",
        "date_posted": "2022-12-11",
        "max_salary": 8000,
        "min_salary": 2500,
    },
]


def min_sort():
    sort_by(jobs, "min_salary")
    return jobs


def max_sort():
    sort_by(jobs, "max_salary")
    return jobs


def date_sort():
    sort_by(jobs, "date_posted")
    return jobs


def test_sort_by_criteria():
    max = max_sort()
    assert max == [
        {
            "job": "Eng",
            "date_posted": "2022-12-11",
            "max_salary": 8000,
            "min_salary": 2500,
        },
        {
            "job": "Dev",
            "date_posted": "2022-12-12",
            "max_salary": 5000,
            "min_salary": 3500,
        },
    ]

    min = min_sort()
    assert min == [
        {
            "job": "Eng",
            "date_posted": "2022-12-11",
            "max_salary": 8000,
            "min_salary": 2500,
        },
        {
            "job": "Dev",
            "date_posted": "2022-12-12",
            "max_salary": 5000,
            "min_salary": 3500,
        },
    ]

    date = date_sort()
    assert date == [
        {
            "job": "Dev",
            "date_posted": "2022-12-12",
            "max_salary": 5000,
            "min_salary": 3500,
        },
        {
            "job": "Eng",
            "date_posted": "2022-12-11",
            "max_salary": 8000,
            "min_salary": 2500,
        },
    ]

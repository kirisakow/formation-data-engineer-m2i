EMPLOYEES = [{'name': 'Max', 'age': 17},
            {'name': 'Sepp', 'age': 18},
            {'name': 'Nina', 'age': 15},
            {'name': 'Mike', 'age': 51}]

def employee_report(db_employees: list=None, *,
                    min_age: int=None,
                    sort_by: str=None,
                    sort_desc: bool=False,
                    uppercase: bool=False) -> list:
    ret = db_employees
    if min_age is not None:
        ret = [e for e in db_employees if e['age'] >= min_age]
    if sort_by is not None:
        ret = sorted(db_employees, key=lambda x: x[sort_by].lower(), reverse=sort_desc)
    if uppercase:
        ret = [e['name'].upper() for e in ret]
    return ret

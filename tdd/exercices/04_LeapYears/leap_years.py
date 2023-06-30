def is_leap_year(annee: int) -> bool:
    if annee < 1582:
        is_bissextile = False
    else:
        is_bissextile = annee % 400 == 0 \
            or (
                annee % 4 == 0
                and annee % 100 != 0
            )
    return is_bissextile

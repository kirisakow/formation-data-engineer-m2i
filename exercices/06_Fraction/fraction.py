from fractions import Fraction


def parse_fraction(operation: str = None, *,
                    require_same_denominator: bool=False) -> str:
    if operation is None:
        return None
    if ' ' not in operation:
        result_frac = Fraction(operation)
        if result_frac.numerator % result_frac.denominator == 0:
            return str(int(result_frac))
        return str(result_frac)
    frac1, operator, frac2 = operation.split(' ')
    frac1, frac2 = Fraction(frac1), Fraction(frac2)
    if require_same_denominator \
        and int(frac1.denominator) != int(frac2.denominator):
        raise ValueError('Les dénominateurs doivent être identiques.')
    if operator in '+-*/' and len(list(operator)) == 1:
        ops = {
            '+': lambda frac1, frac2: Fraction(frac1 + frac2),
            '-': lambda frac1, frac2: Fraction(frac1 - frac2),
            '*': lambda frac1, frac2: Fraction(frac1 * frac2),
            '/': lambda frac1, frac2: Fraction(frac1 / frac2),
        }
        result_frac = ops[operator](frac1, frac2)
        if result_frac.numerator % result_frac.denominator == 0:
            return str(int(result_frac))
        return str(result_frac)

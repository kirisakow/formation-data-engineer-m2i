from math import sqrt


class PrimeFactors:

    @staticmethod
    def factors_of(n: int) -> list:
        if PrimeFactors.is_prime(n):
            return [n]
        factors = []
        smallest_prime_factor = 2
        while n > 1:
            if n % smallest_prime_factor == 0:
                factors.append(smallest_prime_factor)
                n /= smallest_prime_factor
            else:
                smallest_prime_factor += 1
        return factors

    @staticmethod
    def is_prime(n: int) -> bool:
        if n == 0 or n == 1:
            return False
        if n == 2:
            return True
        for possible_factor in range(2, int(sqrt(n)) + 1):
            if n % possible_factor == 0:
                return False
        return True

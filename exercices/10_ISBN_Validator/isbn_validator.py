import re


class IsbnValidator:
    @staticmethod
    def verifier_isbn(isbn: str) -> bool:
        total = 0
        pattern_du_préfixe_isbn = r'^978-'
        isbn = re.sub(pattern_du_préfixe_isbn, '', isbn)
        isbn = isbn.replace('-', '')
        longueur_valide = 10
        if len(isbn) != longueur_valide:
            raise ValueError('Longueur incorrecte du numéro ISBN')
        pattern_caractères_valides = r'[0-9X]+'
        if re.fullmatch(pattern_caractères_valides, isbn) is None:
            raise ValueError('Caractères invalides dans le numéro ISBN')
        for i, char in enumerate(isbn):
            if char == 'X':
                char = '10'
            total += int(char) * (10 - i)
        return total % 11 == 0

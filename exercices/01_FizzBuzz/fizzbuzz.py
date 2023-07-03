def fizzbuzz(n: int) -> int | str:
    ret = ''
    if n % 3 == 0:
        ret += 'Fizz'
    if n % 5 == 0:
        ret += 'Buzz'
    if ret != '':
        return ret
    else:
        return str(n)

def ordinal(number: int):
    return str("%d%s" % (number, "tsnrhtdd"[number % 5 * (number % 100 ^ 15 > 4 > number % 10)::4]))
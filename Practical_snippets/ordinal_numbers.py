def ordinal(number: int):
    k = number % 10
    return str("%d%s" % (number, "tsnrhtdd"[(number / 10 % 10 != 1) * (k < 4) * k::4]))
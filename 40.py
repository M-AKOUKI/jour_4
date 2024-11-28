def pair_impair(n):
    assert n>0, "uniquement nombre positif"
    int(n)
    if n%2 == 0:
        return "pair"
    else:
        return "impair"

print(pair_impair(5))
print(pair_impair(4))
print(pair_impair(-7))
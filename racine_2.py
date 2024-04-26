# trying to approach 1,414 213 562 373 095 048 801 68
import decimal

TWO = decimal.Decimal(2)
ONE = decimal.Decimal(1)


def decimal_expansion(depth: int) -> object:
    depth -= 1
    if depth == 0:
        return 2
    return TWO + (ONE / decimal_expansion(depth))


def uncaped_decimal_expansion(depth: int) -> object:
    denominator1 = decimal.Decimal("2.5")  # initialization
    while depth != 0:
        depth -= 1
        denominator2 = TWO + (ONE / denominator1)
        denominator1 = denominator2
    return denominator2 - ONE


depth = input("Depth : ")

try:
    depth = int(depth)
    if depth < 1:
        raise ValueError
except ValueError as e:
    print("La profondeur est un nombre entier plus grand que 1.")
else:

    decimal.getcontext().prec = depth  #  sets maximum decimal values

    if __name__ == "__main__":
        try:
            root_of_two = decimal_expansion(depth) - 1  # [1,2,2,2,...]
            root_of_two_uncaped = uncaped_decimal_expansion(depth)
            print(root_of_two)
            print(root_of_two_uncaped)
        except Exception as error:
            print(error)

# trying to approach 1,414 213 562 373 095 048 801 68
import decimal


def decimal_expansion(depth):
    depth -= 1
    if depth == 0:
        return 2
    return decimal.Decimal(2) + (decimal.Decimal(1) / decimal_expansion(depth))


depth = input("Depth : ")
try:
    depth = int(depth)
    if depth < 1:
        raise ValueError
except ValueError as e:
    print("La profondeur est un nombre plus grand que 1.")

else:
    try:
        decimal.getcontext().prec = depth  #  sets maximum decimal values
        root_of_two = decimal_expansion(depth) - 1  # [1,2,2,2,...]
        print(root_of_two)
    except Exception as error:
        print(error)

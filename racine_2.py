import decimal
from time import time


TWO = decimal.Decimal(2)
ONE = decimal.Decimal(1)
GOAL = "1.41421356237309504880168872420969807856967187537694807317667973799073247846210703885038753432764157"
LEN_GOAL = 100


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
            print("[WHILE FUNC]")
            t1 = time()
            root_of_two_uncaped = str(uncaped_decimal_expansion(depth))
            print(f"code took {time()-t1}")
            print(root_of_two_uncaped)
            for index in range(LEN_GOAL):
                if root_of_two_uncaped[index] != GOAL[index]:
                    print(
                        f"\ndifférences à partir de la {index-2} décimale. (par rapport à la référence)"
                    )
                    break
            else:
                print("\n pas de différences de décimales par rapport à la référence.")

            if depth < 999:  #  maximum recursion depth in python.
                print("\n", "*" * 20, "\n")
                print("[RECURSIVE FUNC]")
                t1 = time()
                root_of_two = str(decimal_expansion(depth) - 1)  # [1,2,2,2,...]
                print(f"code took {time()-t1}")
                print(root_of_two)
                for index in range(LEN_GOAL):
                    if root_of_two[index] != GOAL[index]:
                        print(
                            f"\nchangement à partir de la {index-2} décimale. (par rapport à la référence)"
                        )
                        break
                else:
                    print(
                        "\npas de différences de décimales par rapport à la référence."
                    )

        except Exception as error:
            print(error)

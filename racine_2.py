# trying to approach 1,414 213 562 373 095 048 801 68 
def decimal_expansion(depth):
	depth -= 1
	if depth == 0:
		return 2
	return 2 + (1/decimal_expansion(depth))
depth = input("Depth : ")
try: 
	depth = int(depth)
	if depth < 1: 
		print("La profondeur est supérieure à 1.")
	else:
		root_of_two = decimal_expansion(depth) - 1 # [1,2,2,2,...]
		print(root_of_two)
except: 
	print("La profondeur est un nombre.")
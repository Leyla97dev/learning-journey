weight = int(input("weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lb is " + str(converted))
else:
    converted = weight * 0.45
    print("weight in kg is " + str(converted))
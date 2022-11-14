first = float(raw_input("First: "))
func = raw_input("+, -, *, or, / ")
second = float(raw_input("Second: "))
sum = first + second
dif = first - second
mul = first * second
div = first / second
if func == "+":
    print("Sum :" + str(sum))
if func == "-":
    print("Difference :" + str(dif))
if func == "*":
    print("Product :" + str(mul))
if func == "/":
    print("Quotient :" + str(div))


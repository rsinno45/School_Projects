Age = float(input("How old are you?: "))

if Age <= 1:
    print("You are an infant")

if 1 < Age < 13:
    print("You are a child")

if 13 <= Age < 20:
    print("You are a teenager")

if Age >= 20:
    print("You are an adult")
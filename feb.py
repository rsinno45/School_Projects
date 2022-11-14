Year = float(input("Year: "))

if Year % 100 == 0:
    if Year % 400 == 0:
        print("29 Days")
    else:
        print("28 Days")
else:
    if Year % 4 == 0:
        print("29 days")
    else:
        print("28 days")
# Problem statement 2
month = int(input("Enter month: "))

if month < 1 or month > 12:
    print("Invalid Month Entered")

elif month >= 3 and month <= 5:
    print("Season: Spring")

elif month >= 6 and month <= 8:
    print("Season: Summer")

elif month >= 9 and month <= 11:
    print("Season: Autumn")

else:
    print("Season: Winter")
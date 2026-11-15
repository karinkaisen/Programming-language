
year = int(input("Enter your year: "))

if year % 400 == 0:
    print("Is leap year")

elif year % 100 == 0:
    print("No leap year ")

elif year % 4 == 0:
    print("Is leap year")

else:
    print("No leap year")

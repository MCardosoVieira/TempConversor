ask = input("Would you like to use Celsius, Fahrenheit or Kelvins? (use c/f/k): ")

if ask == "c":

    c = float(input("Type your temperature (Celsius): "))
    f = float((c * 9 / 5) + 32)
    k = float((c + 273.15))

    print("----------------------------------------------")
    print("The temperatures are: ")
    print(f"{c:.2f}°C / {k:.2f}°K / {f:.2f}°F")
    print("----------------------------------------------")

elif ask == "f":

    f = float(input("Type your temperature (Fahrenheit): "))
    c = float((f - 32) / 1.8)
    k = float((f - 32)/1.8 + 273.15)

    print("----------------------------------------------")
    print("The temperatures are: ")
    print(f"{c:.2f}°C / {k:.2f}°K / {f:.2f}°F")
    print("----------------------------------------------")

elif ask == "k":

    k = float(input("Type your temperature (Kelvin): "))
    c = float(k - 273.15)
    f = float(k * 1.8 - 459.67)

    print("----------------------------------------------")
    print("The temperatures are: ")
    print(f"{c:.2f}°C / {k:.2f}°K / {f:.2f}°F")
    print("----------------------------------------------")
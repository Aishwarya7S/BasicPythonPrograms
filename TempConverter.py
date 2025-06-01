def convert_temperature():
    print("Temperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    choice = input("Choose an option (1 or 2): ")
    print()
    
    if choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius:.2f}°C is equal to {fahrenheit:.2f}°F.")
    elif choice == "2":        
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit:.2f}°F is equal to {celsius:.2f}°C.")
    else:
        print("Invalid choice! Please enter 1 or 2.")
convert_temperature()

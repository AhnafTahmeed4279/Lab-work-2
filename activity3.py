print("Smartphone Super Charging Safety Check")
battery_temperature=float(input("Enter the battery temperature in Celsius: "))
charge_percentage=int(input("Enter the current charge percentage: "))
if battery_temperature<45.5 and charge_percentage<80:
    print("Switch to Safe Slow Charge")
else:
    print("Continue Fast Charging")
# Def listings
def wind_chill(temp, wind_speed):
    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (wind_speed**0.16)) + (0.4275 * temp * (wind_speed**0.16))
    return wind_chill

def celsius_from_fahrenheit(fahrenheit):
    if temp_unit == 'C':
        return temp
    else:
        return (temp - 32) * 5/9

# Questions & Prompts
temp = float(input("Enter the Temperature: "))
temp_unit = input("Enter the Temperature unit C/F: ").upper()

# Unit check
if temp_unit == "C":
    temp = celsius_from_fahrenheit(temp)

# Chilly Day Data
print(f"\nWind Chill Values: At {temp} °{temp_unit}")
print("-----------------------------------")

# ANSI escape sequences for text color
RED = "\033[91m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RESET = "\033[0m"

for wind_speed in range(5, 61, 5):
    chill = wind_chill(temp, wind_speed)
    if 33 <= temp <= 69:
        color = YELLOW
    elif chill > 32:
        color = RED
    else:
        color = BLUE
    print(f"At {wind_speed} mph: -It feels like {color}{chill:.2f} °{temp_unit}{RESET}")

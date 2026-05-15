# Constants
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5
OFFSET = 32

# User input
celsius_input = 20
fahrenheit_input = 85

# Conversions
converted_to_f = (celsius_input * CELSIUS_TO_FAHRENHEIT) + OFFSET
converted_to_c = (fahrenheit_input - OFFSET) * FAHRENHEIT_TO_CELSIUS

# Display
print(f'{celsius_input}°C -> {converted_to_f:.1f}°F')
print(f'{fahrenheit_input}°F -> {converted_to_c:.1f}°C')

# HOMEWORK:
# Your homework is to create a miles-to-kilometers converter in Python!
#
# The script should:
# - Allow the user to convert from kilometers to miles and vice versa.
# - Display the formatted result in the console using f-strings.
#
# Remember, the homework is optional—but doing it will help you
# learn Python much faster than just watching me code.

#Homework
# Contants
MILES_TO_KM = 1.60934
KM_TO_MILES = 1 / 1.60934

# User input
miles_input = 26.2
km_input = 100

# Conversions
converted_to_km = miles_input * MILES_TO_KM
converted_to_miles = km_input * KM_TO_MILES

# Display
print(f'{miles_input}mi -> {converted_to_km:.1f}km')
print(f'{km_input}km -> {converted_to_miles:.1f}mi')

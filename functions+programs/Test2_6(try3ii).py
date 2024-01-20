def kelvin_to_fahrenheit(kelvin):
        assert kelvin>=0#,"Temperature in Kelvin cannot be negative"
        fahrenheit=(kelvin-273.15)*(9/5)+32
        return fahrenheit
    
try:
    temp_in_kelvin=float(input("Enter temp in Kelvin:"))
    converted_temp=kelvin_to_fahrenheit(temp_in_kelvin)
    print(f"{temp_in_kelvin} Kelvin is {converted_temp} Fahrenheit.")
except ValueError:
    print("Invalid input.Please enter valid number for temperature.")
#except AssertionError as e:
#    print(e)

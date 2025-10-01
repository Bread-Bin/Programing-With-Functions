import time

#math set up
min_life = float("inf")
max_life = -float("inf")
country_min = ""
country_max = ""
total_life = 0
count = 0



#introduction:
print('''Welcome to the Data Sorter 3,000!
Life Exceptency of world countries from the years 1543 - 2019
''')

#User Entry
time.sleep(3)
while True:
    print("Enter a year to find the average life expectancy")
    try:
        question = int(input(" Input a year:"))
        if len(str(question)) != 4:
            print("\nInvalid input. Please enter a four-digit number.")
            continue
        break
    except ValueError:
        print("Bad")

#open and read loop
with open("life-expectancy.csv") as file:
    next(file) #skip header
    for line in file:
        country, code, year, life = line.strip().split(",")
        life = float(life)

        if life < min_life:
            min_life = life
            country_min = line.strip()

        elif life > max_life:
            max_life = life
            country_max = line.strip()

        if year == str(question):
            total_life += life
            count += 1
        


#Average Life Expectancy
if count > 0:
    average_life = total_life / count
    print(f"\nFor the year {question}:")
    print(f"The average life expectancy across all countries was {average_life:.2f}")
    print(f"The max life expectancy was in {country_max.split(',')[0]} with {max_life:.3f}")
    print(f"The min life expectancy was in {country_min.split(',')[0]} with {min_life:.3f}")
else:
    print(f"No data available for the year {question}.")


#Overall Data Prompt
while True:
    show_data = input("\nWould you like to see the country with the lowest and highest life expectancies? (yes/no): ")
    if show_data.lower() == "yes":
        #Overall Data
        print("\nCountry with the lowest life expectancy:")
        country_min_values = country_min.split(",")
        print(f'''-----------------------------------------
        {country_min_values[0]}
        Code: {country_min_values[1]}
        Year: {country_min_values[2]}
        Life Expectancy: {country_min_values[3]}''')

        print("\nCountry with the highest life expectancy:")
        country_max_values = country_max.split(",")
        print(f'''-----------------------------------------
        {country_max_values[0]}
        Code: {country_max_values[1]}
        Year: {country_max_values[2]}
        Life Expectancy: {country_max_values[3]}''')
        break
    elif show_data.lower() == "no":
        break
    else:
         print("Invalid input. Please enter 'yes' or 'no'.")

#Single Country Data
while True:
    show_country_data = input("\nWould you like to see the data for a specific country? (yes/no): ")
    if show_country_data.lower() == "yes":
        country_name = input("Enter the name of the country: ")
        country_found = False

        with open("life-expectancy.csv") as file:
            next(file)  # Skip header
            for line in file:
                country, code, year, life = line.strip().split(",")
                life = float(life)

                if country.lower() == country_name.lower():
                    print(f"\nData for {country}:")
                    print(f"Code: {code}")
                    print(f"Year: {year}")
                    print(f"Life Expectancy: {life:.3f}")
                    country_found = True

        if not country_found:
            print(f"No data available for {country_name}.")
    elif show_country_data.lower() == "no":
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
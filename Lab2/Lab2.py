# Function to display the main menu
def display_main_menu():
    print("display_main_menu")

# Function to input temperature values from the user
def input_temperatures():
    print("input_temperatures")

# Function to calculate the average temperature
def calc_average(temperatures):
    print("calc_average")

# Function to find the minimum temperature
def find_minimum(temperatures):
    print("find_minimum")

# Function to find the maximum temperature
def find_maximum(temperatures):
    print("find_maximum")

# Main function to run the program
def main():
    temperatures = []  # Create an empty list to store temperature values

    display_main_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            input_temperatures()
        elif choice == '2':
            calc_average(temperatures)
        elif choice == '3':
            find_minimum(temperatures)
        elif choice == '4':
            find_maximum(temperatures)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    input_string = input("Enter numbers separated by commas: ")
    input_list = input_string.split(',')
    numeric_list = []

    for item in input_list:
        try:
            numeric_list.append(float(item))
        except ValueError:
            print(f"Warning: '{item}' is not a valid numeric value and will be ignored.")

    return numeric_list


if __name__ == "__main__":
    display_main_menu()
    user_input = get_user_input()
    print("User Input List:", user_input)

def calc_average_temperature(temperature_list):
    if len(temperature_list) == 0:
        return 0.0  # Return 0 if the list is empty to avoid division by zero

    total = sum(temperature_list)
    average = total / len(temperature_list)
    return average

def calc_min_max_temperature(temperature_list):
    if len(temperature_list) == 0:
        return [0, 0]  # Return [0, 0] if the list is empty

    minimum = min(temperature_list)
    maximum = max(temperature_list)
    return [minimum, maximum]


if __name__ == "__main__":
    # Assume you have a list of temperature readings (e.g., [25.5, 30.2, 22.1, 27.8, 19.0])
    temperature_readings = [25.5, 30.2, 22.1, 27.8, 19.0]

    average_temp = calc_average_temperature(temperature_readings)
    min_max_temp = calc_min_max_temperature(temperature_readings)

    print("Average Temperature:", average_temp)
    print("Minimum Temperature:", min_max_temp[0])
    print("Maximum Temperature:", min_max_temp[1])


    def calc_median_temperature(temperature_list):
        # Sort the temperature list in ascending order
        sorted_temperatures = sorted(temperature_list)

        # Calculate the length of the sorted list
        n = len(sorted_temperatures)

        # Calculate the median based on the number of elements in the list
        if n % 2 == 1:
            # If the number of elements is odd, return the middle value
            median = sorted_temperatures[n // 2]
        else:
            # If the number of elements is even, return the average of the two middle values
            middle1 = sorted_temperatures[n // 2 - 1]
            middle2 = sorted_temperatures[n // 2]
            median = (middle1 + middle2) / 2.0

        return median



    if __name__ == "__main__":
        # Assume you have a list of temperature readings (e.g., [25.5, 30.2, 22.1, 27.8, 19.0])
        temperature_readings = [25.5, 30.2, 22.1, 27.8, 19.0]

        median_temp = calc_median_temperature(temperature_readings)
        print("Median Temperature:", median_temp)


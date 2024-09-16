"""
nyc_weather.csv contains new york city weather for first few days in the month of January.
Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem


"""

date_list = []


def register_data():
    with open("nyc_weather.csv", "r") as f:
        for lines in f:
            date, temp = lines.split(",")
            temp = temp.strip()  # Remove any trailing newline characters
            if date.lower() != "date":  # Skip the header line
                month, day = date.split()  # Split date into month and day
                date_list.append(
                    (month, int(day), int(temp))
                )  # Append as (month, day, temperature)


def check_avg(my_list):
    avg_temp = 0

    for _, date, temp in my_list:
        if date <= 7:
            avg_temp += temp
    return avg_temp / len(my_list)


def find_max_temp(my_list):
    max_temp = 0
    for i in range(10):
        for _, date, temp in my_list:
            if temp >= max_temp:
                max_temp = temp
    return max_temp


register_data()
check_avg(date_list)
find_max_temp(date_list)

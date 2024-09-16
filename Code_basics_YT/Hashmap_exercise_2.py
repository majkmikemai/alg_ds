"""
nyc_weather.csv contains new york city weather for first few days in the month of January.
Write a program that can answer following,
What was the average temperature in first week of Jan
What was the maximum temperature in first 10 days of Jan
Figure out data structure that is best for this problem


"""

dates = {}


def register_data():
    with open("nyc_weather.csv", "r") as f:
        for lines in f:
            date, temp = lines.split(",")
            temp = temp.strip()  # Remove any trailing newline characters
            if date.lower() != "date":  # Skip the header line
                # month, day = date.split()  # Split date into month and day
                dates[date] = int(temp)  # Append as (month, day, temperature)


register_data()
dates["Jan 9"]
dates["Jan 4"]

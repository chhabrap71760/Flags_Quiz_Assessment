import csv
import random

with open('country_flags.csv', newline='') as f:
    reader = csv.reader(f)
    flag_list = list(reader)

#print(flag_list)

for item in range(0,4):
    chosen_country = random.choice(flag_list)
    country_name = []

    country_name = chosen_country[0]
    country_flag = chosen_country[-1]

    print("country name: ", country_name)
    print("country flag: ", country_flag)

for row in flag_list:
    country_list[row[0]]

print(country_list)

    input()

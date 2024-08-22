'''
Pre Requisites:

NOTES :
#csv are comma separated values i.e. spreadsheets in comma sep. format
#opening weather_data.csv here
with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
🤦‍♀️Since, this becomes lil grinding so w implement csv module

import csv
temperatures = []

with open("./weather_data.csv") as data_file:
    data = csv.reader(data_file)
    #print(data)
    for row in data:
        if row[1]!="temp":
            temperatures.append(row[1])
    print(temperatures)


# now for more complex data, this too becomes strenous.. .here,comes PANDAS


import pandas
data = pandas.read_csv("weather_data.csv")
#print(type(data))  # dataframe is cell in excel/speadsheets
#print(type(data["temp"])) # series is like a list i.e a column
data_dict = data.to_dict()
#print(data_dict)
temp_list = data["temp"].to_list()
# length = len(temp_list)

# to calc avg i.e. mean
# traditional way:
#avg = int(sum(temp_list)/7)
#print(avg)

#pandas way:
# print(f"Mean: {data["temp"].mean()}")

#max in pandas
# print(f"Max temp: {data["temp"].max()}")
# Get data in columns:
# print(data["condition"])
# same o/p as above :
# Using like an object--> print(data.condition)

#prints row with specified  condition
#print(data[data.day == "Monday"])
# prints row with max temp
#print(data[data.temp == data.temp.max()])

#CALCULATING MONDAY'S TEMP IN FAHRENHEIT
monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
temp = monday_temp * 9/5 + 32
print(temp)


#Create a dataframe fom scratch

data_dict = {
    "students": ["Amy","James","Angela"],
    "scores": [76,56,65]
}
# Convert data_dict into pandas dataframe
data= pandas.DataFrame(data_dict)
# print(data)
# data= pandas.DataFrame(data_dict)
# Convert data into csv file
data.to_csv("new_data.csv")


'''
import pandas
data = pandas.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color":["Gray","Cinnamon","Black"],
    "Count":[grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count")
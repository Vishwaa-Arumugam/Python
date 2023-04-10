import csv
import pandas

with open("weather_data.csv") as data:
    d = csv.reader(data)
    tempertatures =[]

    for row in d:
        if row[1] != "temp":
            tempertatures.append(int(row[1]))
    print(tempertatures)


data = pandas.read_csv("weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print("AVERAGE : ", round(sum(temp_list)/len(temp_list)))

print(data["temp"].mean())

print(data["temp"].max())


#get data in columns
print(data["condition"])
print(data.condition)

# get row in data
print(data[data.day == "Monday"])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# mon_t_f = monday_temp * 9/5 + 32
# print(mon_t_f)

# data_dict = {
#         "studenta": ["Amy","James","Angela"],
#         "scores": [76,56,65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("nwpark.csv")
gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
print(gray)
print(red)
print(black)

data_dict = {
        "Fur color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray, red, black]
}

pandas.DataFrame(data_dict).to_csv("squrriel_count.csv")



















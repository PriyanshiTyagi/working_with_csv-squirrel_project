# # import csv
# #
# # with open("./weather_data.csv") as data_file:
# #     next(data_file)
# #     data = csv.reader(data_file)
# #
# #     temperature = []
# #     for rows in data:
# #
# #         temperature.append(int(rows[1]))
# #     print(temperature)
# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# # print(data["temp"])
# # data_dict=data.to_dict()
# # print(data_dict)
#
# # temp_list=data["temp"].to_list()
# # avg=sum(temp_list)/len(temp_list)
# # print(data["temp"].max())
# # printing a row
# # print(data[data.day=="Monday"])
#
# # printing which row has maximum temp
#
# # print(data[data.temp == data["temp"].max()])
#
# monday =data [data.day == "Monday"]
# print((monday.temp*1.8)+32)
import pandas as pd

data = pd.read_csv("Squirrel_Data.csv")
list_of_fur = data.PrimaryFurColor
black_fur = 0
gray_fur = 0
cinnamon_fur = 0
for furs in list_of_fur:
    if furs == "Black":
        black_fur += 1
    if furs == "Gray":
        gray_fur += 1
    if furs == "Cinnamon":
        cinnamon_fur += 1
new_data = {
    "FurColor": ["Black", "Gray", "Cinnamon"],
    "Count": [black_fur, gray_fur, cinnamon_fur]
}

new_data=pd.DataFrame(new_data)
new_data.to_csv("fur_color_count")

# new_data={
#     "Fur Color":[]
# }

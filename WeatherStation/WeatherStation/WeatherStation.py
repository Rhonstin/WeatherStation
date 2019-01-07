import csv,pygal
from statistics import mean 
filename = "history_export_2019-01-07T13_28_28.csv"
data = []

temp_24 = []
temp = []
i=0
line = pygal.Bar(x_label_rotation=20,rounded_bars=20)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        data.append(row[2])
        temp.append(float(row[5]))


for index,column_header in enumerate(header_row):
    print(index, column_header)


while i != len(temp):
    mean_temp = mean(temp[i:i+24])
    i += 24
    temp_24.append(round(mean_temp))

data_8 = data[::24]
line.x_labels = data_8
line.title = "Погода за последние 7 дней "
line.add("temp", temp_24)
line.render_to_file('chart.svg')
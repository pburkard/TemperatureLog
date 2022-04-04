import matplotlib.pyplot as plt
import datetime
from os.path import exists

date_format = '%d-%m-%Y'
data_file_name = f"temperature_{datetime.date.today().strftime(date_format)}"


measurements_raw: list[list[str]] = []

filenames = []
for x in range(0,8):
    date = datetime.date.today() - datetime.timedelta(x)
    filenames.append(date.strftime(date_format))

for filename in filenames:
    data_file_path = rf"data/{filename}.txt"
    if not exists(data_file_path):
        print(f"no data for {filename}")
        continue
    print(f"read data for {filename}")
    filestream = open(data_file_path, "r")
    measurements_raw.append(filestream.read().splitlines())
    filestream.close()

fig = plt.figure()
colors = ['b','r','g','c','m','y','k']
for n, measurement_day in enumerate(measurements_raw):
    axis_time: list[str] = []
    axis_temperature: list[float] = []
    for measurement in measurement_day:
        chunks = measurement.split(',')
        if len(chunks) == 2:
            axis_time.append(chunks[0])
            axis_temperature.append(float(chunks[1]))
    plt.plot(axis_time, axis_temperature, color=colors[n], label=filenames[n])
# xticks = axis_time[::4]
plt.legend()
plt.xticks(['0:0', '6:0', '12:0', '18:0'])
plt.autoscale(enable=True, axis='x', tight=True)
fig.savefig(f"figures/{datetime.datetime.today()}.jpg", dpi=150)
import os
import pandas as pd
from datetime import datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns
from dateutil.relativedelta import relativedelta

time_format ="%Y-%m-%d %H:%M:%S"

def cal_diff(filename, write = True):
    data = pd.read_csv(filename).drop(columns=['Unnamed: 0'])
    year_month = filename.split("_")[-1].split(".")[0]
    
    start_time = datetime.strptime(year_month, "%Y-%m")
    end_time = start_time + relativedelta(months = 1)

    # start_time = "2020-6-1 00:00:00"
    # end_time = "2020-6-2 00:00:00"

    # start_time = datetime.strptime(start_time, time_format)
    # end_time = datetime.strptime(end_time, time_format)

    data["tpep_pickup_datetime"] = pd.to_datetime(data["tpep_pickup_datetime"])
    data["tpep_dropoff_datetime"] = pd.to_datetime(data["tpep_dropoff_datetime"])

    res_times = []
    res_datas = []

    print("Calculating file %s ..." % filename)

    while start_time < end_time:
        # print(start_time)
        # res_times.append(datetime.strftime(start_time, time_format))
        res_times.append(start_time)
        
        tmp = start_time + timedelta(hours = 1)

        # 对每个小时进行统计
        res_data = np.zeros(265, dtype=np.int)

        pickup = data.loc[(data["tpep_pickup_datetime"] > start_time) & (data["tpep_pickup_datetime"] < tmp)]["PULocationID"]
        pickup.reset_index(drop=True, inplace=True)
        dropoff = data.loc[(data["tpep_dropoff_datetime"] > start_time) & (data["tpep_dropoff_datetime"] < tmp)]["DOLocationID"]
        dropoff.reset_index(drop=True, inplace=True)
        for i in range(pickup.shape[0]):
            res_data[pickup[i] - 1] -= 1
        for i in range(dropoff.shape[0]):
            res_data[dropoff[i] - 1] += 1
        
        res_datas.append(res_data)

        start_time = tmp

    res_times = pd.DataFrame(np.array(res_times)).rename(columns = {0: 'time'})
    res_datas = pd.DataFrame(np.array(res_datas))

    res = pd.concat([res_times, res_datas], axis = 1)
    if write:
        res.to_csv("data/diff/%s.csv" % (year_month), index=False)
    print("Done!")
    return res

res = cal_diff("data/clear_data/new_yellow_tripdata_2020-06.csv", write=False)

res_datas = res.iloc[:, 1:]
res_times = res.iloc[:, 0]

# print(res_times)
# print(res_datas)

# exit(0)

# 创建画布
sns.set_style("whitegrid")
fig = plt.figure(figsize=(15, 10))

plt.ion()

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

for i in range(res.shape[0]):

    plt_data = res_datas.loc[i]
    plt_data0 = plt_data.loc[(plt_data > 0) & (plt_data <= 20)]
    plt_data1 = plt_data.loc[(plt_data < 0) & (plt_data >= -20)]
    plt_data2 = plt_data.loc[plt_data > 20]
    plt_data3 = plt_data.loc[plt_data < -20]

    plt.cla()

    plt.xlabel('区域ID', fontsize=20)
    plt.ylabel('下车-上车', fontsize=20)
    plt.xlim([0, 264])
    plt.ylim([-20, 20])

    plt.title(datetime.strftime(res_times[i], time_format), fontsize=20)

    bar0 = plt.bar(x=plt_data0.index.values, height=plt_data0, color='r')
    bar1 = plt.bar(x=plt_data1.index.values, height=plt_data1, color='b')
    bar2 = plt.bar(x=plt_data2.index.values, height=plt_data2, color='orange')
    bar3 = plt.bar(x=plt_data3.index.values, height=plt_data3, color='purple')
    for a, b in zip(plt_data2.index.values, plt_data2):
        text0 = plt.text(a - 6, 18.5, '%.0f'%b, ha = 'center', va = 'bottom', fontsize=20, color='orange')
    for a, b in zip(plt_data3.index.values, plt_data3):
        text1 = plt.text(a - 6, -20, '%.0f'%b, ha = 'center', va = 'bottom', fontsize=20, color='purple')

    plt.pause(0.1)

plt.ioff()

plt.show()
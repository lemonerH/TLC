# 下一站去哪

---

## 概述

这个项目主要对纽约出租车一年半（2019-01到2020-06）的数据进行数据清洗，分析，可视化，建模等方面的操作

数据来源：

<https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page>

你也可以下载我们的数据:

> 百度云
链接：<https://pan.baidu.com/s/15rmppyfRO_De7Azz16qoPQ>
提取码：wzs6

> 交大云盘
链接：<https://jbox.sjtu.edu.cn/l/KnHCvM>

数据描述：

<https://www1.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf>

数据文件夹结构

需创建文件夹并将原始数据下载到data/raw

```shell
├─data/     # 保存数据
│  ├─clear/ # 清洗后数据集
│  ├─diff/  # 上下车差值
│  ├─dist/  # 区域间距离
│  ├─model/ # 模型
│  └─raw/   # 原始数据
├─graph/    # 保存图片
```

## 数据分析

对profiling（2020-06）得到的报告进行分析

|变量|含义|类型|待处理|
|:-|:-|:-|:-|
|VendorID|记录提供商|Categorical|缺省9.2%|
|tpep_pickup_datetime|上车时间|Datetime||
|tpep_dropoff_datetime|下车时间|Datetime||
|passenger_count|乘客数量|Categorical Number|缺省9.2%，零值2.4%|
|trip_distance|打车距离|Contiguous Number|零值3.2%，存在异常值(极大值)|
|RatecodeID|价格代码|Categorical Number|缺省9.2%|
|store_and_fwd_flag|是否保存在车辆内存中|Boolean|缺省9.2%|
|PULocationID|上车区域ID|Categorical Number||
|DOLocationID|下车区域ID|Categorical Number||
|payment_type|支付类别|Categorical Number|缺省9.2%|
|fare_amount|距离计价|Contiguous Number|存在异常值(负值，极大值)|
|extra|附加费|Contiguous Number|零值47.8%(正常)|
|mta_tax|交通税|Categorical Number|两类|
|tip_amount|小费|Contiguous Number|零值41.0%(正常)|
|tolls_amount|过路费|Contiguous Number|零值94.7%(正常)，存在异常值(极大值)|
|improvement_surcharge|改善附加费|Categorical Number|两类，存在异常值(负值)|
|total_amount|总费用|Contiguous Number|存在异常值(负值，极大值)|
|congestion_surcharge|拥挤附加费|Categorical Number|两类，存在异常值(负值)|

## 目录结构

```shell
│  .gitignore
│  README.md
│  纽约出租车.ipynb                             # 代码主notebook
│  
├─data                                         # 数据文件夹
│  ├─clear                                     # 清洗后数据集
│  │      new_yellow_tripdata_2019-01.csv
│  │      ...
│  │      new_yellow_tripdata_2020-06.csv
│  │      
│  ├─diff                                      # 上下车差值
│  │      2019-01.csv
│  │      ...
│  │      2020-06.csv
│  │      
│  ├─dist                                      # 区域间距离
│  │      2019-01.csv
│  │      ...
│  │      2020-06.csv
│  │      
│  ├─model                                     # 模型
│  │      diff.csv
│  │      dist.csv
│  │      graph.npy
│  │      
│  └─raw                                       # 原始数据
|         yellow_tripdata_2019-01.csv
|         ...
│         yellow_tripdata_2020-06.csv
│          
└─graph                                        # 图文件
        heatmap.html
        heatmap_all.html
        heatmap_diff.html
        predict.html
```

## 注意事项

* [x] 1. 项目数据集须在[TLC](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)上下载，本项目使用数据为`Yellow Taxi Trip Records`
* [x] 2. 项目运行前需在根目录下创建data等文件夹存放上述下载的数据

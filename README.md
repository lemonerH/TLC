# 下一站去哪

---

## 概述

这个项目主要对纽约出租车一年半（2019-01到2020-06）的数据进行数据清洗，分析，可视化，建模等方面的操作

数据来源：

<https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page>

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

# 下一站去哪

---

## 目录结构

```
│  .gitignore
│  README.md
│  纽约出租车.ipynb
│  
├─data
│  ├─clear
│  │      new_yellow_tripdata_2019-01.csv
│  │      ...
│  │      new_yellow_tripdata_2020-06.csv
│  │      
│  ├─diff
│  │      2019-01.csv
│  │      ...
│  │      2020-06.csv
│  │      
│  ├─dist
│  │      2019-01.csv
│  │      ...
│  │      2020-06.csv
│  │      
│  ├─model
│  │      diff.csv
│  │      dist.csv
│  │      graph.npy
│  │      
│  └─raw
|         yellow_tripdata_2019-01.csv
|         ...
│         yellow_tripdata_2020-06.csv
│          
└─graph
        heatmap.html
        heatmap_all.html
        heatmap_diff.html
        predict.html
```

## 注意事项

* [x] 1. 项目数据集须在[TLC](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)上下载，本项目使用数据为`Yellow Taxi Trip Records`
* [x] 2. 项目运行前需在根目录下创建data文件夹存放上述下载的数据

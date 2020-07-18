#### matplotlib
- 折線圖  
  ```
  plt.plot([x串列], [y串列], [其他參數])

  其他參數:
    linestyle: {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
    linewidth: 寬度 float
    color: 線的顏色
    maker: 設定標記樣式
        ".", "o", "*" ...
    markersize: float
    label: 設定圖例名稱，需搭配legend()才有效果
  ```
- 設定標題  
  - plt.title(圖表標題, (fontsize=點數))
  - plt.xlabel(x座標標題, (fontsize=點數))
  - plt.ylabel(y座標標題, (fontsize=點數))
- 設定座標範圍  
  - plt.xlim(起始值, 終止值)
  - plt.ylim(起始值, 終止值)
- 設定刻度  
  - plt.xticks(串列)
  - plt.yticks(串列)
- 設定格線
  - plt.grid(True)
  - plt.gird(color='red' ..)與設定線的方式一樣
- 同時繪製多組線  
  ```
  plt.plot(x1, y1)
  plt.plot(x2, y2)

  or 
  plt.plot(x1, y1, 其他參數, x2, y2, 其他參數)
  ```
- 設定中文字型  
  plt.rcParams['font.sans-serif'] = "Microsoft JhengHei"  
  
- 設定圖表區 figure

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

    color linestyle maker，可以一次設定，如g--*
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
  
- 設定圖表區 figure，在沒有特別處理的情況下，matplotlib會自動產生圖表區
  - 建立圖表區 plt.figure([參數屬性])
    - figsize，設定方式為串列: [寬、高]，單位為英吋，預設值為[6.4, 4.8]
    - dip: 解析度，單位唯每英吋的點數
    - facecolor: 設定背景顏色
    - edgecolor: 設定邊線顏色
    - frameon: 是否有邊框，預設為True
    - tight_layout，這定多個圖表是否有邊界，預設為False
- 圖表區加上多張圖表
  - plt.subplot(橫列數, 直欄數, 圖表索引值)
  - plt.axes([與左邊界的距離 與下邊界的距離 寬 高])
    - 這四個數字都是以圖表區的寬高為基準，用0-1之間的浮點數作為計算
    - axes以圖表區的左下角為原點
    - 因為axes是用相對位置來加入圖表，因此可以疊加

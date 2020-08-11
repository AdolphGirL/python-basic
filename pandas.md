#### 基於numpy的擴充
#### Series
- pd.Series(資料, [index=索引])
- 資料可以使用list、元組、字典或numpy陣列，index為可選的選項
- 例如  
  ```
  se = pd.Series(['A', 1, 2])
  print(se)
  print(se.values)
  print(se.index)
  ----------------------------------

  字典建立Series，會自動將字典的key轉換為Series的索引，而字典的值會變為Series的資料
  data = {'A': 1, 'B': 2, 'C': 3}
  se = pd.Series(data)
  print(se)
  print(se.values)
  print(se.index)
  ```
- Series取值，可以使用相關索引(index)或範圍來顯示值  
  ```
  # 索引取值
  print(se['A'])
  print('-' * 6)

  # 位置取值
  print(se[1])
  print('-' * 6)

  # 索引區間取值
  print(se['A':'C'])
  print('-' * 6)

  # 區間取值
  print(se[2:3])
  ```
#### DataFrame的建立  
- pd.DataFrame(資料, [index=索引, columns=欄位])
- 資料可以使用list、元組、字典或numpy陣列
- index columns若沒有填，預設會填入0開始的整數串列
- 例如  
  ```
  df = pd.DataFrame([
      [65, 92, 87, 83, 78],
      [65, 92, 87, 83, 78],
      [65, 92, 87, 83, 78],
  ])
  df
  ----------------------------------

  用字典方式建立，字典的key會當為欄位名稱或index名稱
  df = pd.DataFrame({
    '王曉明': {'國文': 100, '數學': 90, '英文': 88},
    '陳大胖': {'國文': 160, '數學': 97, '英文': 80},
    '張小小': {'國文': 60, '數學': 47, '英文': 85},
  })
  ```
- 取值
  - df[欄位名稱]
  - loc[索引名稱, 欄位名稱]
  - iloc[索引標號, 欄位編號]
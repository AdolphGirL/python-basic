#### python file
- 開啟檔案
  ```
  f = open(檔名, mode)
  f: 回傳file object
  mode: 開啟模式r(唯獨)、w(寫入模式、覆蓋或新增)、a(寫入模式，接著寫入)
  ```
- 若完成動作後，可用file object close()方法關閉檔案
  ```
  f.close()
  ```
- 讀取內容  
  ```
  f.read([size])
  f.readline()，讀取一行
  file.readlines()，逐行讀取，回傳list
  ```
- 寫入檔案  
  ```
  f.write()
  file.writelines()
  ```
- 移動  
  ```
  f.seek()，移動
  ```
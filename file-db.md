#### os path
- os.name，系統
- os.sep，路徑分隔號，windows-\\，linux-/
- os.pathsep，分隔路徑的分隔號，windows-;，linux-:
- 當前完整路徑，os.getcwd()
- 當前路徑(相對)，os.curdir
- os.path.join(dirpath, filename)


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
- 實務寫法  
  ```
  with open('iris.csv', newline='') as csvfile:
  ```

#### csv處理 - csv模組
- 讀取出每一列的內容csv.reader，回傳<class '_csv.reader'>
- open('iris.csv', newline='')，再開啟csv檔案時，換行字元可以被正確解析(即不會被當資料讀入)
- 指定分隔字元csv.reader(csvfile, delimiter=':')
- 讀取成dict，csv.DictReader(csvfile)
- 寫入csv，csv.writer(csvfile, delimiter=' ') delimiter，指定分隔樣式
- 若為2為表格，可以直接寫入writer = csv.writer(csvfile)
- 資料格式若為dict，也可以直接寫入writer = csv.DictWriter(csvfile, fieldnames=fieldnames)，但要定義欄位名稱
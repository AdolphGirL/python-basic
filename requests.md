#### requests 模組
- 返回Reponse物件；內容為text: 文字內容、content，二進制資料、status_code，HTTP狀態碼
- get，可以使用dict方式發送  
  ```
  payload = {key1: value1, key2: value2}
  requests.get(url, params=payload)
  ```
- post，直接使用dict方式發送  
  ```
  payload = {key1: value1, key2: value2}
  requests.post(url, data=payload)
  ```
- requests發送請求加入cookie
  ```
  cookie = {xxx: yyy}
  requests.get(url, cookies=cookie)
  ```
- 測試發送網址，可以使用[httpbin.org](https://httpbin.org/)網站

#### BeautifulSoup 模組
- 解析回傳網頁內容使用
- 使用方式 bs4物件 = BeautifulSoup(原始碼, 解析器)  
  內建的解析器 html.parser(python內建，執行速度適中，文件容錯強) lxml(執行速度快，文件容錯強)
  ```
  sp = BeautifulSoup(html.text, 'html.parser')
  ```
- 屬性，標籤名稱；text，去除所有HTML標籤後的文字資料  
- 常用方法  
  - find()，尋找第一個符合條件的標籤，以字串型態回傳，ex: sp.find("a")
  - find_all()，尋找符合條件的所有標籤，以串列方式回傳，ex: sp.find_all("a")
  - select()，CSS選擇器，使用class name or class id，以串列資料回傳，ex: sp.select(".classname")
    也可以搜尋標籤sp.select('title')、id編號sp.select("#id")
- 加入標籤屬性為收尋條件  
  - find find_all ('標籤', 屬性名稱=屬性內容)，但要留意一件事情sp.find('p', class_='red')，class為python保留字，因此需要加上下底線
  - 屬性值可以字典化，提供多個屬性當成條件  
    ```
    datas = sp.find_all('img', {"xxx":"yyy"})
    ```
- 得到搜尋後的結果時，其為標籤物件，若要取得標籤物件內的屬性資料，可以用  
  ```
  sp.select("img")[0].get('src')
  sp.select("img")[0]['src']
  ```

#### Selenium 模組
- Selenium原為網頁測試工具，但由於可以直接以程式碼操控瀏覽器的特性，使其成為網路爬蟲必備的工具之一。
- 在Chrome瀏覽器操作，需要透過Chrome WebDriver(其餘各種瀏覽器，則需要尋找對應的Driver)
- 使用api參考官網[https://selenium-python-zh.readthedocs.io/en/latest/index.html](https://selenium-python-zh.readthedocs.io/en/latest/index.html)
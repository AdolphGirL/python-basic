#### sqlite操作
- connect: 建立connection連線
- cursor: 操作資料庫物件
- commit: 需手動執行
- close: 需手動執行
  
#### SQLite欄位的資料型態
- INTEGER: 整數，欄位大小有1 2 3 4 6 8 bytes，自動依照資料大小變動
- REAL: 浮點數，8 bytes
- TEXT: 不固定長度字串，編碼格式有 UTF-8、UTF-16BE、UTF-16LE
- BLOB: 二進位資料

#### 提供的查詢方法
- fetchall(): 以串列格式回傳所有符合資料，無資料回傳None
- fetchone(): 以tuple回傳符合的第一筆一資料，無資料回傳None
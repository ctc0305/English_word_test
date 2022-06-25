# 單字測驗程式

這個程式以大考中心提供的7000單字Excel檔案作為單字庫，可以做為背單字練習測驗使用，使用者必須先下載第三方模組`openpyxl.py`。大考中心提供的單字檔為`.xls`檔案，但由於要與openpyxl模組相容，所以必須轉檔為`.xlsx`檔案，其中，背單字練習測驗總共有兩個主程式:
- `test_english.py`:題型為拼寫單字，程式會抽出一個單字對應到的詞性和中文，並給英文單字的首尾，拼出單字即可得分。
- `test_english_multiple_choice.py`:題型為選擇題，程式會抽出一個單字對應到的詞性和中文，並抽出8個選項，要選出與題目對應的英文單字。

在測驗結束後，會自動標記儲存格進excel檔案中，`答對`題目會呈現`綠色`，`答錯`題目會呈現`紅色`。

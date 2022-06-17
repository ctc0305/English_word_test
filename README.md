# 單字測驗程式

- 這個單字以大考中心提供的7000單字Excel檔案作為單字庫，可以做為背單字練習測驗使用。其中，`test_english.py`的題型為拼寫單字，程式會抽出一個單字對應到的詞性和中文，並給英文單字的首尾，拼出單字即可得分。而`test_english_multiple_choice.py`的題型則為選擇題，程式會抽出一個單字對應到的詞性和中文，並抽出8個選項，要選出與題目對應的英文單字。要使用這些程式，必須要先下載xlrd套件使用，以讀取.xls檔案，此外，這兩個程式都可以選擇是否要存取自己所做的檔案。

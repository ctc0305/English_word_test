# 單字測驗程式

這個程式以大考中心提供的7000單字Excel檔案作為單字庫，可以做為背單字練習測驗使用，使用者必須先下載第三方模組`openpyxl`。大考中心提供的單字檔為`.xls`檔案，但由於要與openpyxl模組相容，所以必須轉檔為`.xlsx`檔案，其中，背單字練習測驗總共有兩個主程式:
- `test_english_spelling.py`:題型為拼寫單字，程式會抽出一個單字對應到的詞性和中文，並給英文單字的首尾，拼出單字即可得分。
- `test_english_multiple_choice.py`:題型為選擇題，程式會抽出一個單字對應到的詞性和中文，並抽出8個選項，要選出與題目對應的英文單字。

在測驗結束後，會自動標記儲存格進excel檔案中，`答對`題目會呈現`綠色`，`答錯`題目會呈現`紅色`。

單字實測影片: https://youtu.be/EukQrscBYdg


# Program for word test

This program took the 7000-word Excel file provided by the Exam Center as the word database, and the programming can be used to practice memorizeing the words. Users need to download the module `openpyxl` in precedence. The file provided by Exam Center is `.xls` file, however, to let it compatible with openpyxl module, the file should be transformed to `.xlsx` file. There are two main program:
- `test_english_spelling.py`: The problem type is spelling. The program would choose the part of speech and chinese word that corresponding the randomly-chosen word, and give the first and last alphabet of the English word, you will get the score if you spell it correctly.
- `test_english_multiple_choice.py`: The problem type is multiple choice. The program would choose the part of speech and chinese word that corresponding the randomly-chosen word, and provide 8 choices, you should choose the English options corresponding to the problem.

After the test, the program would mark the cells in Excel file automatically. The  `correct` answer would give `green` background color, and the `wrong` answer would give `red` background color.

Word test video: https://youtu.be/EukQrscBYdg

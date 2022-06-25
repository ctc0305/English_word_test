import openpyxl
import random
from lib.file import load_xlsx_file, mark_cells
from lib.problem import start_and_final, remove_word_length, create_spelling
from lib.judge import judge_spelling
#以下兩行可隨檔案名稱及中英文分隔符號調整
filename = 'senior_7000.xlsx'
En_Ch_spliter = '@'

fp = []
try:
    fp = openpyxl.load_workbook(filename)
except:
    print("檔案不存在!")
    quit()

words, number, sheets = load_xlsx_file(fp, En_Ch_spliter)#抓取工作表單字

length = len(words)
print()

start, final = 0, 0
while True:#要以第幾個工作表出題(可以是範圍)?
    try:
        start, final = start_and_final(input("第幾個工作表? "), number)
    except:
        print('\n工作表不存在，請輸入範圍內的正整數。\n')
        continue
    else:
        break
    
print()
print('總單字量:', final - start + 1)
print()

num_of_problems = 0

while True:#決定出題數
    num_of_problems = input('請輸入題數: ')
    if not num_of_problems.isdigit():
        print('\n輸入必須是正整數\n')
        continue
    else:
        num_of_problems = int(num_of_problems)
        break

if num_of_problems > final - start + 1:
    print("\n單字題庫不足，將改為 %d 題。" % (final - start + 1))
    num_of_problems = final - start + 1

print()
problems = random.sample(range(start, final+1, 1), num_of_problems)#選定要出的題目
print()
print()
print('-'*40)
total_score = 0

for i in range(num_of_problems):
    print()
    
    words[problems[i]][1] = remove_word_length(words[problems[i]][1])#去除單字長度提示

    create_spelling(i, words[problems[i]])#格式化印出題目

    print()
    
    answer = input("請輸入答案: ")
    print()
    
    score = judge_spelling(answer, words[problems[i]][0]) * 100/num_of_problems
    if score > 0:#標記正確和錯誤的題目
        mark_cells(True, fp, problems[i], number, sheets)
    else:
        mark_cells(False, fp, problems[i], number, sheets)
    total_score += score
    print()
    print()
    print('-'*40)
    
print()
fp.save(filename)
print('測驗成績為: %.1f' % (total_score))

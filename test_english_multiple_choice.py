import openpyxl
import random
from lib.file import load_xlsx_file, mark_cells
from lib.problem import start_and_final, remove_word_length, create_multiple_choice, print_detail
from lib.judge import judge_multiple_choice
#以下兩行可隨檔案名稱及中英文分隔符號調整
filename = 'senior_7000.xlsx'
En_Ch_spliter = '@'
fp = []
try:
    fp = openpyxl.load_workbook(filename)
except:
    print("檔案不存在!")
    quit()
print()
sheets = fp.sheetnames
start, final, total_word_num, sheet_num = 0, 0, 0, len(sheets)
while True:#要以第幾個工作表出題(可以是範圍)?
    try:
        start, final= start_and_final(input("第幾個工作表? "), sheet_num)
    except:
        print('\n工作表不存在，請輸入範圍內的正整數。\n')
        continue
    else:
        break
words, number, total_word_num = load_xlsx_file(fp, En_Ch_spliter, start, final, sheets)#抓取工作表單字
print()
print('總單字量:', total_word_num)
print()
if total_word_num < 8:
    print('\n單字庫無法出選擇題!')
    quit()   
num_of_problems = 0
while True:#決定出題數
    num_of_problems = input('請輸入題數: ')
    if not num_of_problems.isdigit():
        print('\n輸入必須是正整數\n')
        continue
    else:
        num_of_problems = int(num_of_problems)
        break
if num_of_problems > total_word_num:
    print("\n單字題庫不足，將改為 %d 題。" % (total_word_num))
    num_of_problems = total_word_num
print()
problems = random.sample(range(0, total_word_num, 1), num_of_problems)#選定要出的題目
print()
print()
print('-'*76)
total_score = 0
for i in range(num_of_problems):
    print()

    words[problems[i]][1] = remove_word_length(words[problems[i]][1])#去除單字長度提示
        
    print(i+1, '. ', words[problems[i]][1],  sep = '' )

    options_loc = random.sample(range(0, total_word_num, 1), 8)

    correct_answer, options = create_multiple_choice(options_loc, problems[i], words)#格式化印出選擇題
        
    answer = input("請輸入答案: ")
    print()

    score = (100 / num_of_problems) * judge_multiple_choice(answer, correct_answer, options)
    total_score += score

    if score > 0:#標記正確和錯誤的題目
        mark_cells(True, fp, problems[i], number, sheets, start)
    else:
        mark_cells(False, fp, problems[i], number, sheets, start)

    print()
    c = input()
    if(c != ''):
        print_detail(words, options_loc)
    print()
    print('-'*76)
print()
fp.save(filename)
print('測驗成績為:%.1f' % (total_score))



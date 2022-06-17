import random
from lib.file import *
from lib.problem import *
from lib.judge import *

words, number = read_xls_file()

length = len(words)
print()

start, final = start_and_final(input("請輸入單字等級: "), number)
print()
print('總單字量:', final - start + 1)
print()
num_of_problems = int(input("請輸入題數: "))
print()
save_file = input("是否存取答錯單字? (y/n) ")
problems = random.sample(range(start, final+1, 1), num_of_problems)
print()
print()
print('----------------------------------------------------------------------------')
total_score = 0

if('y' in save_file.lower()):
    wa = open('wa.csv', 'a', encoding = 'BIG5')

for i in range(num_of_problems):
    print()

    words[problems[i]][1] = remove_word_length(words[problems[i]][1])
        
    print(i+1, '. ', words[problems[i]][1],  sep = '' )

    options_loc = random.sample(range(start, final+1, 1), 8)

    correct_answer, options = create_multiple_choice(options_loc, problems[i], words)
        
    answer = input("請輸入答案: ")
    print()

    score = (100 / num_of_problems) * judge_multiple_choice(answer, correct_answer, options)
    total_score += score
    if(score == 0. and 'y' in save_file.lower()):
        write_csv_file(wa, words[problems[i]])
    print()
    c = input()
    if(c != ''):
        print_detail(words, options_loc)
    print()
    print('----------------------------------------------------------------------------')
print()
print('最終成績為:',total_score)

if('y' in save_file.lower()):
    wa.close()

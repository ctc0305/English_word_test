def judge_multiple_choice(answer, correct_answer, options):
    if(answer == str(correct_answer)):
        print('正確!')
        return 1.
    else:
        try:
            if(options[int(answer) - 1][0] == options[correct_answer - 1][0]):#選項重複的情況(工作表有重複單字)
                print('正確!')
                return 1.
            elif(options[int(answer) - 1][1] == options[correct_answer - 1][1]):#詞性和英文一樣的情況
                print('正確!')
                return 1.
            else:
                print('錯誤，答案為: ', '(', correct_answer, ')', sep = '')
                return 0.
        except:
            print('錯誤，答案為: ', '(', correct_answer, ')', sep = '')
            return 0.

def judge_spelling(answer, correct_answer):
    if(answer == correct_answer):
        print('正確!')
        return 1.
    else:
        print('錯誤，答案為:', correct_answer)
        return 0.

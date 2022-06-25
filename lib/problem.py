import random

def start_and_final(classes, sheet_num):
    classes = classes.split('~')
    if(len(classes) == 1):
        classes.append(classes[0])
    if not (classes[0].isdigit() and classes[1].isdigit()):
        return
    if int(classes[0]) <= 0 or int(classes[1]) <= 0 or int(classes[0]) > int(classes[1]) or int(classes[1]) > sheet_num:
        return
    return int(classes[0]), int(classes[1])

def remove_word_length(string):
    j = 0
    while string[j] != ')':
        if(string[j].isdigit() or string[j] == '.'):
            string = string.replace(string[j], '')
            j -= 1
        j += 1
        if j == len(string) - 1:
            break
    return string

def create_multiple_choice(options_loc, index, words):
    correct_answer = 0
    options = []
    for j in range(8):
        options.append(words[options_loc[j]])
        if(options_loc[j] == index):
            correct_answer = j + 1
    if correct_answer == 0:
        k = random.randint(0, 7)
        options[k] = words[index]
        options_loc[k] = index
        correct_answer = k + 1
    print()
    opt = ''
    for j in range(8):
        opt += ('('+str(j+1)+') ' + '%-15s'%(options[j][0]))
        if(j % 4 == 3):
            opt += '\n'
    print(opt)
    return correct_answer, options
    
def create_spelling(i , word_lst):
    prob = ''
    prob += str(i+1) + '. ' + word_lst[1] + '('
    if len(word_lst[0]) == 1:
        prob += '_'
    elif len(word_lst[0]) == 2:
        prob += word_lst[0][0] + '_'
    else:
        length = len(word_lst[0])
        prob += word_lst[0][0]
        for j in range(length - 2):
            prob += '_'
        prob += word_lst[0][length-1]
    prob += ')'
    print(prob)
    return

def print_detail(words, options_loc):
    print()
    detail = ''
    for j in range(8):
        detail += str(j+1) + '. %-15s' % (words[options_loc[j]][0]) + ' '
        string = remove_word_length(words[options_loc[j]][1]) + '\n'
        index = 0
        for index in range(len(string)):
            if(string[index] == ')' and (string[index - 1].isalnum() or string[index - 1] in ',.;:')):
                break
        if index != len(string) - 1:
            part = string[:index + 1]
            chinese = string[index + 1:]
            detail += '%-7s' % part + chinese
        else:
            detail += string
    print(detail)
    d = input()
    return



from openpyxl.styles import PatternFill

def load_xlsx_file(fp, spliter):
    word = []
    numbers = []
    sheets = fp.sheetnames
    for i in range(len(sheets)):
        sheet = fp[sheets[i]]
        numbers.append(sheet.max_row)
        for j in range(numbers[i]):
            try:
                word.append(sheet.cell(j+1, 1).value.split(spliter))
            except:
                print("工作表含無效的儲存格!")
                quit()
    return word, numbers, sheets

def mark_cells(color, fp, index, number, sheets):
    order = 0
    sheet_name = ''
    for i in range(len(sheets)):#尋找要標記的位置
        if order + number[i] <= index:
            order += number[i]
        else:
            sheet_name = sheets[i]
            break
    sheet = fp[sheet_name]
    if color:#如果答案正確填綠色，反之則填紅色
        sheet.cell(index - order + 1, 1).fill = PatternFill("solid", fgColor = "00FF00")
    else:
        sheet.cell(index - order + 1, 1).fill = PatternFill("solid", fgColor = "FF0000")
    

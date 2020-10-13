#coding by S.Z.Chang
def search(sob,finding):
    for student in sob:
        if(student.find(finding) != -1):
            print(student)
def search_number_group(sob,findings_str):
    findings = findings_str.split(' ')
    total = ""
    key = 0
    print(len(findings))
    for finding in findings:
        for student in sob:
            if (student.find(finding) != -1):
                st = student.split(',')
                number = st[0]
                total += number + '\n'
                key += 1
    print(key)
    return total
def search_rank():
    title = "csv_sob_"
    path = "/Users/szchandler/Desktop/ram/"
    table = {}
    for i in range(0, 3):
        lines = []
        full_title = path + title + str(i) + ".csv"
        with open(full_title, 'r') as ft:
            file = ft.readlines()
        for line in file:
            if not (line == '\ufeff学号,姓名,学院,年级,专业,专业方向,班级,加权平均成绩\n'):
                lines.append(line)
        for rank,line_r in enumerate(lines):
            ls = line_r.split(',')[1]
            table[ls] = rank+1
    findings_str = input("请输入学生姓名或学号：")
    findings = findings_str.split(' ')
    for name in findings:
        print(table[name])
def search_imformation():
    title = "csv_sob_"
    path = "/Users/szchandler/Desktop/ram/"
    lines = []
    for i in range(0, 3):
        full_title = path + title + str(i) + ".csv"
        with open(full_title, 'r') as ft:
            file = ft.readlines()
        for line in file:
            if not (line == '\ufeff学号,姓名,学院,年级,专业,专业方向,班级,加权平均成绩\n'):
                lines.append(line)
    while 1:
        find = input("请输入学生姓名或学号：")
        if (find == "exit"):
            break
        print(search_number_group(lines, find))
#rome forever (773BC--1453-- )
if __name__ == '__main__':
    search_imformation()
    # search_rank()

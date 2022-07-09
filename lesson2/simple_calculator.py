invalid = True
while invalid:
    invalid = False
    exersice_task = input('Write an exersice\n')
    if exersice_task.index('=') != len(exersice_task) - 1 or exersice_task[0] in '*/':
        print('Your exersice is invalid')
        invalid = True
        continue
    for s in exersice_task:
        if s not in '1234567890+-*/= ':
            print('Your exersice is invalid')
            invalid = True
            break



exersice_task = exersice_task.replace(' ', '')
exersice_list = []
i = 0
j = 0
while i < len(exersice_task):
    if exersice_task[i].isdigit() or exersice_task[i] in '+-':
        exersice_list.append(exersice_task[i])
        i += 1
    while exersice_task[i].isdigit():
        exersice_list[j] += exersice_task[i]
        i += 1
    j += 1
    if exersice_task[i] in '*/=':
        exersice_list.append(exersice_task[i])
        j += 1
        i += 1


exersice_list.remove('=')
for i in range(len(exersice_list)):
    if exersice_list[i] not in '*/':
        exersice_list[i] = float(exersice_list[i])

while '*' in exersice_list or '/' in exersice_list:
    for i in range(len(exersice_list)):
        if not str(exersice_list[i]).isdigit():
            if exersice_list[i] == '*':
                exersice_list[i - 1] = exersice_list.pop(i - 1) * exersice_list.pop(i)
                break
            if exersice_list[i] == '/':
                exersice_list[i - 1] = exersice_list.pop(i - 1) / exersice_list.pop(i)
                break


print(sum(exersice_list))
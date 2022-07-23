l = input()
new_l = list(map(int, filter(str.isdigit, l)))
print(new_l)
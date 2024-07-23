file = open('custom_errors.txt', 'r', encoding='utf-8')
for line in file:
    print(line.strip("\n").split(", "))
# print(line)
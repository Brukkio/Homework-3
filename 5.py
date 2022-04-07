# Bruk Tewelde
# PSID 1834503

numbers = input()
user_list = numbers.split()
NumList = []
for x in user_list:
    if int(x) > 0:
        NumList.append(int(x))
NumList.sort()
for x in NumList:
    print(x, end='')
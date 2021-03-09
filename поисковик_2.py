total_str = []
flag = True
while flag:
    s = input()
    total_str.append(s)
    if s == 'yamete kudasai':
        flag = False

    
total_req = []
flag = True
while s != 'search':
    s = input()
    total_req.append(s)
    if s == 'поиск':
        flag = False

    
#for j in range(len(total_str)):
#    total_str[j] = total_str[j].lower()
    
for i in range(len(total_str)):
    count = 0
    for j in range(len(total_req) - 1):
        if total_req[j].lower() in total_str[i].lower():
            count += 1
        if count == len(total_req) - 1:
            print(total_str[i])


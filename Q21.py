list1=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
i=0
l=[]
while i<len(list1):
    for x in list1[i]:
        l.append(list1[i][x])
    i+=1
dic=[]
i=0
while i<len(l):
    if l[i] not in dic:
        dic.append(l[i])
    i+=1
print(dic)
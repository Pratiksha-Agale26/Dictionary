dict=[{"name":"pratiksha","age":19},{"name":"aku","age":16},{"name":"sakshi","age":17}]
a=[]
for i in range(len(dict)):
    for x,y in dict[i].items():
        if x=="age":
            a.append(y)
print(a)
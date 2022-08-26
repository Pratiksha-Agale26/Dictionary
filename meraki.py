# city_population = {
# "NewYorkCity":8550405,
# "LosAngeles":3971883, 
# "Toronto":2731571, 
# "Chicago":2720546, 
# "Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }

# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))


# Dict = {
#     'ball' : 'green',
#     'Ball': 'red'
# }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# student=dict(name= "Ravina",age= 20)
# print(student)

# my_dict = {1:'apple', 2:'ball'}
# print(my_dict)

# Dic= {
#  1: 'NAVGURUKUL',
#  2: 'IN',  
#  3:{
# 'A' : 'WELCOME',
# 'B' : 'To', 
# 'C' : 'DHARAMSALA'
# }
# }
# print(Dic)

# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organisation'}

# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# dic= {
# 'Name': 'RAM', 
# 'Age': 17,
# }
# dic['ORGANIZATION'] = "NAV GURUKUL"

# dic['place'] = 'dharamsala'

# print(dic)

# car ={
# "brand":  "ford",
# "model":  "mustang",
# "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")

# else:
#     print("No, 'model' key dictionary mai nahi hai.")

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)


# details={
# 'Name': 'RAM',
# 'Age': 17, 
# 'student': {
# 'id': 22,
# 'place': 'dharamsala'
# } } 
# details['student']['id']=35
# print(details)

# classes ={
# "room1":  "6th",
# "room2":  "7th",
# "room3":  "8th"
# }
# mydict=classes.copy()
# print(mydict)

# CAR_DETAILS={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# person.popitem()
# print(person)

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# del person['place']
# print(person)

# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   print(state)

# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }

# for state in states_capitals:
#     print(states_capitals[state])


# details ={
# "name":  "Bijender",
# "age":  17,
# "class":  "10th"
# }
# for x in details.values():
#     print(x)

# movie ={
# "name":  "Puli",
# "hero":  "Vijay",
# "rating":  7.5
# }
# for x,y in movie.items():
#     print(x,y)

# a={'a':1,'b':2,'c':{'d':{'q':3}},'d':{'c':9,'b':{'a':11,'c':10}}}
# for i in a:
#     if i=='c':
#         print(a[i])
#         if type(a[i])==dict:
#             for j in a[i]:
#                 print(a[i][j])
#                 if type(a[i][j])==dict:
#                     for k in a[i][j]:
#                         print(a[i][j][k])
#     if i=='d':
#         if type(a[i])==dict:
#             # print(a[i])
#             for j in a[i]:
#                 print(a[i][j])
#                 if type(a[i][j])==dict:
#                     for k in a[i][j]:
#                         print(a[i][j][k])
#                         for l in a[i][j]:
#                             if k=='a':
#                                 print(a[i][j][k])
#             # for l in a[i][j][k]:
#             # print(a[i][j][k][l])
#             # if type(a[i][j][k][l])==dict:
#             #     for m in a[i][j][k][l]:
#             #         print(a[i][j][k][l][m])
#             #         if type(a[i][j][k][l][m])==dict:
#             #             for n in a[i][j][k][l][m]:
#             #                 print(a[i][j][k][l][m][n])
#             #                 if type (a[i][j][k][l][m][n])==dict:
#             #                     for o in a[i][j][k][l][m][n][o]:
#             #                         print(a[i][j][k][l][m][n][o])

                
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# dic1.update(dic3)
# print(dic1)

# dict1={"name":"raj", "marks":56}
# check=input("enter the number")
# if check in dict1:
#     print("exit")
# else:
#     print("not exit")

# my_dict = {'data1':100,'data2': -54,'data3': 247}
# dic1={}
# sum=0
# for i in my_dict:
#     sum=sum+my_dict[i]
# print(sum)

# dict= {1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# for i in dict:
#     print(dict[i])
#     if type (dict[i])==dict:
#         for j in dict[i]:
#             print(dict[i][j])


# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# i=0
# d={}
# while i<len(list1):
#     d [(list1[i])]=(list2[i])
#     i=i+1
# print(d)

# dic={"ball":"red","bat":4,"wickets":8,"ball":"green","bat":3}
# d={}
# for key,value in dic.items():
#     if value not in d.values():
#         d[key] = value
# print(d)

# dict=[{"first":"1"}, {"second": "2"},{"third": "1"}, {"four": "5"}, {"five":"5"}, {"six":"9"},{"seven":"7"}]
# k=[]
# for i in dict:
#     for j in i:
#         if i[j] not in k:
#             k.append((i[j]))
# print(k)

# student=dict()
# n=int(input("enter the number"))
# for i in range(n):
#     sname=input("enter the name")
#     for j in range(1):
#         mark=int(input("enter the number"))
#         student[sname]=mark
# print(student)
# 'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56

# a="MISSISSIPPI"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# print(b)

# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#     if type(dict1[i]) is list:
#         count=count+len(dict1[i])
# print("total list value:-",count)

# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# max1=0
# max2=0
# max3=0
# for i in my_dict:
#     if my_dict[i]>max1:
#         max3=max2
#         max2=max1
#         max1=my_dict[i]
#     elif my_dict[i]>max2:
#         max3=max2
#         max2=my_dict[i]
# print([max1,max2,max3])

# a=int(input("enter the number"))
# d={}
# for a in range(1,a):
#     d.update({a:a**2})
# print(d)

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # x = thisdict["model"]
# x = thisdict.items()
# print(x)

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# print(mydict)

# d1={"a":100,"b":200,"c":300}
# d2={"a":300,"b":200,"d":400}
# for i in d2 :
#     if i in d1 :
#         d1[ i ] = d1[ i ] +d2[ i ]
#     else :
#         d1[ i ] = d2[ i ]
# print(d1)

# dic={1:0,2:3,4:2,3:1}
# l=[]
# for i in dic:
#     l.append(i)
# for i in range(len(l)):
#     for j in range(len(l)):
#         if l[j]<l[i]:
#             tem=l[i]
#             l[i]=l[j]
#             l[j]=tem
# print(l)
# dic1={}
# for i in range(len(l)):
#     for j in dic:
#         if i==j:
#             dic1.update({i:dic[j]})
# print(dic1)

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#     c.update(i)
# print(c)

# c=dict()
# for i in range(1,16):
#     c=i*i
# print(c)

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1.values():
#     sum=sum+i
# print(sum)


a=["pratiksha","dhanashree","kranti"]
b=["22","18","20"]
c=["agale","sarvade","waghmare"]
p=[]
i=0
while i<len(a):
    j=0
    g={}
    while j<len(b):
        k=0
        while k<len(c):
            if i==j==k:
                g.update({b[j]:c[k]})
            k+=1
        j+=1
    p.append({a[i]:[g]})
    i+=1
print(p)

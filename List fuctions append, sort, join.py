#append

a = [1,2,3,4,5]
a.append("bala")
print(a)

a=input()
d=[]
for i in a:
    d.append(i)
print(" ".join(d))


#Insert

thislist=["apple", "banana", "cherry"]
for item in enumerate(thislist):
    print(item)
thislist.insert(2, "orange")
print(thislist)


#Remove

a=["apple", "banana", "cherry"]
a.remove("apple")
print(a)

#Delete

thislist=["apple", "banana", "cherry"]
print(id(thislist))
del thislist[0]
print(thislist)

#multiple Delete

a=[1,2,3,4,5,6,7,8,9,10,11,12,1,3,14,15,16,17,1,8,19]
a=list(range(20))
del a[0]#step operator
print(a)

#pop

a=[1,2,3,4,5,6,7,8,9]
   #0 1 2 3 4 5 6 7 8
a.pop(-3)
print(a)

#Index

a=[1,2,3,4,5,6,7,8,9,10,20,3,0,30,3,0,3,3,"deepika", "Titikksha"]
for i in enumerate(a):
    print(i)
print(a.index(30))


#Clear

thislist=["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#reverse

a=[1,2,3,4,5,6,7,8,9,10,20, "AAA", "Titikksha", "deepika"]
a.reverse()
print(a)


#count:

a=[1,2,3,4,5,6,7,8,9,10,20,3,0,30,3,0,3,3,"deepika", "Titikksha"]
print(a.count(3))


#sort:

a=[1,2,3,4,5,6,7,8,9,10,20,3,0,30,3,0,3,3]
a.sort()
print(a)
a.reverse()
print(a)
a=input().split()
print(a)


list = ["guvi",1.0, 5, True]
print(list)


tuple = ("guvi",1.0, 5, True)
print(tuple)


dict = {"name":"guvi","mark":1.0, "range":5, "do":True}
print(dict)


set = {"guvi",1.0, 5, True, 5, "GUVI"}
print(set)
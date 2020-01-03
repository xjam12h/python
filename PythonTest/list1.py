#イテレータ
data1=[1,2,3,4,5,6,7,8,9.10]
it1=iter(data1)
print(it1)
print(next(it1))
print(next(it1))



data2=[11,31,555,551,152]
data3=[]
for i in zip(data1,data2):
    data3.append(i)
    print(i)
for i in enumerate(data3):
    print(i)
for i ,j in data3:
    print(i,j)
    
print(data3)

data4=[1,2,3,4,5]
data5=[n*2 for n in data4 if n!=3]
print(data5)
print(max(data5))
print(min(data5))
print(sum(data5))
print(sorted(data2))
data5.sort(reverse=True)
print(data5)

data6=[[1,4],
       [4,7],
       [4,"京都"],
       [10,"東京"]]

print(data6)



    
    


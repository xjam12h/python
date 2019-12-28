list1=[1,2,3,4,5,6,7,8,9,10]


print(list1)

for i in range(10):
    print(list1[i]-1,",",end="")

print("")
    
print("list1の長さ : ",len(list1))

for i in list1:
    print(i)
    
num=int(input("変更するデータの番号"))
data=int(input("変更後のデータ"))

for i in range(len(list1)):
    if(i+1==num):
        list1[i]=data
    print(list1[i])


list2=[3,7,9,10]
list2.append(100)
print(list2)
del list2[2]
print(list2)


list3=[5,7,10,55,28]
list3.insert(len(list3)-1,100)
print(list3)
list3.remove(7)
print(list3)
#同じリストを差すようになっただけ
print("list3をlist2と同化")
list3=list2
print(list2)
print(list3)
print("list2のデータを変更")
del list2[0]
print(list2)
print(list3)


#新しいリストの作成
print("リストの作成")
list4=list(list3)
print(list3)
print(list4)
print("listの値を変更")
del list3[1]
list4.append(5)
print(list3)
print(list4)
#コピーは可能
list5=list4.copy()
print("list4をlist5にコピー")
print(list4)
print(list5)
del list4[0]
list5.insert(1,1000)
print("値を変更")
print(list4)
print(list5)

#連結
list6=list4+list5
print(list6)
list6.remove(5)
print(list6)
#list1+=list2
#list1.extend(list2)
#等も使える
list6.insert(3,"あいうえお")
print(list6)
list7=list6[0:3]
list8=list6[6:]
list9=list6[::2]
list10=list6[::-1]
list11=list6[:4]
print(list7)
print(list8)
print(list9)
print(list10)
print(list11)
list6.reverse()
print(list6)


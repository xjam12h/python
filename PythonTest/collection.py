#タプル タプルは変更不可能

tap1=(1,2,5,6,8)
print(tap1)
print(tap1[1])

#ディクショナリ

dic1={"京都":10,"東京":1,"大阪":3,"沖縄":40}
print(dic1)
print(dic1["東京"],dic1["京都"])
key=input("キーを入力してください")
if key in dic1:
    print(key,"のデータは、",dic1[key],"です")
else:
    print(key,"のデータは見つかりませんでした")
    
if key not in dic1:
    print("データは存在しません")
    
    
changeKey=input("変更するキーを入力してください")
changeData=input("変更後のデータを入力してください")
if changeKey not in dic1:
    print("データは存在しません")
else:
    dic1[changeKey]=changeData
    print(dic1)

for k in dic1.keys():
    print(k,end="\t")
print()
for v in dic1.values():
    print(v,end="\t")
print()
for item1 in dic1.items():
    print(item1,end="\t")
print("\n")

dic2={"神奈川":41,"栃木":19,"大阪":100,"京都":80}
dic1.update(dic2)
print(dic1)
newKey=input("キー名の入力")
newData=input("新しいデータ")
dic1[newKey]=newData
print(dic1)

#セット
set1={1,3,45,6,1,7,344}
print(set1)
set1.add(1111)
set1.remove(1)
set1.add(96)
print(set1)
set2={1,3,1,7,344}
print(set1&set2)
print(set1-set2)
print(set2-set1)
print(set1|set2)


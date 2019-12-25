test=int(input("整数を入力してください"))
print(test,"が入力されました")
if test>100:
    print("入力した値は１００以上です")
elif test<100:
    print("入力した値は１００未満です")
else:
    print("１００が入力されました")
    
    

for i in range(10):
    print(i+1,"回目のループ") 
    
for i in range(0,10,2):
    print(i+2,"範囲指定、間隔も指定できる") 
    
i=1;
while i<=12:
    print(i,"回目のループ　whileバージョン")  
    i+=1
    
for i in range(5):
    for j in range(5):
        print(i+1,"*",j+1,"=",(i+1)*(j+1)," ",end="")
    print("\n")
    

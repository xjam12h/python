def function1():
    print("関数が呼び出されました")
def double(num):
    print("２倍します")
    return num*2
def func(*key):
    print(key)
    print(key[1])
def func1(**key):
    print(key["a"])
    print(key["b"])
    print("掛け算")
    print(key["a"]*key["b"])

function1()

num1=int(input("整数を入力してください"))
print(double(num1))


func(1,2,3,5,6,7,3)
func(9,1)

func1(a=1,b=21)
func1(a=31,b=414)



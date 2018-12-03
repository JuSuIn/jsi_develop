#In[1]

if True :
    print("Yes")
if False :
    print("퍼얼스")
    
#4-2 다음은 단독으로 조건에 들어가면 True로 취급합니다.

print("다음은 단독으로 조건에 들어가면 True로 취급합니다.")
number_true = 39;
string_true = "Miku"
list_true = [3,9,39]
tuple_true = (3,9,39.39)
dict_true = {"name":"Song hana"}

#다음은 false 로 취급합니다.

print("다음은 false 로 취급합니다.")
number_false = 0
string_false = ""
list_false = []
tuple_false = ()
dict_false = {}

#In[2] :
a = 1
b = 0

print(a == b)

print(a != b)

print(a > b)

print(a < b)

print(a <= b)

#리스트 딕셔너리 집합 튜플과 함께 사용하는 in

#In[11]

l = [1,2,3]
s = {4,5,6,6}
d = {"one":1, "two":2, "three":3}
t = (7,8,9)

print("리스트 딕셔너리 집합 튜플과 함께 사용하는 in")

print(1 in l)
print(6 in s)
print(7 in s)
print("one" in d)
print(9 in t)
print(10 in t)

print("for문")

for i in range(10):
    print(i)


print("for문을 딕셔너리를 이용해 응용해서 TEST")

Diva_infor = { "fatherName":"주성래",
               "motherName":"서영옥",
               "MyName":"주수인",
               "sisterName":"주민희"}

for title in Diva_infor :
    print(title,":",Diva_infor[title]);
    


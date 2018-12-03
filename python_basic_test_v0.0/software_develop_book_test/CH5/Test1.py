#.
def soGae(value):
    print("안녕하세요? 제이름은 :",value)
    print("입니당")

def mainTest():
    ret_Value = "주수인";
    soGae(ret_Value);

mainTest();

#----------------------------------------------------------------------

#In[1]
print("Test2 : 타입힌팅")

def count_length(world : str , num : int) -> int:
    return len(world) *num

print(count_length("Miku",39));

#in[7]
print("함수를 변수 처럼 전달하기 ")
def transform_func(num):
    return num;

def add_with_transform(left,right,transform_func):
    tmp_value=transform_func(left)+transform_func(right)
    return transform_func(tmp_value);

def add_plus_1(number):
    #print("궁금 데스네 ",number+1)
    return number+1;

print(" (2 + 1) + (3 + 1) + 1 = 8 ");

ret_val = add_with_transform(2,3,add_plus_1);
#ret_val = transform_func(8);

print(ret_val);

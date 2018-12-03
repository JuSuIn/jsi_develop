#In[1]

#파이썬 연습 생성사 생성방식

print(" 6-2 파이썬 연습 생성자 생성방식");

class Diva:
    print("클래스 변수")
    version = "v3"

    #생성자
    def __init__(self, name = ""):
        self.name = name
    #메서드
    def song(self, title = "song"):
        print(self.name + " sing the "+title)

    def medley(self):
        self.song()
        self.song("second song")
        self.song("third song")
        
print("6-3 클래스 변수 사용")

diva1 = Diva()
diva2 = Diva("주수인")
diva3 = Diva("주민희")


def print_diva_info(diva):
    print("====")
    print("Name : ",diva.name)
    print("Version : ",diva.version)

print_diva_info(diva1)
print_diva_info(diva2)
print_diva_info(diva3)

print("6-5 클래스에 메서드 추가 ")

voice_diva = Diva("TEST")
voice_diva.song()
voice_diva.song("wolrd is Mine")
voice_diva.medley();


print("6-7 클래스 메서드에 전달하는 첫번째 파라미터")
Diva.song(voice_diva, "Tell your world")

print("6-8 self 를 메서드의 파라미터로 추가하지 않음")

class calulator:
    def adder(l,r):
        print(l+r)

calulator.adder(3,9)














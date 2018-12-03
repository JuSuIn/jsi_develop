#상속 

class Diva:
    print("클래스 변수")
    version = "v3"

    #생성자
    def __init__(self, name = ""):
        self.name = name
    #메서드
    def song(self, title = "song"):
        print(self.name + " sing the "+title)


class Miku(Diva):
    def __init__(self,module = "class uniform"):
        self.module = module
        print("슈퍼클래스를 초기화하지 않으면")
        print("슈퍼 클래스에서 초기화 & 할당되는 name 변수를 사용할 수 없습니다.")

        super().__init__("Miku")

    def dance(self):
        print("Dancing")
        

print("in[9]")

hatsune_miku = Miku()
print(hatsune_miku.module)
print(hatsune_miku.version)
print(hatsune_miku.name)
hatsune_miku.dance()
hatsune_miku.song("Hello worker")



print("6-12 덕타이핑")

class Cat:
    def sound(self):
        print("Nya")

class Dog:
    def sound(self):
        print("Mung")

cat = Cat();
dog = Dog();

animals = [cat,dog]

for animal in animals:
    animal.sound();
    

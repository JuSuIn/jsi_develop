#개발자를 위한 파이썬 기본 실습

# 데이터 타입과 기본 연산자

#3.1 코드

#in[1]

diva= "Song Hana";
is_she_play_to_win = True;
digital_diva = "Hatsune Miku";
diva_version = 3.0;
how_many_diva = 2
diva_list=[diva,digital_diva];
new_challenger = { "name":"Miku" };

print(type( diva ));
print(type( is_she_play_to_win ));
print(type( digital_diva ));
print(type( diva_version ));
print(type( how_many_diva ));
print(type( diva_list ));
print(type( new_challenger ));


#3.2 코드

#in[2]

i  = 39;
i2 = -3;
biiiiig_int = 9999999999999999999999999999999999;

print(i);
print(i2);
print(biiiiig_int);


#3.4 코드
#In[4]

print("-----------------------------------정수 ,실수 연산 -------------------------------------")
i1 = 39
i2 = 939
big_in1 = 123456789123456789012345678901234567890
big_in2 = 999999999999999999999999999999999999999
f1 = 1.234
f2 = 3.939


# +
print("##### + #####")
print("i1 + i2",i1+i2) #정수끼리
print("f1 + f2",f1+f2) #실수끼리
print("big_in1 + big_in2 ",big_in1+big_in2); #엄청큰수 끼리
print("i1 + f1 : ",i1+f1); # 실수와 정수 끼리







#3.8
print("raw 문자열 사용법 ")
print("\n\n\n\n");

#in[8]

raw_s1 = r'C:\Programs\new program\"';
raw_s2 = r"\\t\n\b\s";
raw_s3 = r'\'"';
raw_s4 = r"\"'";

print(raw_s1+"\n");
print(raw_s2+"\n");
print(raw_s3+"\n");
print(raw_s4+"\n");



#3.9
#In[9]

print("멀티라인 문자열 표현법 ");

multi_s = """ 이문자열은




멀티라인의




문자열표현법 """;


print(multi_s);





#3.13

#in[13]

#리스트 사용 방법
print("리스트 사용 방법 ");
print("\n\n\n\n\n");

i1 = [1, 2, 3];
i2 = ["a" , "b" , "c"];
i3 = ["miku", 39 ];
i4 = [ [0,1], [2,3], [4,5] ];
i5 = list("hatsune Miku");
i6 = list(i1+i2+i3+i4);


print(i5);
print(i6);






#리스트 아이템에 접근하기

i1 = [ 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 ]

print("i1 =",i1)

#9번째 인덱스 이후만 가져오기
print("i1[9:] = ",i1[9:]);

#15번째 인덱스 이전만 가져오기
print("i1[:15] = ",i1[:15]);

#2번째마다의 아이템을 가져오기
print("i1[::2] = ",i1[::2]);

#7번째마다의 아이템을 가져오기
print("i1[::7] = ",i1[::7]);

#5번째부터 시작해서2번째마다 아이템을 가져오기
print("i1[5::2] = ",i1[5::2]);

#17번째 이전까지 매 4번째마다 아이템을 가져오기
print("i1[:17:4] = ",i1[:17:4]);

#7번째부터 시작해서 3번째마다 아이템을 가져오고, 15번째를 전달하지 않기
print("i1[7:15:3 ] = ",i1[7:15:3]);



a_string = "like this"
a_number = 3
a_float = 3.12
a_boolean = False # 첫글자를 대문자로 써줌
a_none = None # null과 비슷함 존재하지 않음

ldays = ["Mon", "Tue", "Wed", "Thur", "Fri"] # list. mutable함 = 변경가능함
# print("Mon" in ldays) # days 안에 Mon이 존재합니까? True of False
# print(ldays[3]) # 해당 인덱스의 값을 가져옴
# print(len(ldays)) # 리스트 길이
ldays.append("Sat") # Sat 추가함
# print(ldays)

tdays = ("Mon", "Tue", "Wed", "Thur", "Fri") # tuple. imutable함

nico = { # dictionary
    "name": "Nico",
    "age": 29,
    "korean": True,
    "fav_food": ["Kimchi","Sashimi"]
}
# print(nico)
# print(nico["fav_food"])
nico["handsome"] = True # dictionary에 추가함



def say_hello(who, wha): # python은 body를 {}가 아닌 들여쓰기로 구분함.
    print("hello", who)
    print("bye", wha)
    print(who+ " and " + wha)
    
say_hello("Nicolas", "YY")

def plus(a, b=0): # b 인자가 없을 경우에는 0으로 대체한다. default value
    print(a + b)
    return a + b
    # return 이후 function은 종료되기 때문에 아래 어떤 코드가 있어도 실행이 안됨.

plus(2)
print(plus(5, 8))

result = plus(b=30, a=5) # arguments의 위치가 아닌 arguments 이름으로 정해지는것 >> 인자가 많을때 헷갈리지 않게해주므로 유용
print(result)

def say_helloo(name, age):
    return f"Hello {name} you are {age} years old"

# helloo=say_helloo("nico", "12")
helloo=say_helloo(age="12", name="nico")
print(helloo)
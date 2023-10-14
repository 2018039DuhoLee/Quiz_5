#붕어빵 먹고싶다~~~
class fish_bread:
    def __init__(self,name,price):
        self.name= name
        self.price= price
        self.sales_quantity = 0  # 인스턴스 변수로 판매량을 저장
    def sell(self):
        print(self.name+ "이" +str(self.price)+ "원으로 판매되었습니다.") #가격은 숫자라 + 를 사용하려면 문자열로 바꿔야함
        self.sales_quantity += 1  # 판매 메서드 호출 시 판매량을 1 증가
    def eat(self):
        print(str(self.price)+ "원 에 " +self.name+ "을 먹었습니다.") #가격은 숫자라 + 를 사용하려면 문자열로 바꿔야함
    def get_sales_quantity(self):
        return self.sales_quantity  # 판매량을 반환하는 메서드

# 붕어빵의 종류와 가격
original = fish_bread("팥", 2000)  #팥이랑 가격을 정의
sucream = fish_bread("슈크림", 2500) #슈크림이랑 가격을 정의

#판매하는 붕어빵
original.sell()
sucream.sell()
sucream.sell()

#먹는 붕어빵
sucream.eat()
original.eat()

#붕어빵의 총 판매량
print(str(original.name)+"의 총 판매량:" + str(original.get_sales_quantity()) + "개")
print(str(sucream.name)+ "의 총 판매량:" + str(sucream.get_sales_quantity())+"개")


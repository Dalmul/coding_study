from abc import ABC, abstractmethod # 추상 클래스, 추상 메메소드 정의

class Person(ABC):
    def __init__(self, name, age, job=None):
        self.name = name
        self.__age = age
        self.job = job

    @abstractmethod
    def introduce(self):
        pass

    # 최초 지정한 인스턴스 변수의 값을 사용한다.         
    def _hello(self):  # _ 언더바 1개 : 상속시 사용가능한 함수(protected 함수)임을 
        # self.name = name
        print(f"hello, I'm {self.name}, {self.__age} years old.")

    # 매개변수를 지정하지 않으면 인스턴스 변수의 값을 사용한다.
    def update_age(self, age=None):
        if age is None:
            age = self.age
        else:
            self.age = age
        
        if age < 0:
            raise ValueError('나이는 음수일 수 없습니다')
        else: 
            print(f"Now I'm {self.age} years old!")
        # self.age = age


# if __name__ == '__main__': # 파일이 직접 실행될 때만 동작한다
#     man = Person('subin', 25) # 인스턴스(클래스를 바탕으로 만들어진 구체적인 객체) 생성
#     man.hello()
#     man.update_age(38) # 인스턴스 실행
# 추상 클래스화 함 250403
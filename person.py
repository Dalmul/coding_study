class Person:
    def __init__(self, name, age, job=None):
        self.name = name
        self.age = age
        self.job = job

    # 최초 지정한 인스턴스 변수의 값을 사용한다.            
    def hello(self): 
        # self.name = name
        print(f"hello, I'm {self.name}.")

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


if __name__ == '__main__': # 파일이 직접 실행될 때만 동작한다
    man = Person('subin', 25) # 인스턴스(클래스를 바탕으로 만들어진 구체적인 객체) 생성
    man.hello()
    man.update_age(38) # 인스턴스 실행
"""
python 파일을 실행시킬 때 인자를 즉석으로 주되, 
인자값을 입력하지 않아도 Default 값을 반환하여 실행시킬 수 있다
"""


import argparse  # sys 대신 argparse 사용

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
                
    def hello(self): 
        print(f"hello, I'm {self.name}.")

    def update_age(self, age):
        self.age = age
        if age < 0:
            raise ValueError('나이는 음수일 수 없습니다')
        else: 
            print(f"Now I'm {self.age} years old!")

if __name__ == '__main__':
    # ArgumentParser 객체 생성
    parser = argparse.ArgumentParser(description='Person 클래스 실행')
    
    # 인자 추가 (기본값 설정)
    parser.add_argument('--name', default='subin', help='이름을 입력하세요 (기본값: John)')
    parser.add_argument('--age', type=int, default=25, help='나이를 입력하세요 (기본값: 25)')
    
    # 인자 파싱
    args = parser.parse_args()
    
    # 인스턴스 생성 및 메서드 실행
    man = person(args.name, args.age)
    man.hello()
    man.update_age(args.age)

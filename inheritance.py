class A:
    def method(self):
        print('i am A')

class B(A):
    def method(self):
        print('i am B')

class C(A):
    def method(self):
        print('i am C')

class D(B, C):
    pass


d = D() # 다중상속 실행시 먼저 상속받은 클래스를 실행
d.method()
print(D.mro()) # 클래스 상속 순서 확인 (클래스 내 기능 확인 시 사용)
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# 순서대로 해당 내용 (d.method() 가 있는지 확인, class 'object'까지 찾았을 때 없을 시 오류 발생)
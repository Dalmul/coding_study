from programmer import Programmer
from actor import Actor
from farmer import Farmer

# dave = Programmer("Dave", 30, "Python")
# dave.introduce()

# song = Actor("Song", 55, "Parasite")
# song.introduce()

# kim = Farmer("Kim", 40, "Apple")
# song.introduce()

"""다형성 예시"""
# people = [
#     Programmer("Dave", 30, "Python"),
#     Actor("Song", 55, "Parasite"),
# #     Farmer("Kim", 40, "Apple")
# # ]

# for person in people :
#     person.introduce()

dave = Programmer("Dave", 30, "Python")
dave.__age = -1 # private 변수 접근 시도, 멤버 변수 외부에서 접근 불가(언더바 2개)
dave._hello()
from person import Person

class Farmer(Person):
    def __init__(self, name, age, fruit):
        super().__init__(name, age, job="Farmer")
        self.fruit = fruit

    # introduce 메소드 재정의 (추상 메소드로 정의 되어있기 때문)
    def introduce(self):
        super()._introduce()
        print(f"나는 {self.fruit} 농장을 하고 있습니다.")

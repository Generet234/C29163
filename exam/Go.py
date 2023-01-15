from main import Person
from Act import Action
import random
human1 = Person(name='Тарас', money=100, mood=100, health=100)
human2 = Person(name='Богдан', money=100, mood=100, health=100)
human3 = Person(name='Иван', money=100, mood=100, health=100)
go_to_park = Action(name='Сходить в парк', money=0, mood=15, health=3)
human1.do(go_to_park)
human2.do(go_to_park)
human3.do(go_to_park)

while True:
    m=0
    try:
        human1.change_state(money=random.randint(70, 100), mood=random.randint(-20, -5), health=random.randint(-10, -5))
    except:
        m = m+1
    try:
        human2.change_state(money=random.randint(60, 100), mood=random.randint(-25, -15),health=random.randint(-17, -4))
    except:
        m = m + 1
    try:
        human3.change_state(money=random.randint(50, 100), mood=random.randint(-30, -20),health=random.randint(-15, -2))
    except:
        m = m + 1
    if m == 3:
        break
print(human1)
print(human2)
print(human3)

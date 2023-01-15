
class OutOfHealth(Exception):
    def __init__(self, message='У человека нету здоровья,он умер'):
        Exception.__init__(self, message)
class OutOfMoney(Exception):
    def __init__(self, message='У человека нету денег,он банкрот'):
        Exception.__init__(self, message)
class OutOfMood(Exception):
    def __init__(self, message='У человека нету настроения,развеселите его'):
        Exception.__init__(self, message)
class Person:
    name = ""
    health = 100
    mood = 100
    money = 100

    def __init__(self,name,health=0,mood = 0 , money=0):
        self.health = health
        self.mood = mood
        self.money = money
        self.name = name

    def __str__(self):
        return f' == {self.name} ==\n' \
               f' Здоровье: {self.health}\n' \
               f' Настроение: {self.mood}\n' \
               f' Количество денег: {self.money}\n'
    def change_state(self,mood=0,health=0,money=0):
        self.health += health
        self.mood += mood
        self.money += money

        if self.mood <0:
            raise OutOfMood
        if self.money<0:
            raise OutOfMoney
        if self.health<0:
            raise OutOfHealth












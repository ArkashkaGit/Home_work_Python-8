"""
Задание 2.
1. Реализовать проект расчета суммарного расхода ткани на производство одежды.
2. Единственный класс этого проекта — одежда (класс Clothes).
3. К типам одежды в этом проекте относятся пальто и костюм.
4. У этих типов одежды существуют параметры:
a) размер (для пальто) и рост (для костюма). Это могут быть обычные числа: v и h, соответственно.
b) Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (v/6.5 + 0.5),
для костюма (2*h + 0.3).
c) Проверить работу этих методов на реальных данных.
d) Реализовать общий подсчет расхода ткани.

5. Проверить на практике полученные на этом уроке знания:
a) реализовать абстрактный класс для единственного класса проекта,
b) проверить на практике работу декоратора @property

Пример:
Расход ткани на пальто = 1.27
Расход ткани на костюм = 20.30
Общий расход ткани = 21.57
Два класса: абстрактный и Clothes
"""

from abc import ABC, abstractmethod

class Abstract_clothes(ABC):
    def __init__(self, v, h):
        self.v = v
        self.h = h

# Пальто
    @abstractmethod
    def coat(self):
        global coat_expend
        coat_expend = self.v / 6.5 + 0.5
        return coat_expend

# Костюм
    @abstractmethod
    def suit(self):
        global suit_expend
        suit_expend = 2 * self.h + 0.3
        return suit_expend

# Суммарный расход
    @abstractmethod
    def summa_clothes(self):
        summa_expend = coat_expend + suit_expend
        return summa_expend

class Clothes(Abstract_clothes):
    def __init__(self, v, h):
        super().__init__(v,h)

    @property
    def coat(self):
        global coat_expend
        coat_expend = self.v / 6.5 + 0.5
        print(f'{coat_expend} потребуется ткани для польто')
    @property

    def suit(self):
        global suit_expend
        suit_expend = 2 * self.h + 0.3
        print(f'{suit_expend} потребуется ткани для костюма')

    @property
    def summa_clothes(self):
        summa_expend = coat_expend + suit_expend
        print(f'{summa_expend} потребуется ткани для костюма и польто')

abs = Clothes(30,40)
abs.coat
abs.suit
abs.summa_clothes
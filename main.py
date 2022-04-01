import random
import time
class Student:
    def __init__(self, name):
        self.name = name
        self.happines = 50
        self.progress = 0
        self.alive = True
        self.money = 100
        self.found_work = False
    def to_study(self):
        print("Тужимося..")
        self.progress += 0.12
        self.happines -= 3
    def sleep(self):
        print("дрихну))")
        self.happines += 3
    def find_work(self):
        if self.found_work = False:
            print("Ти шукаєш роботу..")
            time.sleep(0.10)
            print("Пошук роботи: 0%")
            print("Перша робота: Прибиральник")
            time.sleep(1)
            print("Думаю, можна знайти ліпше.")
            time.sleep(0.10)
            print("Пошук роботи: 10%")
            time.sleep(0.30)
            print("Пошук роботи: 25%")
            time.sleep(1)
            print("Друга робота: Адвокат.")
            time.sleep(0.30)
            print("Непогано, але ще можна пошукати.")
            time.sleep(0.20)
            print("Пошук роботи: 40%")
            time.sleep(0.10)
            print("Пошук роботи: 65%")
            time.sleep(0.10)
            print("Пошук роботи: 75%")
            time.sleep(1)
            print("Третя робота: Завод")
            time.sleep(0.20)
            print(". . .")
            time.sleep(2)
            print("Адвокат теж непогано.")
            time.sleep(0.10)
            print("Пошук роботи: 100% (закінчено через скасування)")
            self.found_work = True
        else:
            print("Ти вже маєш роботу!")
    def work(self):
        print("Ти вирішив почати працювати..")
        time.sleep(0.50)
        print("Ти зайшов на робочий сайт, почав шукати замовлення.")
        time.sleep(0.10)
        print("Пошук справи: 0%")
        time.sleep(0.10)
        print("Пошук справи: 10%")
        time.sleep(0.10)
        print("Пошук справи: 15%")
        time.sleep(0.10)
        print("Пошук справи: 25%")
        time.sleep(0.10)
        print("Пошук справи: 40%")
        time.sleep(0.10)
        print("Пошук справи: 50%")
        time.sleep(0.10)
        print("Пошук справи: 65%")
        time.sleep(0.30)
        rand1 = random.randint(1, 3)
        if rand1 == 1:
            print("Справа: Бандера бомбив бомбас")
            print("Загроза: Розстріл")
            time.sleep(0.15)
            print("Ваша задача: не дати Бандері вмерти!!")
            time.sleep(1)
            print("Ти пробуєш сказати шо Бандера не обязан")
            rand2 = random.randint(1, 2)
            if rand2 == 1:
                print("Перший етап пройшов успішно, продовжуємо далі.")
                time.sleep(1)
                print("Ше трохи, ти пробуєш доказати судді що відео це фотошоп")
                time.sleep(2)
                print("ВІТАЮ!!! БАНДЕРА СВОБІДНИЙ!!")
                self.money += 25
            elif rand2 == 2:
                print("Перший етап пройшов як по паштету.., пробуємо дати ")
                time.sleep(2)
                print("ВЗЯТКУ.")
                time.sleep(3)
                rand3 = random.randint(1, 2)
                if rand3 == 1:
                    print("В тебе получилось підкупити суддю! Ти втратив 25 грн, але виграв 15. Ти в боргу на 10 грн.")
                    self.money -= 25
                    self.money += 15
                elif rand3 == 2:
                    print("Суддя відмовився, і тебе затримали.")
                    time.sleep(2)
                    print("Ти не витримав булінгу і вийшов з світу (осуждаю!)")
                    self.is_alive == False
        elif rand1 == 2:
            print("Справа: Стерненко кікнув з світу нападника")
            print("Загроза: 7 років")
            time.sleep(0.15)
            print("Ваша задача: Не дати імператору правого сектору сісти!!!")
            time.sleep(1)
            print("Ця справа легко дається..")
            time.sleep(1)
            print("Вітаю! Ти лакі. (виграв справу)")
            time.sleep(1)
            print("Ти заробив 50 грн.")
            self.money += 50
        elif rand1 == 3:
            print("Справа: Мужик вкрав снікерс з заправки")
            print("Ваша задача: Не.. Я навіть не знаю чого тут треба добитись..")
            time.sleep(3)
            print(". . .")
            time.sleep(0.50)
            print("ВЯЖІТЬ ЙОГО!!!")
            time.sleep(0.50)
            print("ТОБІ ДАЛИ БЕЗРОБІТНЄ ЖИТТЯ!")
            time.sleep(0.10)
            print("ТИ ЗАРОБИВ 100000 ГРН!!!")
            self.money += 100000



    def to_chill(self):
        print("На раслаблонє")
        self.happines += 5
        self.progress -= 0.5
    def is_alive(self):
        if self.progress < -0.5:
            print("БАН")
            self.alive = False
        elif self.happines <= 0:
            print("ol mai frends ar toksik")
            self.alive = False
        if self.progress > 5:
            print("год мод???")
            self.happines = 1000000
            time.sleep(1)
            print(".. але ти здох..")
            self.alive = False
    def stats(self):
        print("Статистика студента:")
        print("Рівень щастя: " + self.happines)
        print("Рівень успішності: " + round(self.progress, 2))
    def live(self, day):
        print("День: " + day + " Ім'я студента: " + self.name)
        rand = random.randint(1, 3)
        if rand == 1:
            self.to_study()
        elif rand == 2:
            self.sleep()
        elif rand == 3:
            self.to_chill()
        self.stats()
        self.is_alive()

        if self.money <= 0:
            print("Йди працюй, бомжара!")
            time.sleep(0.50)
            print("1. Ну ладно( ")
            print("2. Ні! Я живу в свобідній країні!")
            e = input("Ваша відповідь(1/2): ")
            if e == 1:
                Student.work(self)
            elif e == 2:
                print("НУ ТОДІ ПРИЙМИ СМЕРТЬ ГІДНО!")
                self.is_alive == False


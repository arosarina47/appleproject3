from PyQt5.QtWidgets import QApplication
from random import choice , shuffle
from time import sleep
app = QApplication([])

from m2 import*
from m3 import*

class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q1 = Question('Який місяць року має 28 днів' , "Всі" , "Березень" , "Лютий" , "Червень")
q2 = Question('Що можна побачити із закртими очима?' , "Сни" , "Нічого" , "Темряву" , "Себе")
q3 = Question('Що не жує,але все пожирає?' , "Вогонь" , "Кіт" , "Корова" , "Пітьма")
q4 = Question('Не махає крилом,але літає, не птах,але птахів обганяє' , "Літак" , "Муха" , "Вертоліт" , "Дракон")
q5 = Question('Хто в небі народився і в землі поховався?' , 'Дощ' , "Птах" , "Комар" , "Вітер")
q6 = Question('Електропоїзд йде за вітром,куди йде дим?' , 'У електропоїзда немає диму' , "Вверх " , "В низ" , "В право")
q7 = Question('З якого посуду не можна нічого їсти?' , 'З пустого' , "З розбитого" , "З дерев'яного" , "З керамічного")
q8 = Question('Скільки горошин може увійти в один стакан?' , '0,горошини не ходять' , "10" , "50" , "100")
q9 = Question('Що стане більшим,якщо його перевернути догори ногами' , 'число 6' , "Пісочний годинник" , "Число 9" , "Вітер")
q10 = Question('Що кидають ,коли потребують цього , і піднімають,коли в цьому немає потреби?' , 'Морський якір' , "Друзів" , "М'яч " , "Гроші")
def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)
def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu())
window.show()
app.exec_()

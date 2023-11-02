def summer(NumberN):
    Number0 = ('{0:0>12}'.format(NumberN))
    Number = Number0[::-1]

    # Определяем однозначное
    order0 = int((Number[0]))
    test0 = {
        1: "один",
        2: "два",
        3: "три",
        4: "четыре",
        5: "пять",
        6: "шесть",
        7: "семь",
        8: "восемь",
        9: "девять",
        0: ""
    }

    # Определяем двузначное
    order1 = int((Number[1]))
    test1 = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        0: ""
    }

    # первая цифра в "11 12 13 14 15 16 17 18 19"
    if order1 == 1:
        test11 = {
            1: "надцать"
        }
        two = (test11[order1])

        # вторая цифра в "11 12 13 14 15 16 17 18 19"
        order0 = int((Number[0]))
        test12 = {
            1: "один",
            2: "две",
            3: "три",
            4: "четыр",
            5: "пят",
            6: "шест",
            7: "сем",
            8: "восем",
            9: "девят",
            0: "десять"
        }
        one = ((test12[order0]))

    else:
        two = (test1[order1])
        one = (test0[order0])

    # Даем значение однозначному и двузначному в одной переменной А #
    if order1 == 1:
        if order0 == 0:
            A = (str(one))
        else:
            A = (str(one) + str(two))
    else:
        A = (str(two + " ") + str(one))

    # Определяем трехзначное
    order2 = int((Number[2]))
    test2 = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
        0: ""
    }
    B = (test2[order2])

    # Определяем четырехзначное

    order3 = int((Number[3]))
    test3 = {
        1: "одна тысяча",
        2: "две тысячи",
        3: "три тысячи",
        4: "четыре тысячи",
        5: "пять тысяч",
        6: "шесть тысяч",
        7: "семь тысяч",
        8: "восемь тысяч",
        9: "девять тысяч",
        0: ""
    }

    # Определяем пятизначное

    order4 = int((Number[4]))
    test4 = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        0: ""
    }

    # первая цифра в "11 12 13 14 15 16 17 18 19"
    if order4 == 1:
        test11 = {
            1: "надцать тысяч"
        }
        five = (test11[order4])

        # вторая цифра в "11 12 13 14 15 16 17 18 19"
        order3 = int((Number[3]))
        test22 = {
            1: "один",
            2: "две",
            3: "три",
            4: "четыр",
            5: "пят",
            6: "шест",
            7: "сем",
            8: "восем",
            9: "девят",
            0: "десять"
        }
        four = ((test22[order3]))

    else:
        five = (test4[order4])
        four = (test3[order3])

    if order4 == 1:
        if order3 == 0:
            C = (str(four))
        else:
            C = (str(four) + str(five))
    else:
        C = (str(five + " ") + str(four))

    # Определяем шестизначное
    order5 = int((Number[5]))
    test5 = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
        0: ""
    }
    D = (test5[order5])

    # Определяем семизначное

    order6 = int((Number[6]))
    test6 = {
        1: "один миллион",
        2: "два миллиона",
        3: "три миллиона",
        4: "четыре миллиона",
        5: "пять миллионов",
        6: "шесть миллионов",
        7: "семь миллионов",
        8: "восемь миллионов",
        9: "девять миллионов",
        0: ""
    }

    # Определяем восьмизначное

    order7 = int((Number[7]))
    test7 = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        0: ""
    }

    # первая цифра в "11 12 13 14 15 16 17 18 19"
    if order7 == 1:
        test31 = {
            1: "надцать миллионов"
        }
        seven = (test31[order7])

        # вторая цифра в "11 12 13 14 15 16 17 18 19"
        order6 = int((Number[6]))
        test32 = {
            1: "один",
            2: "две",
            3: "три",
            4: "четыр",
            5: "пят",
            6: "шест",
            7: "сем",
            8: "восем",
            9: "девят",
            0: "десять"
        }
        six = ((test32[order6]))

    else:
        seven = (test7[order7])
        six = (test6[order6])

    # Создаем переменную Е в которой будет содераться значение десятков и единиц миллиона
    if order7 == 1:
        if order6 == 0:
            E = (str(six))
        else:
            E = (str(six) + str(seven))
    else:
        E = (str(seven + " ") + str(six))

    # Определяем вомьмизначное
    order8 = int((Number[8]))
    test8 = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
        0: ""
    }
    F = (test8[order8])

    # Определяем семизначное

    order9 = int((Number[9]))
    test9 = {
        1: "один миллиард",
        2: "два миллиарда",
        3: "три миллиарда",
        4: "четыре миллиарда",
        5: "пять миллиардов",
        6: "шесть миллиардов",
        7: "семь миллиардов",
        8: "восемь миллиардов",
        9: "девять миллиардов",
        0: ""
    }

    # Определяем миллиардное

    order11 = int((Number[10]))
    test11 = {
        2: "двадцать",
        3: "тридцать",
        4: "сорок",
        5: "пятьдесят",
        6: "шестьдесят",
        7: "семьдесят",
        8: "восемьдесят",
        9: "девяносто",
        0: ""
    }

    # первая цифра в "11 12 13 14 15 16 17 18 19"
    if order11 == 1:
        test41 = {
            1: "надцать миллиардов"
        }
        nine = (test41[order11])

        # вторая цифра в "11 12 13 14 15 16 17 18 19"
        order9 = int((Number[9]))
        test42 = {
            1: "один",
            2: "две",
            3: "три",
            4: "четыр",
            5: "пят",
            6: "шест",
            7: "сем",
            8: "восем",
            9: "девят",
            0: "десять"
        }
        eight = ((test42[order9]))

    else:
        nine = (test11[order11])
        eight = (test9[order9])

    # Создаем переменную Е в которой будет содераться значение десятков и единиц миллиона
    if order11 == 1:
        if order9 == 0:
            G = (str(eight))
        else:
            G = (str(eight) + str(nine))
    else:
        G = (str(nine + " ") + str(eight))

    # Определяем вомьмизначное
    order12 = int((Number[11]))
    test12 = {
        1: "сто",
        2: "двести",
        3: "триста",
        4: "четыреста",
        5: "пятьсот",
        6: "шестьсот",
        7: "семьсот",
        8: "восемьсот",
        9: "девятьсот",
        0: ""
    }
    H = (test12[order12])

    # К 20, 30... 90 миллионам и тысячам дописываем обозначение
    if order3 == 0 and order4 > 0:
        C1 = (C + "тысяч")
    else:
        C1 = C

    if order6 == 0 and order7 > 0:
        E1 = (E + "миллионов")
    else:
        E1 = E

    if order9 == 0 and order11 > 0:
        G1 = (G + "миллиардов")
    else:
        G1 = G

    # Выводим результат

    return(H + " " + G1 + " " + F + " " + E1 + " " + D + " " + C1 + " " + B + " " + A)


from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
Config.set('graphics', 'resizable', '0');
Config.set('graphics', 'width', '400');
Config.set('graphics', 'height', '500');


class MyApp(App):
    def update_label(self):
        self.lbl.text = self.formula
    def add_number(self, instance):
        if( self.formula == '0'):
            self.formula = ""
        self.formula += str(instance.text)
        self.update_label()

    def add_del(self, instance):
        self.formula = "0"
        self.update_label()

    def calc_result(self, instance):
        self.lbl.text = str(summer(self.lbl.text))

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation = 'vertical', padding = [10],)

        self.lbl = (Label(text='0',
                          font_size = 25,
                          halign = 'right',
                          size_hint = (1, .4),
                          text_size = (380, 170)))
        bl.add_widget(self.lbl)


        gl = GridLayout(cols=3, spacing=3, size_hint=(1, .6))

        gl.add_widget(Button(text='7', on_press = self.add_number))
        gl.add_widget(Button(text='8', on_press = self.add_number))
        gl.add_widget(Button(text='9', on_press = self.add_number))

        gl.add_widget(Button(text='4', on_press = self.add_number))
        gl.add_widget(Button(text='5', on_press = self.add_number))
        gl.add_widget(Button(text='6', on_press = self.add_number))

        gl.add_widget(Button(text='1', on_press = self.add_number))
        gl.add_widget(Button(text='2', on_press = self.add_number))
        gl.add_widget(Button(text='3', on_press = self.add_number))

        gl.add_widget(Button(text='C',on_press = self.add_del,
                             font_size = 17))
        gl.add_widget(Button(text='0', on_press = self.add_number))
        gl.add_widget(Button(text='=', on_press = self.calc_result,
                             font_size = 26))

        bl.add_widget(gl)

        return bl

if __name__ == "__main__":
    MyApp().run()
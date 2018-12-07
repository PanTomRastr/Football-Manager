import requests, bs4
import re
import playsound

lst = ['авангард', 'уфа', 'анжи', 'ангушт', 'мордовия', 'cпартаквладикавказ', 'рубин', 'камаз', 'нефтехимик', 'ахмат',
       'динамо', 'краснодар', 'сочи', 'черноморец', 'енисей', 'звезда', 'салют',
       'торпедо', 'муром', 'ротор', 'Факел', 'балтика', 'калуга', 'ленинградец',
       'металлург', 'химки', 'коломна', 'знамятруда', 'долгопрудный', 'сатурн', 'химким', 'нижнийновгород',
       'сибирь', 'оренбург', 'псков', 'лукиэнергия', 'ростов', 'ска', 'крыльясоветов', 'сокол', 'урал'
         'днепр', 'томь', 'арсенал', 'шинник', 'цска', 'спартак', 'локомотив', 'чертаново', 'торпедо',
       'казанка', 'велес', 'чертаново', 'строгино', 'зенит']


def football_box(url):
    s = requests.get(url)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    p4 = b.select('.championship')
    football_game = b.select(' .tab-row-green')
    team1 = b.select('.tour')[0].getText()
    team2 = b.select('.tour')[1].getText()

    for i in range(len(p4[0].getText())):
        if p4[0].getText()[i] == 'З':
            lst1 = p4[0].getText()[:i]
            break
    for i in range(len(p4[1].getText())):
        if p4[1].getText()[i] == 'З':
            lst2 = p4[1].getText()[:i]
            break

    lst_box = []
    lst_team1 = []
    lst_team2 = []
    lst_lst1 = []
    lst_lst2 = []
    last = 0
    for i in range(1, len(lst1)):
        if ord(lst1[i]) == ord('М') or ord(lst1[i]) == ord('Н') or ord(lst1[i]) == ord('П'):
            lst_lst1.append(lst1[last:i])
            last = i
    lst_lst1.append(lst1[last:])
    last = 0
    for i in range(1, len(lst2)):
        if ord(lst2[i]) == ord('М') or ord(lst2[i]) == ord('Н') or ord(lst2[i]) == ord('П'):
            l = lst2[last:i]
            lst_lst2.append(lst2[last:i])
            last = i
    lst_lst2.append(lst2[last:])
    reg = re.compile('[^0-9 ]')
    for i in range(len(lst_lst1)):
        lst_lst1[i] = reg.sub('', lst_lst1[i])

    if len(lst_lst1) == 5:
        del lst_lst1[0]

    for i in range(len(lst_lst2)):
        lst_lst2[i] = reg.sub('', lst_lst2[i])

    if len(lst_lst2) == 5:
        del lst_lst2[0]

    lst_team1.append(team1)
    lst_team1.append(lst_lst1)
    lst_team2.append(team2)
    lst_team2.append(lst_lst2)
    lst_box.append(lst_team1)
    lst_box.append(lst_team2)
    lst_com = []
    last = 0
    s = p4[2].getText()
    for i in range(1, len(s)):
        if s[i] == 'Ч':
            lst_com.append(s[last:i])
            last = i
    lst_box.append(lst_com)
    return lst_box

#print(football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Zenit_St_Petersburg/club2/RUS_Baltika_Kaliningrad'))

def distance(a, b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


def proverka(slovo, lenght):
    lst_digit = []
    for i in lst:
        if lenght <= (len(slovo) - distance(slovo, i)) / len(slovo):
            lst_digit.append(i)
            return lst_digit
    return lst_digit

def chek(s):
    if len(s) < 2:
        return s
    reg = re.compile('[^а-яА-Я ]')
    for i in range(len(s)):
        s[i] = s[i].lower()
        s[i] = reg.sub('', s[i])
    i = 0
    while i < len(s):
        if len(s[i]) == 0:
            del s[i]
        else:
            i += 1
    if len(s) < 2:
        return s
    team1 = proverka(s[0], 0.6)
    team2 = proverka(s[1], 0.6)
    myString1 = ' '.join(team1)
    myString2 = ' '.join(team2)
    lst = []
    lst.append(myString1)
    lst.append(myString2)
    return lst


def sait(lst1, lst2):
    if (lst1 == 'авангард' and lst2 == 'анжи') or (lst2 == 'авангард' and lst1 == 'анжи'):
        return football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Anzhi_Makhachkala')

    if (lst1 == 'авангард' and lst2 == 'cпартак-владикавказ') or (lst2 == 'авангард' and lst1 == 'cпартак-владикавказ'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Spartak_Shchelkovo')

    if (lst1 == 'авангард' and lst2 == 'динамо') or (lst2 == 'авангард' and lst1 == 'динамо'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Dynamo-2_Moskva')

    if (lst1 == 'авангард' and lst2 == 'краснодар') or (lst2 == 'авангард' and lst1 == 'краснодар'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Krasnogvardeyets_Moskva')

    if (lst1 == 'авангард' and lst2 == 'салют') or (lst2 == 'авангард' and lst1 == 'салют'):
        return football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Salyut_Belgorod')

    if (lst1 == 'авангард' and lst2 == 'торпедо') or (lst2 == 'авангард' and lst1 == 'торпедо'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Torpedo_Taganrog')

    if (lst1 == 'авангард' and lst2 == 'Факел') or (lst2 == 'авангард' and lst1 == 'Факел'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Fakel_Voronezh')

    if (lst1 == 'авангард' and lst2 == 'металлург') or (lst2 == 'авангард' and lst1 == 'металлург'):
        return football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Metallurg_Lipetsk')

    if (lst1 == 'авангард' and lst2 == 'сатурн') or (lst2 == 'авангард' and lst1 == 'сатурн'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Saturn_Moskovskaya_Oblast')

    if (lst1 == 'авангард' and lst2 == 'ска') or (lst2 == 'авангард' and lst1 == 'ска'):
        return football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_ASK_Rostov-on-Don')

    if (lst1 == 'авангард' and lst2 == 'цска') or (lst2 == 'авангард' and lst1 == 'цска'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_CSKA-D_Moskva')

    if (lst1 == 'авангард' and lst2 == 'спартак') or (lst2 == 'авангард' and lst1 == 'спартак'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Spartak_Shchelkovo')

    if (lst1 == 'авангард' and lst2 == 'локомотив') or (lst2 == 'авангард' and lst1 == 'локомотив'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Lokomotiv_St_Petersburg')

    if (lst1 == 'авангард' and lst2 == 'торпедо') or (lst2 == 'авангард' and lst1 == 'торпедо'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Avangard_Kolomna/club2/RUS_Torpedo_Taganrog')

    if (lst1 == 'уфа' and lst2 == 'анжи') or (lst2 == 'уфа' and lst1 == 'анжи'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Bashinformsvyaz-Dinamo_Ufa/club2/RUS_Anzhi_Makhachkala')

    if (lst1 == 'уфа' and lst2 == 'анжи') or (lst2 == 'уфа' and lst1 == 'анжи'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Bashinformsvyaz-Dinamo_Ufa/club2/RUS_Anzhi_Makhachkala')

    if (lst1 == 'уфа' and lst2 == 'ангушт') or (lst2 == 'уфа' and lst1 == 'ангушт'):
        return football_box('http://wildstat.ru/p/60/ch/all/club1/RUS_Bashinformsvyaz-Dinamo_Ufa/club2/RUS_Angusht-2_Nazran')

    if (lst1 == 'уфа' and lst2 == 'мордовия') or (lst2 == 'уфа' and lst1 == 'мордовия'):
        return football_box(
            'http://wildstat.ru/p/60/ch/all/club1/RUS_Bashinformsvyaz-Dinamo_Ufa/club2/RUS_Mordovia_Saransk')

    if (lst1 == 'уфа' and lst2 == 'спартак') or (lst2 == 'уфа' and lst1 == 'спартак'):
        return football_box(
            'http://wildstat.ru/p/60/ch/all/club1/RUS_Bashinformsvyaz-Dinamo_Ufa/club2/RUS_Spartak_Moskva')

    if (lst1 == 'зенит' and lst2 == 'авангард') or (lst2 == 'зенит' and lst1 == 'авангард'):
        return football_box(
            'http://wildstat.ru/p/60/ch/all/club1/RUS_Zenit_St_Petersburg/club2/RUS_Avangard_Kamyshin')


    if (lst1 == 'зенит' and lst2 == 'анжи') or (lst2 == 'зенит' and lst1 == 'анжи'):
        return football_box(
            'http://wildstat.ru/p/60/ch/all/club1/RUS_Zenit_St_Petersburg/club2/RUS_Anzhi_Makhachkala')

    if (lst1 == 'зенит' and lst2 == 'локомотив') or (lst2 == 'зенит' and lst1 == 'локомотив'):
        return football_box(
            'http://wildstat.ru/p/60/ch/all/club1/RUS_Zenit_St_Petersburg/club2/RUS_Lokomotiv_Moskva')

    if (lst1 == 'зенит' and lst2 == 'балтика') or (lst1 == 'балтика' and lst2 == 'зенит'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Zenit_St_Petersburg/club2/RUS_Baltika_Kaliningrad')


    if (lst1 == 'салют' and lst2 == 'cпартаквладикавказ') or (lst1 == 'салют' and lst2 == 'cпартаквладикавказ'):
        return  football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_FC_Spartak_Vladikavkaz/club2/RUS_Salyut_Belgorod')

    return 'Нету комманд'


def open_game_now(year):
    s = requests.get(year)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    global1 = b.select('.box')
    return global1

def open_game_club(year):
    s = requests.get(year)
    b = bs4.BeautifulSoup(s.text, "html.parser")
    global1 = b.select('.tab-row-green')
    return  global1

def music():
    target = playsound.playsound('file2.mp3', True)


'''''
lst = ['авангард', 'уфа', 'анжи', 'ангушт', 'мордовия', 'cпартаквладикавказ', 'рубин', 'камаз', 'нефтехимик', 'ахмат',
       'динамо', 'краснодар', 'сочи', 'черноморец', 'енисей', 'звезда', 'салют',
       'торпедо', 'муром', 'ротор', 'Факел', 'балтика', 'калуга', 'ленинградец',
       'металлург', 'химки', 'коломна', 'знамятруда', 'долгопрудный', 'сатурн', 'химким', 'нижнийновгород',
       'сибирь', 'оренбург', 'псков', 'лукиэнергия', 'ростов', 'ска', 'крыльясоветов', 'сокол', 'урал'
         'днепр', 'томь', 'арсенал', 'шинник', 'цска', 'спартак', 'локомотив', 'чертаново', 'торпедо',
       'казанка', 'велес', 'чертаново', 'строгино', 'зенит']
'''
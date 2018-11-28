import requests, bs4

lst = ['авангард', 'уфа', 'анжи', 'ангушт', 'мордовия', 'cпартак-владикавказ', 'рубин', 'камаз', 'нефтехимик', 'ахмат',
       'динамо', 'краснодар', 'сочи', 'черноморец', 'урожай', 'енисей', 'звезда', 'луч', 'ска-хабаровск', 'салют',
       'торпедо', 'муром', 'ротор-волгоград', 'ротор-2', 'Факел', 'балтика', 'калуга', 'авангард', 'ленинградец',
       'металлург', 'химки', 'коломна', 'Знамя Труда', 'Долгопрудный', 'Сатурн', 'Химки-М', 'нижний новгород',
       'сибирь', 'оренбург', 'псков-747', 'луки-энергия', 'ростов', 'ска', 'крылья советов', 'сокол', 'урал'
       'днепр', 'томь', 'арсенал', 'шинник', 'цска', 'спартак', 'локомотив', 'динамо', 'чертаново', 'спартак-2'
       'торпедо', 'казанка', 'велес', 'чертаново-2', 'строгино', 'зенит']


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
    lst_team1.append(team1)
    lst_team1.append(lst1)
    lst_team2.append(team2)
    lst_team2.append(lst2)
    lst_box.append(lst_team1)
    lst_box.append(lst_team2)
    lst_box.append(p4[2].getText())

    return lst_box


#print(football_box('http://wildstat.ru/p/7001/ch/all/club1/RUS_Terek_Groznyi/club2/RUS_Zenit_St_Petersburg'))


def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
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


#print(proverka('балтека', 0.7))

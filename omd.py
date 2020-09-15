# Guido van Rossum <guido@python.org>

def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print('Утка взяла зонтик и думает куда бы ей отправиться. '
          'Утка хочет либо на Патрики, либо на Чистые Пруды.')
    print('Куда ей пойти?')
    option = ''
    options = {'Патрики': True, 'Чистые': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step3_patriki()
    return step3_chystye()


def step2_no_umbrella():
    print('Пошел дождь и утка осталась дома :(')
    print('Начать заново?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    else:
        print('Игра окончена!')


def step3_patriki():
    print('Утка отправилась на Патриаршие Пруды, '
          'зашла в бар и думает что выпить. '
          'Что ей выпить?')
    option = ''
    options = {'Вино': True, 'Пиво': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return step4_patriki()


def step3_chystye():
    print('Утка пришла в бар на Чистых Прудах и думает, '
          'что бы ей выпить. Поможете с выбором?')
    option = ''
    options = {'Вино': True, 'Виски-кола': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return step4_chystye()


def step4_patriki():
    print('Утка напилась и вышла гулять, '
          'где ею бесщадно отобедал кот Бегемот.')
    print('Начать заново?')
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step1()
    else:
        print('Игра окончена!')


def step4_chystye():
    print('Утка явно перебрала и отправилась к своим друзьям, '
          'которые в это время плавали в пруду.'
          '\nВместе они думают, куда улететь из этой '
          'серой и ненавистной им Москвы. '
          'Куда им улететь?')
    option = ''
    options = {'Египет': 1, 'Тунис': 2, 'Крым': 3}
    while option not in options:
        print('Выберите: {}/{}/{}'.format(*options))
        option = input()
    answer = ['Отлично, утка и ее друзья улетели в ', option, '!']
    print(''.join(answer))
    print('Вы победили!')
    print('AVIASALES поможет каждой утке улететь в теплые края. '
          'AVIASALES - поиск дешевых авиабилетов.')
    print('Начать заново?')
    option1 = ''
    options1 = {'да': True, 'нет': False}
    while option1 not in options1:
        print('Выберите: {}/{}'.format(*options1))
        option1 = input()

    if options1[option1]:
        return step1()
    else:
        print('Игра окончена!')


if __name__ == '__main__':
    step1()

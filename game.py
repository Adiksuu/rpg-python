# ZAIMPORTOWANIE MODUŁÓW
import colorama
from colorama import Fore
colorama.init()

from random import randint


# ZDEFINIOWANIE ZMIENNYCH GLOBALNYCH
game_running = True

# ZDEFINIOWANIE ZMIENNYCH POZIOMÓW
level = 1
xp = 0
xp_remain = 100
xp_max = False

# POCZĄTKOWE MENU GRACZA
while game_running == True:


# ZDEFINIOWANIE STATYSTYK
    player = {'name': 'Adiksuu', 'attack': 13, 'heal': 18, 'health': 100}
    monster = {'name': 'BOSS', 'attack_min': 11, 'attack_max': 15, 'health': 200}
    new_round = True

    #SPRAWDZANIE NOWEGO POZIOMU
    if xp_remain <= 0:
        if xp_max == False:
            level = level + 1
            if level == 2:
                xp_remain = 200
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 5
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +5 attack! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 3:
                xp_remain = 300
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 10
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +10 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 4:
                xp_remain = 400
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 15
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +15 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 5:
                xp_remain = 500
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 20
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +20 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 6:
                xp_remain = 600
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 25
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +25 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 7:
                xp_remain = 700
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 30
                player['health'] = player['health'] + 5
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +30 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 8:
                xp_remain = 800
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 35
                player['health'] = player['health'] + 10
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +35 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +10 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 9:
                xp_remain = 900
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 40
                player['health'] = player['health'] + 10
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +40 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +10 hp! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')
            if level == 10:
                xp_remain = 1000
                xp_max = True
                print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
                player['attack'] = player['attack'] + 50
                player['health'] = player['health'] + 15
                print('')
                print('---' * 7)
                print(Fore.BLUE + 'Otrzymujesz +50 attack! ' + Fore.CYAN +
                      'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
                print(Fore.BLUE + 'Otrzymujesz +15 hp! ' + Fore.CYAN + 'Aktualnie posiadasz: ' + str(player['health']) + Fore.RED + ' HP')


    if xp_max == True:
        print(Fore.RED + '---' * 7)
        print(Fore.RED + 'Osiągnąłeś maksymalny poziom!')
        print(Fore.RED + '---' * 7)
        print('')

    if xp_remain <= 0:
        if xp_max == False:
            level = level + 1
            print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
            player['attack'] = player['attack'] + 5
            print('')
            print('---' * 7)
            print(Fore.BLUE + 'Otrzymujesz +5 attack! ' + Fore.CYAN +
                  'Aktualnie posiadasz: ' + str(player['attack']) + Fore.RED + ' ATTACK')
            print('')

    print(Fore.CYAN + '---' * 5)
    player['name'] = input(Fore.BLUE + 'Nazwa gracza: ')

    print('')
    print(Fore.CYAN + '---' * 5)
    print(Fore.LIGHTGREEN_EX + player['name'] + Fore.GREEN + ' Posiada: ' + Fore.LIGHTRED_EX + str(player['health']) + Fore.RED + 'HP')
    print(Fore.LIGHTGREEN_EX + monster['name'] + Fore.GREEN + ' Posiada: ' + Fore.LIGHTRED_EX + str(monster['health']) + Fore.RED + 'HP')

    while new_round == True:

        player_won = False
        monster_won = False

        print('')
        print(Fore.RED + 'Wybierz opcję!')
        print('---' * 5)
        print(Fore.CYAN + '1.' + Fore.LIGHTBLUE_EX + ' Atakuj')
        print(Fore.CYAN + '2.' + Fore.LIGHTBLUE_EX + ' Ulecz')
        print(Fore.CYAN + '3.' + Fore.LIGHTBLUE_EX + ' Wyświetl Statystyki')
        print(Fore.CYAN + '4.' + Fore.LIGHTBLUE_EX + ' Opuść Grę!')

        player_choice = input(Fore.BLUE + 'Wybrana opcja: ' + Fore.CYAN)
        print('') 


        # PO WYBORZE OPCJI
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
                
            else:
                monster_attack = randint(monster['attack_min'], monster['attack_max'])
                player['health'] = player['health'] - monster_attack
                if player['health'] <= 0:
                    monster_won = True

        
        elif player_choice == '2':
            monster_attack = randint(monster['attack_min'], monster['attack_max'])
            if player['health'] < 100:
                player['health'] = player['health'] + player['heal']
                print(Fore.RED + 'Gracz został uleczony!')
                player['health'] = player['health'] - monster_attack
            if player['health'] > 100:
                player['health'] = 100

        elif player_choice == '3':
            print(Fore.LIGHTGREEN_EX + 'Twój poziom: ' + Fore.GREEN + str(level) + ' lvl')
            if xp_max == False:
                print(Fore.LIGHTGREEN_EX + 'Do następnego poziomu brakuje ci: ' + Fore.GREEN + str(xp_remain) + ' xp')
            

        elif player_choice == '4':
            print(Fore.RED + 'Opuszczanie...')
            new_round = False
            game_running = False
    # CO W WYPADKU GDY WYBIERZEMY ZŁĄ OPCJĘ?
        else:
            print('')
            print(Fore.LIGHTRED_EX + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print(Fore.RED + ' ERROR! - Wybrano niepoprawną opcję')
            print(Fore.LIGHTRED_EX + '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    # INFORMACJE O WYGRANYCH
        if player_won == False and monster_won == False:
            print(Fore.MAGENTA + player['name'] + ' Posiada: ' + Fore.LIGHTMAGENTA_EX + Fore.LIGHTRED_EX + str(player['health']) + Fore.RED + ' HP')
            print(Fore.MAGENTA + monster['name'] + ' Posiada: ' + Fore.LIGHTMAGENTA_EX + Fore.LIGHTRED_EX + str(monster['health']) + Fore.RED + ' HP')

        elif player_won == True:
            print(Fore.LIGHTGREEN_EX + player['name'] + Fore.GREEN + ' Wygrywa!')
            new_round = False
            xp_remain = xp_remain - 10


        elif monster_won == True:
            print(Fore.LIGHTGREEN_EX + monster['name'] + Fore.GREEN + ' Wygrywa!')
            new_round = False
            xp_remain = xp_remain - 1
        #SPRAWDZANIE NOWEGO POZIOMU
            if xp_remain <= 0:
                level = level + 1
                xp_remain = 100
                print(Fore.YELLOW + 'Osiągnałeś poziom' + str(level))
                new_round = True
        # PO WYGRANEJ / PRZEGRANEJ
        if player_won == True or monster_won == True:
            new_round = False
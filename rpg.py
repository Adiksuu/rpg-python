# IMPORTOWANIE MODUŁÓW

# COLORAMA - KOLORKI
import colorama 
from colorama import Fore
colorama.init()

# RANDOM - LOSOWOŚĆ 
from random import randint

# ZMIENNE 
level = 1
xp_remain = 100
xp = 100

xp_min = 10
xp_max = 35

monster_health_max = 200
# START GRY
game_running = True

# WYBRANA KLASA...
print('')
print(Fore.CYAN + '-------' * 7)
print(Fore.CYAN + ' Wybierz klasę ( Mag, Wojownik, Rycerz, Strzelec, Pogromca, Rolnik )')
player_class = input(Fore.BLUE + ' Wybrana klasa: ')
print(Fore.CYAN + '-------' * 7)

#WYBÓR KLASY
if player_class == 'Mag':
    health = 50
    max_health = 50
    attack = 19
    heal = 20
elif player_class == 'Wojownik':
    health = 75
    max_health = 75
    attack = 14
    heal = 13
elif player_class == 'Rycerz':
    health = 90
    max_health = 90
    attack = 10
    heal = 16
elif player_class == 'Strzelec':
    health = 40
    max_health = 40
    attack = 24
    heal = 19
elif player_class == 'Pogromca':
    health = 50
    max_health = 50
    attack = 24
    heal = 12
elif player_class == 'Rolnik':
    health = 69
    max_health = 69
    attack = 16
    heal = 10
else:
    print('')
    print(Fore.LIGHTRED_EX + '------' * 7)
    print(Fore.RED + 'Nie znaleziono takiej klasy, spróbuj ponownie')
    print(Fore.LIGHTRED_EX + '------' * 7)
    print('')



# PĘTLA GRY
while game_running == True:

# STATYSTYKI PRZECIWNIKA
    monster = {'name': 'BOSS', 'attack_min': 11, 'attack_max': 15, 'health': 200}
    new_round = True
            
# POZIOMY I NAGRODY
    if xp_remain <= 0:
        level = level + 1
        xp = xp * 1.5
        xp_remain = xp
        attack = attack + 5
        max_health = max_health + 5
        monster_health_max = monster_health_max + 5
        print('')
        print('---' * 7)
        print(Fore.BLUE + 'Otrzymujesz +5 attack! ' + Fore.CYAN +'Aktualnie posiadasz: ' + str(attack) + Fore.RED + ' ATTACK')
        print(Fore.BLUE + 'Otrzymujesz +5 hp! ' + Fore.CYAN +'Aktualnie posiadasz: ' + str(max_health) + Fore.RED + ' HP')
        print(Fore.YELLOW + 'Osiągnałeś poziom: ' + str(level))
        print('')
    
    #INFO HP
    print('')
    print(Fore.CYAN + '---' * 5)
    health = max_health
    monster['health'] = monster_health_max
    print(Fore.LIGHTGREEN_EX + player_class + Fore.GREEN + ' Posiada: ' + Fore.LIGHTRED_EX + str(health) + Fore.RED + 'HP')
    print(Fore.LIGHTGREEN_EX + monster['name'] + Fore.GREEN + ' Posiada: ' + Fore.LIGHTRED_EX + str(monster['health']) + Fore.RED + 'HP')
    # PĘTLA NOWEJ RUNDY - MENU
    while new_round == True:

        player_won = False
        monster_won = False

        print('')
        print('---' * 5)
        print(Fore.CYAN + '1.' + Fore.LIGHTBLUE_EX + ' Atakuj')
        print(Fore.CYAN + '2.' + Fore.LIGHTBLUE_EX + ' Ulecz')
        print(Fore.CYAN + '3.' + Fore.LIGHTBLUE_EX + ' Wyświetl Statystyki')
        print(Fore.CYAN + '4.' + Fore.LIGHTBLUE_EX + ' Opuść Grę!')
    # PĘTLA NOWEJ RUNDY - WYBRANA OPCJA - INPUT
        player_choice = input(Fore.BLUE + 'Wybrana opcja: ' + Fore.CYAN)
        print('')

    # PĘTLA NOWEJ RUNDY - WYBRANA OPCJA - JEŻELI WYBRANA OPCJA TO...

    # JEŻELI WYBRANA OPCJA TO 1...
        if player_choice == '1':
            monster['health'] = monster['health'] - attack
            if monster['health'] <= 0:
                monster['health'] = 0
                player_won = True

            else:
                monster_attack = randint(monster['attack_min'], monster['attack_max'])
                health = health - monster_attack
                if health <= 0:
                    health = 0
                    monster_won = True
    # JEŻELI WYBRANA OPCJA TO 2...
        elif player_choice == '2':
            if health < max_health:
                health = health + heal
                print(Fore.RED + 'Gracz został uleczony!')
            if health > max_health:
                health = max_health

    # JEŻELI WYBRANA OPCJA TO 3...    
        elif player_choice == '3':
            print('')
            print(Fore.LIGHTMAGENTA_EX + 'Do następnego poziomu brakuje ci: ' + Fore.MAGENTA + str(xp_remain) + ' XP')
            print(Fore.LIGHTMAGENTA_EX + 'Aktualnie posiadasz: ' + Fore.MAGENTA + str(level) + ' LVL')
            print('')
    # JEŻELI WYBRANA OPCJA TO 4...
        elif player_choice == '4':
            print(Fore.RED + 'Opuszczanie...')
            new_round = False
            game_running = False

    # INFORMACJE O WYGRANYCH
        if player_won == False and monster_won == False:
            print(Fore.MAGENTA + player_class + ' Posiada: ' + Fore.LIGHTMAGENTA_EX + Fore.LIGHTRED_EX + str(health) + Fore.RED + ' HP')
            print(Fore.MAGENTA + monster['name'] + ' Posiada: ' + Fore.LIGHTMAGENTA_EX + Fore.LIGHTRED_EX + str(monster['health']) + Fore.RED + ' HP')

        elif player_won == True:
            print(Fore.LIGHTGREEN_EX + player_class + Fore.GREEN + ' Wygrywa!')
            new_round = False
            xp_remain = xp_remain - randint(xp_min, xp_max)

        elif monster_won == True:
            print(Fore.LIGHTGREEN_EX + monster['name'] + Fore.GREEN + ' Wygrywa!')
            new_round = False

        # PO WYGRANEJ / PRZEGRANEJ
        if player_won == True or monster_won == True:
            new_round = False

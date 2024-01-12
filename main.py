import utils

games = ["rescue", "explorers", "gates", "super"]
options = ['exit', 'check', 'help', 'delete']
pokemon_list = []
unown_forms = []
last_pokemon = {"rescue": 386, "explorers": 492, "gates": 649, "super": 721}

def add_new_pokemon(name):
    new_pokemon = utils.get_pokemon_by_name(name, utils.get_all_pokemons())
    pokemon_list.append(new_pokemon)
    pokemon_list.sort(key = lambda x:int(x['id']))
    utils.update_file(pokemon_list, game)

    if len(pokemon_list) == last_pokemon[game]:
        print("You have recruited all Pokemons! CONGRATULATIONS!")

def remove_pokemon(name):
    pokemon_to_remove = utils.get_pokemon_by_name(name, utils.get_all_pokemons())
    pokemon_list.remove(pokemon_to_remove)
    utils.update_file(pokemon_list, game)

def ask_yes_no():
    while True:
        res = input().lower()
        if res in ['y', 'n']:
            break
    
    return True if res == 'y' else False

def unown_management():
    if not utils.get_pokemon_by_name('unown', pokemon_list):
        return False
    
    unown_forms = utils.load_unown_forms(game)
    
    if len(unown_forms) == 28:
        print("You have already recuited all Unown forms!")
        return True
    
    print(f'You have already recruited Unown: Would you like to check for the forms of Unown? ', end ='')
    if not ask_yes_no():
        return True
    
    while True:
        letter = input("Insert the form (empty for exit): ")
        if not letter: break
        letter = letter[0]
        if not (letter.isalpha() or letter in ['!', '?']):
            print(f'Unown does not have that form!')
            continue    
        if letter not in unown_forms:
            print(f'You don\'t have recruited unown{letter.upper()}: Would you like to add this new form?', end=' ')
            if ask_yes_no():
                utils.add_unown_form(unown_forms, letter.lower(), game)
                print(f'Unown{letter.upper()} joined your party!')
            continue
        print(f'You have already recruited unown{letter.upper()}')
                    
    return True 

def multi_search(mon_list):
    print('You sent a list of pokemon.')

    for mon in mon_list:
        check_input(mon)
    pass

def option_rules(option):
    if option == 'exit':
        print("BYE BYE!")
        exit()
    
    if option == 'check':
        game_gen = utils.get_generation_game(game)
        remaining_list = utils.get_remaining_pokemons(pokemon_list, game_gen)
        
        if len(remaining_list) == 0:
            print("You have recruited all Pokemons! CONGRATULATIONS!")
            return

        print(f'You still have to recruit {len(remaining_list)} pokemon: would you like to check who are exactly missing?', end='')
        if ask_yes_no():
            for mon in remaining_list: print(mon)
        return
    
    if option == 'delete':
        print(f'Choose the Pokemon that you would like to remove: ', end='')

        name = input().lower()
        mon = utils.get_pokemon_by_name(name, pokemon_list)

        if not mon:
            print('This Pokemon does not exist or you have not recruited yet, please retry:', end='')
            return
        
        print(f'Are you sure to say goodbye to {name.capitalize()}?', end='')

        if ask_yes_no():
            remove_pokemon(name)
            print(f'{name.capitalize()} said goodbye...')

def check_input(name):
    
    if name in options: 
        option_rules(name)
        return

    mon = utils.get_pokemon_by_name(name, utils.get_all_pokemons())

    if not mon:
        print('Pokemon not found, please write the name properly')
        return
    
    mon_gen = utils.get_generation_pokemon(name)
    game_gen = utils.get_generation_game(game)

    if mon_gen > game_gen:
        print(f'{name.capitalize()} is not in this game!')
        return
    
    if utils.get_pokemon_by_name(name, pokemon_list) and name != 'unown':
        print(f'You already have obtained {name.capitalize()}!')
        return

    if name == 'arceus' and game_gen == 4:
        print('Arceus is unobtainable in Explorers series.')
        return

    if name == 'unown':
        if unown_management(): return

    print(f'You still not have obtained {name.capitalize()}: Would you like to add it? ', end='')
    if ask_yes_no(): 
        add_new_pokemon(name)
        print(f'{name.capitalize()} joined your party!')

while True:
    game = input("Select the game: ").rstrip().lower()
    if game in games:
        break
    print("Not correct, retry")

print('Welcome to the world of Pokemon!')
print('Uploading the list....')
pokemon_list = utils.open_file('data/games/'+game)
print('Upload complete!')

if len(pokemon_list) == last_pokemon[game]:
    print("You have recruited all Pokemons! CONGRATULATIONS!")

while True:
    name = input("Give me a Pokemon: ").rstrip().lower()
    mon_list = name.split(' ')
    if len(mon_list) > 1:
        multi_search(mon_list)
        continue
    
    check_input(name)
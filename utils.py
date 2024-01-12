import pokebase as pb

#generations = {'generation-i': 1, 'generation-ii': 2, 'generation-iii': 3, 'generation-iv': 4, 'generation-v': 5, 'generation-vi': 6}
games_generation = {"rescue": 3, "explorers": 4, "gates": 5,"super":6}
pokemon_list =[]

def get_pokemon_by_name(name, pokemons):
    return next((poke for poke in pokemons if poke.get('name') == name),None)

def get_all_pokemons():
    return tuple(pokemon_list)

def get_generation_game(name):
    return games_generation[name]

def get_remaining_pokemons(current_list, game_gen):
    the_list = [poke for poke in pokemon_list if poke not in current_list and poke.get('generation') <= game_gen]
    
    if game_gen == 4:
        the_list = [poke for poke in the_list if poke.get('name') != 'arceus']
    
    return the_list   

def get_generation_pokemon(name):
    poke = get_pokemon_by_name(name, pokemon_list)

    if poke:
        return poke['generation']

def add_unown_form(unown_forms, letter, file):
    unown_forms.append(letter)
    alphas = [c for c in unown_forms if c.isalpha()]
    alphas.sort()
    alphas.append('!') if '!' in unown_forms else None
    alphas.append('?') if '?' in unown_forms else None
    unown_forms = alphas
    letters = ''.join(unown_forms)
    
    with open('data/unown/'+file +'.txt', 'w') as fd:
        fd.write(letters)

def load_unown_forms(file):
    with open('data/unown/'+file +'.txt', 'r') as fd:
        unown_forms = list(fd.read())

    return unown_forms   

def open_file(file):
    with open(file+'.txt', 'r') as fd:
        lines = [line.rstrip('\n').split(';') for line in fd.readlines()]
        res_list = [dict(id = line[0], name = line[1], generation = int(line[2])) for line in lines]
    return res_list

def update_file(updated_list, game):
    with open('data/games/'+game +'.txt', 'w') as fd:
        for mon in updated_list:
            line = str(mon['id']) + ';' + mon['name'] + ';' + str(mon['generation'])
            fd.write(line+'\n')

pokemon_list = open_file('mons')

if __name__ == '__main__':
    print('Running this file is useless')
    '''l = pb.APIResourceList('pokemon-species')
    mon_list = []
    i = gen = 1
    new_gen = [152,252,387,494,650,722,810,906]
    print("Calling the APIs... Please wait")
    for el in l:
        mon = pb.APIResource('pokemon-species' , el['name'])
        line = str(i) + ';' + el['name'] + ';' + str(gen)
        mon_list.append(line)
        i +=1
        if i in new_gen: gen +=1
    with open('mons.txt', 'w') as fd:
        for mon in mon_list:
            fd.write(str(mon)+'\n')
        print("Done!")'''
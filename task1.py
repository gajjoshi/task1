modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
                 'StELLa']
indices = list()
characters = list()
for i, name in enumerate(modern_family):
    indices.append(i)
    characters.append(name.lower().replace('_', '-'))

print(indices)
print(characters)
[0, 1, 2, 3, 4]
['claire-dunphy', 'phil-dunphy', 'gloria-pritchett', 'cameron-tucker', 'stella']
n = lambda a: len(a)
temp = list(map(n, characters))
print(temp)
[13, 11, 16, 14, 6]
indices = list(map(sum, (zip(indices, temp))))
indices.sort(reverse=True)
Phew_finally = dict(zip(indices, characters))
print(Phew_finally)
{18: 'claire-dunphy', 17: 'phil-dunphy', 13: 'gloria-pritchett', 12: 'cameron-tucker', 10: 'stella'}

creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
               'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
               'green_light', 'red_light', 'red_light', 'green_light', 'you_got_shot', 'red_light', 'you_got_shot']

next_game = []
next_game.append(creepy_doll[1:len(creepy_doll) - 1:3])
print(next_game)
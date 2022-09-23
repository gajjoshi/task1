modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
                 'StELLa']
indices = list()
characters = list()
for i, name in enumerate(modern_family):
    indices.append(i)
    characters.append(name.lower().replace('_', '-'))

print(indices)
print(characters)

task = 'find the longest and shortest meaning in a dictionary'

meaning = {'piece': 'Portion of an object or of a material, produced by cutting',
           'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
           'area': 'a region or part of a town, a country, ot the world',
           'visit': 'go to see and spend time with (someone)',
           'with': 'having or possessing',
           'small': 'less than normal'
           }

keys = list(meaning.keys())
values = list(meaning.values())

lens = [len(x) for x in values]
print(keys)
print(values)
print(lens)

max = max(lens)
min = min(lens)

print(max)
print(min)

max_index = lens.index(max)
min_index = lens.index(min)

print(max_index)
print(min_index)

longest_meaning = keys[max_index]
shortest_meaning = keys[min_index]

print('longest_meaning is',longest_meaning,'=>', values[max_index])
print('shortest_meaning is',shortest_meaning,'=>', values[min_index])
# find planet name by ID

def planet(id):
    planets = {1: 'Mecury', 2: 'Venus', 3: 'Earth', 4: 'Mars',
              5: 'Jupiter', 6: 'Saturn', 7: 'Uranus', 8: 'Neptune',
              9: 'Pluto'}

    if id > len(planets):
        return 'outside the solar system'
    else:
        return planets[id]


id = int(input('Enter Planet id'))
p = planet(id)
print('planet is', p)
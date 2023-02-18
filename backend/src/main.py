from game.game_objects import EGame
from world.places import ELocation, EPlace
from world.geology import EPosition, EDirection
# import os

def print_edimons(edimons):
    for edimon in edimons:
        print(f"  {edimon.id}")
        print(f"    {edimon.name}")
        print(f"    {edimon.type}")
        print_stats(edimon.stats)
    print()

def print_stats(stats):
    print(f"      hp: {stats.hp}")
    print(f"      attack: {stats.attack}")
    print(f"      defense: {stats.defense}")
    print(f"      speed: {stats.speed}")

def print_locations(locs):
    for loc in locs:
        print(f'  {loc.name}')
        print_positions(loc.positions)
    print()

def print_positions(positions):
    for pos in positions:
        print(f'    ({pos.x}, {pos.y})')
    print()

def print_places(places: list[EPlace]):
    for place in places:
        xs = place.xs
        ys = place.ys
        print('  locations: ')
        for loc in place.locations:
            print(f'    {loc.name}')
        
        xs = place.xs
        x = 0
        print('  positions:')
        for pos in place.positions:
            print(pos, end=' ')
            x += 1
            if x == xs:
                x = 0 
                print()
        print()

def main():
    game = EGame('database.json')
    game.start()

    print('current pos: ', game.player.pos)
    print('moving down...')
    game.move_down()
    print('moving right...')
    game.move_right()
    print('current pos: ', game.player.pos)
    print()
    print('other data:')
    print('edimons')
    print_edimons(game.edimons)
    print('locations')
    print_locations(game.locations)

    print('places')
    print_places(game.places)

if __name__ == '__main__':
    main()
from random import choice

def create_tunnel(cave_from, cave_to):
    """ Create a tunnel between cave_from and cave_to"""
    caves[cave_from].append(cave_to)
    caves[cave_to].append(cave_from)

def visit_cave(cave_number):
    """Mark a cave as visited"""
    visited_caves.append(cave_number)
    unvisited_caves.remove(cave_number)

def choose_cave(cave_list):
    """Pick a cave from a list, provided that the cave has less than 3 tunnels."""
    cave_number = choice(cave_list)
    while len(caves[cave_number]) >= 3:
        cave_number = choice(cave_list)
    return cave_number

def print_caves():
    """Print out the current cave structure"""
    for number in cave_numbers:
        print number, ":", caves[number]
    print '---------------------------------------------------'

def setup_caves(cave_numbers):
    """ Create the starting list of caves """
    caves = []
    for cave in cave_numbers:
        caves.append([])
    return caves

def link_caves():
    """Mark sure all of the caves are connected with two-way tunnels"""
    while unvisited_caves != []:
        this_cave = choose_cave(visited_caves)
        next_cave = choose_cave(unvisited_caves)
        create_tunnel(this_cave, next_cave)
        visit_cave(next_cave)

def finish_caves():
    """Link the rest of the caves with one-way tunnels"""
    for cave in cave_numbers:
        while len(caves[cave]) < 3:
            passage_to = choose_cave(cave_numbers)
            caves[cave].append(passage_to)

def print_location(player_location):
    """Tell the player about where they are"""
    print "You are in cave ���ڴ˶�Ѩ��", player_location
    print "From here, you can see caves: ��������Ե������¶�Ѩ��", caves[player_location]
    if wumpus_location in caves[player_location]:
        print "I smell a wumpus!ע�⣺���޾��ڸ�����"

def get_next_location():
    """Get the player's next location"""
    print ""
    print "Which cave next?������һ������ȥ�Ķ�Ѩ��"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print player_input, "?"
        print "Thats's not a a direction that I can see! ��Ѩѡ��������������룺"
        return None
    else:
        return int(player_input)

cave_numbers = range(0,20)
unvisited_caves = range(0,20)
visited_caves = []
caves = setup_caves(cave_numbers)

visit_cave(0)
#print_caves()
link_caves()
#print_caves()
finish_caves()
print_caves()

wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location):
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "You can see", len(cave_numbers), "caves"
print "To play, just type the number"
print "of the cave you wish to enter next"

print "��ӭ�����Բ�����!"
print "���ܿ���", len(cave_numbers), "����Ѩ"
print "���ʱ���������֣�"
print "��ʾ��ϣ������Ķ�Ѩ"

while True:
    print_location(player_location)
    new_location = get_next_location()
    if new_location is not None:
        player_location = new_location
    if player_location == wumpus_location:
       print "Aargh! You got eaten by a wumpus!����! �㱻���޳Ե���!"
       break


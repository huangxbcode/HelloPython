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
    print ""
    print "You are in cave 你在此洞穴：", player_location, cave_names[player_location]
    print "From here, you can see caves: 在这里，可以到达如下洞穴："

    neighbors = caves[player_location]
    for tunnel in range(0,3):
        next_cave = neighbors[tunnel]
        print "   ", tunnel+1, "-", cave_names[next_cave]

    if wumpus_location in caves[player_location]:
        print ""
        print "I smell a wumpus!注意：怪兽就在附近！"
        print ""

def get_next_location():
    """Get the player's next location"""
    print ""
    print "Which cave next?输入下一个你想去的洞穴："
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in caves[player_location]):
        print player_input, "?"
        print "Thats's not a a direction that I can see! 洞穴选择错误，请重新输入："
        return None
    else:
        return int(player_input)

def ask_for_cave():
    """ Ask the player to choose a cave from their current_location. """
    player_input = raw_input("Which cave? 请选择要搜索或射击的洞穴：")
    if(player_input in ['1', '2', '3']):
        index = int(player_input)-1
        neighbors = caves[player_location]
        cave_number = neighbors[index]
        return cave_number
    else:
        print player_input + "?"
        print "That's not a direction that I can see! 此洞穴不可见，请选择其它"
        return None

def get_action():
    """ Find out what the player wants to do next. """
    print ""
    print "What do you do next? 请确认你的下一步行动："
    print "   m)  move 进入下一个洞穴,请输入 m "
    print "   f)  fire an arrow 开弓放箭，向怪兽射击，请输入 f"
    print ""
    action = raw_input("> ")
    if action == "m" or action == "f":
        return action
    else:
        print action + "?"
        print "That's not an action that I know about 无效的行动，请输入正确的行动"
        return None

def do_movement():
    print "Moving... 正在移动..."
    new_location = ask_for_cave()
    if new_location is None:
        return False
    else:
        return new_location

def do_shooting():
    print "Firing... 即将向洞穴射击..."
    shoot_at = ask_for_cave()
    if shoot_at is None:
        return False
    if shoot_at == wumpus_location:
        print "Twang ... Aargh! You shot the wumpus! Duang! 你击中了怪兽！"
        print "Well done, mighty wumpus hunter! 太好了，杰出的怪兽猎手！"
    else:
        print ""
        print "Twang ... clatter, clatter!"
        print "You wasted your arrow!"
        print "Empty handed, you begin the long trek back to your village..."
        print "Duang Duang！未射中怪兽，继续努力吧！"
        print ""
        return False
    return True

cave_names = ["盘丝洞","游龙洞","水帘洞","蜘蛛洞","泥鳅洞","中南海","北海","东海","南海","西海"]
            
cave_numbers = range(0,10)
unvisited_caves = range(0,10)
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

print "欢迎来到猎捕怪兽!"
print "你能看到", len(cave_numbers), "个洞穴"
print "玩的时候，输入数字，"
print "表示你希望进入的洞穴"

while True:
    print_location(player_location)
        
    if wumpus_location in caves[player_location]:
        action = get_action()
        if action is None:
            continue
        if action == "m":
            player_location = do_movement()
            if player_location == wumpus_location:
                print "Aargh! You got eaten by a wumpus!哈哈! 你被怪兽吃掉了!"
                break
        if action == "f":
            game_over = do_shooting()
            if game_over:
                break
            else:
                player_location = do_movement()
                if player_location == wumpus_location:
                    print "Aargh! You got eaten by a wumpus!哈哈! 你被怪兽吃掉了!"
                    break
    else:
        player_location = do_movement()
        if player_location == wumpus_location:
            print "Aargh! You got eaten by a wumpus!哈哈! 你被怪兽吃掉了!"
            break
        
            


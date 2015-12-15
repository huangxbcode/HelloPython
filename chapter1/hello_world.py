from random import choice
cave_numbers = range(1,8)
wumpus_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while player_location == wumpus_location:
    player_location = choice(cave_numbers)

print "Welcome to Hunt the Wumpus!"
print "欢迎来到猎捕怪兽!"
print "You can see", len(cave_numbers), "caves"
print "你能看到", len(cave_numbers), "个洞穴"
print "To play, just type the number"
print "玩的时候，输入数字，"
print "of the cave you wish to enter next"
print "表示你希望进入的洞穴"

while True:
    print "You are in cave", player_location
    print "你在洞穴", player_location
    if(player_location == wumpus_location-1 or
       player_location == wumpus_location +1):
        print "I smell a wumpus!"
        print "我闻到了怪兽!"
        print "Which cave next?"
        print "下一个洞穴?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print player_input, "is not a cave!"
        print player_input, "不是洞穴号，输入错误!"
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
           print "Aargh! You got eaten by a wumpus!"
           print "哈哈! 你被怪兽吃掉了!"
           break

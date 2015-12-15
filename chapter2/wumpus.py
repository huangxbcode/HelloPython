from random import choice
cave_numbers = range(1,15)
wumpus_location = choice(cave_numbers)
wumpus_friend_location = choice(cave_numbers)
player_location = choice(cave_numbers)
while (player_location == wumpus_location or
       player_location == wumpus_friend_location):
    player_location = choice(cave_numbers)

print wumpus_location,wumpus_friend_location,player_location
print "Welcome to Hunt the Wumpus!"
print "��ӭ�����Բ�����!"
print "You can see", len(cave_numbers), "caves"
print "���ܿ���", len(cave_numbers), "����Ѩ"
print "To play, just type the number"
print "���ʱ���������֣�"
print "of the cave you wish to enter next"
print "��ʾ��ϣ������Ķ�Ѩ"

while True:
    print "You are in cave", player_location
    print "���ڶ�Ѩ", player_location
    if(player_location == wumpus_location-1 or
       player_location == wumpus_location +1):
        print "I smell a wumpus!"
        print "���ŵ��˹���!"
    if(player_location == wumpus_friend_location-1 or
       player_location == wumpus_friend_location +1):
        print "I smell an even stinkier wumpus!"
        print "���ŵ�����һ������!"
    print "Which cave next?"
    print "��һ����Ѩ?"
    player_input = raw_input(">")
    if (not player_input.isdigit() or
        int(player_input) not in cave_numbers):
        print player_input, "is not a cave!"
        print player_input, "���Ƕ�Ѩ�ţ��������!"
    else:
        player_location = int(player_input)
        if player_location == wumpus_location:
           print "Aargh! You got eaten by a wumpus!"
           print "����! �㱻���޳Ե���!"
           break
        if player_location == wumpus_friend_location:
           print "Aargh! You got eaten by the wumpus'friend!!"
           print "����! �㱻�ڶ������޳Ե���!"
           break

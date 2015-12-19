# coding=utf-8
from random import choice, shuffle

class Cave(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.here = []
        self.tunnels = []

    def tunnel_to(self, cave):
        """Create a two-way tunnel"""
        self.tunnels.append(cave)
        cave.tunnels.append(self)

    def __repr__(self):
        return "<Cave " + self.name + ">"

cave_names = ["盘丝洞","游龙洞","水帘洞","蜘蛛洞","泥鳅洞",
              "鳝鱼洞","螃蟹洞","水母洞","黄金洞","水银洞",]

def create_caves():
    shuffle(cave_names)
    caves = [Cave(cave_names[0], cave_names[0])]
    for name in cave_names[1:]:
        new_cave = Cave(name, name)
        eligible_caves = [cave for cave in caves
                          if len(cave.tunnels)<3]
        new_cave.tunnel_to(choice(eligible_caves))
        caves.append(new_cave)
    return caves

if __name__ == '__main__':
    for cave in create_caves():
        print cave.name, "=>", cave.tunnels

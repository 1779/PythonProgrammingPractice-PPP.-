class Game:

    num = 0

    def __init__(self):
        self.name = "laowang"

    @classmethod
    def add_num(cls):
        cls.num = 100
    
    @staticmethod
    def print_menu():
        print("——————————————————————")
        print("——————游戏开始——————")
        print("——————————————————————")



game = Game()
game.print_menu()
print(game.name)
print(Game.num)
#Game.add_num()
game.add_num()
print(game.name)
print(game.num)


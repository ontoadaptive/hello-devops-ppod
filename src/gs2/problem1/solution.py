class Solution(object):
    def __init__(self, id, name, difficulty):
        self.id = id
        self.name = name
        self.difficulty = difficulty

    # GS2. Driver code
    def winner(self, game):

        def plus_one_match(listGame, x):
            if listGame[x] == listGame[x + 1]:
                return True
            else:
                return False

        def plus_two_match(listGame, x):
            if listGame[x] == listGame[x + 2]:
                return True
            else:
                return False

        def game_tokens_same(listGame, x):
            if(x+1 < len(listGame) and x+2 < len(listGame)):
                if plus_one_match(listGame, x) and plus_two_match(listGame, x):
                    return True
                else:
                    return False
        turn = 1
        playing = True
        listGame = list(game)
        while(playing):
            while(turn % 2 == 0):
                for x in range(0, len(listGame)):
                    if listGame[x] == 'b':
                        if game_tokens_same(listGame, x):
                            del listGame[x + 1]
                            turn += 1
                            break
                if turn % 2 == 0:
                    playing = False
                    return 'Wendy'

            while(turn % 2 != 0):
                for x in range(0, len(listGame)):
                    if listGame[x] == 'w':
                        if game_tokens_same(listGame, x):
                            del listGame[x + 1]
                            turn += 1
                            break
                if turn % 2 != 0:
                    playing = False
                    return 'Bob'

        return "Wendy"

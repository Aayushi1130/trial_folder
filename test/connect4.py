import json
player_moves = []
input_file = json.load(open("connect4.json"))
for each in input_file:
    player_moves.append(each['column'])

ROWS = 6
COLS = 7

print(player_moves)

class Game():
    def __init__(self):
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
        self.turns = 0
        self.piece = [-1,-1] 
        
        
    def display(self):
        for c in range(COLS):
            print(f"({c}) ",end = "")
        print("\n")
        for r in range(ROWS):
            print("|",end="")
            for c in range(COLS):
                print(f" {self.board[r][c]} |", end = "")
            print("\n")
        print("-------------------------------------------------\n")
        
    def isempty(self):
        for x in self.board:
            if x == ' ':
                return False
        return True
    
    def playing(self):
        players = ['1','2']
        return players[self.turns % 2]
        
    def turn(self,col):
        for r in range(ROWS-1,-1,-1):
            if self.board[r][col] == ' ':
                self.board[r][col] = self.playing()
                self.piece = [r,col]
                self.turns += 1
                return True
        return False
    
    
    def winner(self):
        lrow = self.piece[0]
        lcol = self.piece[1]
        match_piece = self.board[lrow][lcol]
        
        direction = [
            [[-1,0],0, True],
            [[1,0],0, True],
            [[0,-1],0, True],
            [[0,1],0, True],
            [[-1,1],0, True],
            [[1,-1],0, True],   
            [[-1,-1],0, True],
            [[1,1],0, True],
        ]
        
        for i in range(4):
            for d in direction:
                r = lrow + (d[0][0]*(i+1))
                c = lcol + (d[0][1]*(i+1))
                
                if d[2] and r >=0 and r < ROWS and c >=0 and c < COLS and self.board[r][c] == match_piece:
                    d[1] += 1
                else:
                    d[2] = False
        
        for j in range(0,7,2):
            if (direction[j][1]+direction[j+1][1] >= 3):
                print(f"Winner is Player {match_piece}")
                return match_piece
        return False
    
        
    

game = Game()
game.display()
game_over = False
while not game_over:
    for i in player_moves:
        user_move = i
        game.turn(user_move)
        game.display()
        winn = game.winner()
        if winn:
            break
    if game.isempty() and not winn:
        print("It is a draw!!!")
        
    print("\nGame Over!")
    break
        
     
import random

#RUNS A SNAKE GAME IN THE SHELL.  MUST HIT ENTER BETWEEN EACH INPUT.

class board:
    """Class for implimenting the grid that the snake game is played on"""

    def __init__(self):
        self.grid = []
        self.food_spot = []

    def create(self):
        """Creates a blank grid for the game to start on"""
        for row in range(10):
            self.grid.append([])
            for column in range(10):
                self.grid[row].append('.')

    def output(self):
        """Outputs what is currently on the grid"""
        for row in self.grid:
            print(row)

    def snake_board(self, snake):
        """Adds the snakes location on the grid"""
        self.grid[snake.locations[-1][0]][snake.locations[-1][1]] = '.'
        snake.locations.pop()
        for i in range(snake.size):
            self.grid[snake.locations[i][0]][snake.locations[i][1]] = 'X'
        
        
    def food(self, snake):
        """Randomly generates where the food will be placed on the grid
            and changes the character given when it is eaten"""
        if self.food_spot == []:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            self.food_spot = [[y, x]]
            while self.food_spot[0] in snake.locations:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                self.food_spot = [[y, x]]
            self.grid[y][x] = 'O'
        if self.food_spot[0] in snake.locations:
            self.grid[self.food_spot[0][0]][self.food_spot[0][1]] = '#'

    def eat(self, snake):
        """Adds to the snakes length and adjusts the snakes locations on the
            grid once the last part passes the eaten portion"""
        if self.food_spot[0] == snake.locations[-1]:
            snake.add()
            snake_tail = self.food_spot.pop()
            snake.locations.append(snake_tail)
            print(snake.size)
            print(self.food_spot)


class snake:

    def __init__(self):
        self.size = 5
        self.locations = []
        self.head_x = 5
        self.head_y = 5
        self.direction = 'a'

    def start(self):
        """Generates a snake to start the game"""
        for i in range(self.size):
            self.locations.append([5, 5 + i])

    def direct(self):
        """Takes input to move the snake and adjust the locations on the grid"""
        move = input()
        accept = ['w', 's', 'a', 'd']
        while move not in accept:
            move = input()
        if move == 'w':
            self.head_y -= 1

        if move == 's':
            self.head_y += 1

        if move == 'a':
            self.head_x -= 1

        if move == 'd':
            self.head_x += 1

        self.locations.insert(0, [self.head_y, self.head_x])


    def snake_output(self):
        """Used to test the contents of the locations of the snake on grid"""
        for i in range(self.size):
            print(self.locations[i])    

    def add(self):
        """Adds to the size of the snake"""
        self.size += 1



#MAIN

#LOOPS THE GAME TO CONTINUE PLAYING ONCE LOST
again = True
while again == True:

    #THESE SET UP THE GAME SO IT HAS A FRESH START 
    Game = board()
    Game.create()
    Item = snake()
    Item.start()

    #THESE ACT UPON EACH INDIVIDUAL GAME
    #LOOPS BETWEEN EACH TURN THE SNAKE MAKES
    play = True
    while play == True:
        Item.direct()
        Game.snake_board(Item)
        Game.food(Item)
        Game.eat(Item)
        Game.output()
        #CHECKS FOR COLLISION AND ENDS THE GAME WITH SCORE OUTPUT
        for i in range(Item.size - 1):
            if Item.locations[0] == Item.locations[i + 1]:
                print("GAME OVER \nYOUR SCORE WAS " , Item.size - 5)
                print("THE GAME WILL NOW RESET\n")            
                play = False
                break









class Game_of_life:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.current_state = []
        self.num_of_loops = 0

        self.i = 0
        self.j = 0

        self.alive = "o"
        self.dead = "."

        self.look_around_prefix = [self.move_up, self.move_left, self.move_down, self.move_down, self.move_right, self.move_right, self.move_up, self.move_up]

    def input_current_state(self, state):
        self.current_state = state

    def hand_input(self):
        self.width, self.height = [int(x) for x in input().split()]
        self.num_of_loops = int(input())
        self.current_state = []
        for _ in range(self.height):
            self.current_state.append(input())

    def render_game(self):
        separator = ["=" for _ in range(self.width)]

        for _ in range(self.num_of_loops):
            self.current_state = self.update_state(self.count_living_cells_around())
            print("".join(separator))
            for row in self.current_state:
                print("".join(row))

    def count_living_cells_around(self):
        living_cells_around = []
        for _ in range(self.height):
            living_cells_around.append([0 for _ in range(self.width)])

        for i in range(self.height):
            for j in range(self.width):
                self.i = i
                self.j = j

                for move in self.look_around_prefix:
                    move()
                    if self.current_state[self.i][self.j] == self.alive:
                        living_cells_around[i][j] += 1

        return living_cells_around

    def update_state(self, count_list):
        updated_state = []
        for _ in range(self.height):
            updated_state.append([0 for _ in range(self.width)])

        c = 0
        r = 0
        for row in count_list:
            for count in row:
                if self.current_state[c][r] == self.alive and count < 2:
                    updated_state[c][r] = self.dead

                elif self.current_state[c][r] == self.alive and count == 2 or count == 3:
                    updated_state[c][r] = self.alive

                elif self.current_state[c][r] == self.alive and count > 3:
                    updated_state[c][r] = self.dead

                elif self.current_state[c][r] == self.dead and count == 3:
                    updated_state[c][r] = self.alive

                else:
                    updated_state[c][r] = self.current_state[c][r]              
                    
                r += 1

            r = 0
            c += 1

        return updated_state
        
    def move_up(self):
        if self.i == 0:
            self.i = self.height - 1
        else:
            self.i += -1

    def move_down(self):
        if self.i == self.height - 1:
            self.i = 0
        else:
            self.i += 1

    def move_left(self):
        if self.j == 0:
            self.j = self.width - 1
        else:
            self.j += -1

    def move_right(self):
        if self.j == self.width - 1:
            self.j = 0
        else:
            self.j += 1

    def run(self):
        
        for _ in range(self.num_of_loops):
            self.current_state = self.update_state(self.count_living_cells_around())
            self.render_game()


game = Game_of_life()
game.hand_input()
game.render_game()

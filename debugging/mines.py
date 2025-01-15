#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.cells_to_reveal = width * height - mines  # Non-mine cells to reveal

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if (y * self.width + x) in self.mines:
            return False
        if not self.revealed[y][x]:  # Only update if not already revealed
            self.revealed[y][x] = True
            self.cells_to_reveal -= 1
            if self.count_mines_nearby(x, y) == 0:
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            self.reveal(nx, ny)
        return True

    def play(self):
        while True:
            self.print_board()
            if self.cells_to_reveal == 0:  # Check for a win
                self.print_board(reveal=True)
                print("Congratulations! You won!")
                break
            try:
                x = int(input("Enter x coordinate (0-9): "))
                y = int(input("Enter y coordinate (0-9): "))
                if 0 <= x < 10 and 0 <= y < 10:  # Validate range
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                else:
                    print("Invalid input. Please enter numbers between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
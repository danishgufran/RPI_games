import curses
import random
import time

def main(stdscr):
    # Initialize the screen
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initialize variables
    snake = [(sh//2, sw//4)]
    food = (sh//2, sw//2)
    key = curses.KEY_RIGHT
    score = 0

    while True:
        # Clear the screen
        w.clear()

        # Draw the snake and the food
        for y, x in snake:
            w.addstr(y, x, 'o')
        w.addstr(food[0], food[1], '*')

        # Get user input
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        # Update the snake position
        y, x = snake[0]
        if key == curses.KEY_UP:
            y -= 1
        elif key == curses.KEY_DOWN:
            y += 1
        elif key == curses.KEY_LEFT:
            x -= 1
        elif key == curses.KEY_RIGHT:
            x += 1
        snake.insert(0, (y, x))

        # Check if the snake hit a border
        if y == 0 or y == sh-1 or x == 0 or x == sw-1:
            w.addstr(sh//2, sw//2 - 6, "Loser LOL !")
            w.refresh()
            time.sleep(10)
            break

        # Check if the snake ate the food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                new_food = (random.randint(1, sh-1),
                            random.randint(1, sw-1))
                if new_food not in snake:
                    food = new_food
        else:
            snake.pop()

        # Display the score
        w.addstr(0, 0, "Score: {}".format(score))

        # Refresh the screen
        w.refresh()

# Run the game
curses.wrapper(main)


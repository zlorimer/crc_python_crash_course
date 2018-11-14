# Lesson 6 writing .py files instead of jupyter notebooks
import random
# IF RUNNING IN SPYDER SET BREAKPOINTS USING F12
if __name__ == '__main__': # this line ensures we are in the main application
    # Start your game here, replace enter some text with a question you want to ask the player
    game_over = False
    tries = 0
    number = random.randint(0,10)
    while not game_over:
        tries += 1
        some_text = int(input('Enter a number between 1 and 10: ')) # allows player to enter some text or a number
        print('You entered {}'.format(some_text))
        # Check the input with an if statement
        if some_text == number:
            print('You guessed the right answer')
            break
        elif some_text == (number - 1) or some_text == (number + 1):
            print('Getting warmer...')
        else:
            print('Try again')

        if tries == 5:
            game_over = True
            print('You lose. The number was ' + number)
        # Your task: make a 2-3 step text game with the starting code up above and have your neighbor try playing it
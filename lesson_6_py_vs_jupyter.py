# Lesson 6 writing .py files instead of jupyter notebooks

# IF RUNNING IN SPYDER SET BREAKPOINTS USING F12
if __name__ == '__main__': # this line ensures we are in the main application
    # Start your game here, replace enter some text with a question you want to ask the player
    game_over = False
    tries = 0
    while not game_over:
        tries += 1
        some_text = input('Enter a number between 1 and 10: ') # allows player to enter some text or a number
        print('You entered {}'.format(some_text))
        # Check the input with an if statement
        if some_text == '7':
            print('You guessed the right answer')
            break
        elif some_text == '6' or some_text == '8':
            print('Getting warmer...')
        else:
            print('Not even close')

        if tries == 5:
            game_over = True
            print('You are terrible at this game')
        # Your task: make a 2-3 step text game with the starting code up above and have your neighbor try playing it
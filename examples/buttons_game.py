from machine import Timer
from machine import I2C
from i2c_lcd import Display

from Button import Button
from time import sleep

i2c_bus = I2C(0)
display = Display(i2c_bus, 0x3e)

reset_timer = Timer(-1)
# states:
# 0: invite users to play > register button C action to trigger game info
# 1: game info displayed > register button C action to trigger game start
# 2: game is running > register buttons A and B to play | check for game score | first player to get to 20 wins
# 3: game is over > wait 2 seconds > go to state 4
# 4: announce player > wait 3 seconds > go to state 0

game_state = 0

player_one_score = 0
player_two_score = 0
winning_player = 0
max_score = 20


# display 16x2 alignment example
# aligning scores for player A and B
'''
________________
77    A--B    99
'''

# 💡💡💡 TIP 
# avoid to clearing the screen often
# by updating only the areas that need to change


def render_players_score():
    global winning_player

    # The first line of this screen has been printed during
    # the state change. From now on we'll only update line two
    display.move(0, 1)
    
    # format the two scores (player_one_score and player_two_score)
    # to always take at least 2 characters
    # this will get the single digit numbers to be prefixed by a space
    # i.e.: 9 will become ' 9' and there won't be any shifting or lack
    # of alignment which might result in a poor looking score line
    score_a = "{:>2}".format(player_one_score)
    score_b = "{:>2}".format(player_two_score)

    # let's write a composed string to line 2
    display.write(f'{score_a}    A--B    {score_b}')
    
    if player_two_score >= max_score:
        winning_player = 2
        change_state(3)
        return
        
    if player_one_score >= max_score:
        winning_player = 1
        change_state(3)
        return
    
    
        

def change_state(new_state):
    print(f"changing state to {new_state}")
    sleep(1)
    # only using sleep(1) to give a sense of state changing
    global game_state
    if new_state == 0:
        # reset scores
        player_one_score = 0
        player_two_score = 0
        winning_player = 0
        
        display.clear()
        display.write("  play with me")
        display.move(0, 1)
        display.write("  press button")
        
    if new_state == 1:
        display.clear()
        display.write("    2 players")
        display.move(0, 1)
        display.write("   fastest wins")
        
    if new_state == 2:
        display.clear()
        display.write("game ongoing")
        display.move(0, 1)
        display.write("2 players")
    
    if new_state == 3:
        display.clear()
        display.write("  the winner is")
        display.move(0, 1)
        display.write(f"player {winning_player}")
        # start reset timer
        # at the end of the waiting time, state 0 will be restored
        reset_timer.init(period = 3000, mode = Timer.ONE_SHOT, callback = reset_game)
        
    game_state = new_state
    
def player_one_score_increase():
    global player_one_score
    player_one_score = player_one_score + 1
    # print(player_one_score)
    
def player_two_score_increase():
    global player_two_score
    player_two_score = player_two_score + 1
    # print(player_one_score)

def button_one_action(little_pin, massive_event):
    print(f'button on pin {little_pin} registered {massive_event}')
    if massive_event == Button.RELEASED:
        player_one_score_increase()
        render_players_score()
    

def button_two_action(little_pin, massive_event):
    print(f'button on pin {little_pin} registered {massive_event}')
    if massive_event == Button.RELEASED:
        player_two_score_increase()
        render_players_score()
    

def button_three_action(little_pin, massive_event):
    global game_state
    print(f'button on pin {little_pin} registered {massive_event}')
    if game_state == 0 and massive_event == Button.RELEASED:
        change_state(1)
        return
    
    if game_state == 1 and massive_event == Button.RELEASED:
        change_state(2)
        return


buttonA = Button(26, rest_state = True, callback = button_one_action)
buttonB = Button(27, rest_state = True, callback = button_two_action)
buttonC = Button(4, rest_state = False, callback = button_three_action)

change_state(0)

def reset_game(timer_object):
    change_state(0)
    

while(True):
    if game_state == 0:
        # waiting for user to interact
        buttonC.update()
        pass

    if game_state == 1:
        # waiting to start game
        # showing instructions
        buttonC.update()
        pass
    
    if game_state == 2:
        # game running
        buttonA.update()
        buttonB.update()
        pass
    if game_state == 3:
        # do game state things
        pass
    if game_state == 4:
        # do game state things
        pass

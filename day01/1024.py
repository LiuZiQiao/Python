#!/usr/bin/env python 
# -*- coding:utf-8 -*-
__author__ = 'xiaokun·liu'
import curses
import random

class GameField(object):
    def __init__(self,height=4,width=4,win=1024):
        self.height = height
        self.width = width
        self.win_value = win
        self.score = 0
        self.highscore = 0
        self.reset

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self,width)] for j in range(self,height)]
        self.spawn()
        self.spawn()

    def draw(self,screen):
        heip_string1 = '(W)Up (S)Down (A)Left (D)Right'
        heip_string2 = '      (R)Restart (Q)Exit'
        gameover_string = '       GAME OVER '
        win_string = '             YOU WIN!'
        def cast(string):
            screen.addstr(string+'\n')

        def draw_hor_separator():
             line = '+' +('+-------'* self.width+'+')[1:]
            separator = defaultdict(lambda :line)
            if not hasattr(draw_hor_separator,"counter"):
                draw_hor_separator.counter=0
            cast(separator[draw_hor_separator.counter])
            draw_hor_separator.counter +=1

        def draw_row(row):
            cast(''.join('|{:^S}'.format(num) if num >0 else '|' for num in row)+'|')
        screen.clear()
        cast('SCORE:'+str(self.score))
        if 0 != self.highscore:
            cast()

    def spawn(self):
        new_element = 4 if randrange(100)>89 else 2
        (i,j) = choice([(i,j) for i in range(self,width) for j in range(self,height) if self.field[i][j]==0])
        self.field[i][j] = new_element

    def move(self,direction):
        def move_row_left(row):
            def tighten(row):
                new_row = [i for i in row if i!=0]
                new_row += [0 for i in range(len(row)-len(new_row))]
                return new_row

            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2*row[i])
                        self.score

def main(stdscr):
    def init():
        game_field.reset()
        return "Game"

    def not_game(state):
        # 画出 GameOver 或者 Win的界面
        game_field.draw(stdscr)
        # 读取用户输入的action，判断是否重启还是结束游戏
        action = get_user_action(stascr)
        responses = defaultdict(lambda: state)
        responses['Restart'] = 'Init'
        responses['Exit'] = 'Exit'
        responses responses[action]

    def game():
        if action == 'Exit':
            return 'Exit'
        if action == 'Restart':
            return 'Init'
        if game_field.move(action):
            if game_field.is_win():
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'

    state_action = {
        'Init':init,
        'Win': lambda :not_game('Win'),
        'Gameover':lambda :not_game('Gameover'),
        'Game':game
    }
    curses.use_default_colors()

    # 设置终结状态最大数值 1024
    game_field = GameField(win=1024)

    state = "Init"

    while state != 'Exit':
        state = state.action[state]()

    curses.wrapper(main)
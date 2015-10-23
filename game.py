#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import random
cells = {}
field_keys = []

def start():
  output = True
  num = raw_input("\nWELCOME TO THE GAME! ARE YOU READY? ENTER THE NUMBER:\n1. Menu;\n2. Exit.\n")   
  while(output):
    if num == "1":
      main_menu()
      output = False
    elif num == "2":
      print "\nBYE-BYE!"
      sys.exit()
    else:
      num = raw_input("\nYOU ENTERED SOMETHING WRONG! ENTER 1 OR 2.\n")

def main_menu():
  output = True
  num = raw_input("\nCHOOSE WHAT TO DO NEXT:\n1. Start;\n2. Authors;\n3. Back.\n")
  while(output):
    if num == "1":
      game()
      output = False
    elif num == "2":
      authors()
      output = False
    elif num == "3":
      start()
      output = False
    else:
      num = raw_input("\nYOU ENTERED SOMETHING WRONG! ENTER 1, 2 OR 3.\n")

def authors():
  output = True
  num = raw_input("\nDevelopment and Testing - Andriy Bondarev. About author: bla-bla man, egocentric alcoholic, hate black people and racism.\nEnter 1 to go back\n")
  while(output):
    if num == "1":
      main_menu()
      output = False
    else:
      num = raw_input("\nYOU ENTERED SOMETHING WRONG! ENTER 1 TO GO BACK.\n")


def character_not_bad():
  char_sting = """\n
             ▄██████████▄▄        
          ▄█████████████████▄     
         ██▀▀▀▀▀▀▀▀▀▀▀████████    
        ██              ███████   
       ██               ████████  
       █▀               ▀███████  
       █▄▄██▄   ▀█████▄  ▀██████  
       █▀███▄▀   ▄██▄▄█▀   █████▄ 
       █  ▀▀█     ▀▀   ▀   ██  ▀▄█
       █   █   ▄             ██ ██
       █  █▄▄▄▄█▄▀▄         ▄▄█▄█ 
       █  █▄▄▄▄▄▄ ▀▄        ▄ ▀█  
       █ █▄████▀██▄▀       █ ▀▀   
        ██▀ ▄▄▄▄   ▄▀    ▄▀█      
         █▄▀    ▀█▀█▀ ▄▄▀ ▄▀      
         ▀▄        ▄▄▀    █       
         ▄██▀▀▀▀▀▀▀       █▄      
      ▄▄▀   ▀▄          ▄▀ ▀▀▄    
    ▄▀▀       █▄      ▄▀      █▄  
    █                          ▀█▄"""
  print char_sting
  global char_name
  char_name = "Obama"

def character_yao():
  char_sting = """\n
            ███████████████        
         █████████████████████     
        ████████████████████████   
       ██████████████████████████  
      █████████████████████████████
      ███████████▀         ████████
      ███████████               ███
     ████████████                ██
     █  ███████           ▄▄     ██
    █    █████      ▄███████  ██  █
    █  █   ███     ██▀▀        ██ █
    █   █            ▄██▄       ███
    █  ▄█                  █▀▀█▄ ██
    █                      █    ██ 
     ███                   █    █  
      █ █       █     ██▀▄ ▄██   █ 
      █ █      █                 █ 
       ██      █    ▄▄▄▄▄▄      █  
       ██       █  █▄▄▄▄ ▀▀██  █   
       ██       █  ▀████████  █    
      █  █       █  ▀▄▄▄▄██  █     
      █   █       █         █      
     █     █                █      
            █      █        █      
                    ████████"""
  print char_sting
  global char_name
  char_name = "Yao"

def character_know_that_feel_bro():
  char_sting = """\n
           ▄▀▀▀▀▀▀▀▀▀▀▄▄
        ▄▀▀             ▀▄
      ▄▀                  ▀▄
      █                     ▀▄
     ▐▌        ▄▄▄▄▄▄▄       ▐▌
     █           ▄▄▄▄  ▀▀▀▀▀  █
    ▐▌       ▀▀▀▀     ▀▀▀▀▀   ▐▌
    █         ▄▄▀▀▀▀▀    ▀▀▀▀▄ █
    █                ▀   ▐     ▐▌
    ▐▌         ▐▀▀██▄      ▄▄▄ ▐▌
     █           ▀▀▀      ▀▀██  █
     ▐▌    ▄             ▌      █
      ▐▌  ▐              ▀▄     █
       █   ▌        ▐▀    ▄▀   ▐▌
       ▐▌  ▀▄        ▀ ▀ ▀▀   ▄▀
       ▐▌  ▐▀▄                █
       ▐▌   ▌ ▀▄    ▀▀▀▀▀▀   █
       █   ▀    ▀▄          ▄▀
      ▐▌          ▀▄      ▄▀
     ▄▀   ▄▀        ▀▀▀▀█▀
    ▀   ▄▀          ▀   ▀▀▀▀▄▄▄▄▄"""
  print char_sting
  global char_name
  char_name = "Bro"

def game():
  output = True
  player_name = raw_input("\nAt first introduce yourself. What\'s your name?\n")
  while(output):
    if player_name.strip():
      print "\nHello, " + player_name.strip() + "!"
      output = False
    else:
      player_name = raw_input("\nPlease enter something! What\'s your name?\n")
  select_character()
  print "Let\'s continue the game!"
  x_and_o()

def select_character():
  output = True
  character = raw_input("\nNow you need to select a character:\n1. Obama;\n2. Yao;\n3. Bro.\n")
  while(output):
    if character == "1":
      character_not_bad()
      output = False
    elif character == "2":
      character_yao()
      output = False
    elif character == "3":
      character_know_that_feel_bro()
      output = False
    else:
      character = raw_input("\nYOU ENTERED SOMETHING WRONG! PLEASE, SELECT A CHARACTER(1, 2 or 3):\n")
  print "You selected " + char_name + ", but are you sure?"
  choose = raw_input("\nSelect new character?\n1. Yes;\n2. No, continue game.\n")
  output = True
  while(output):
    if choose == "1":
      select_character()
      output = False
    elif choose == "2":
      output = False
    else:
      choose = raw_input("\nYOU ENTERED SOMETHING WRONG! PLEASE, SELECT 1 OR 2:\n")
  
def x_and_o():
  global cells
  global field_keys
  print "Now we will play simple game X\'s and O\'s:\n"
  print "Here is a field to play:"
  print """
  _|A|B|C|
  1|_|_|_|
  2|_|_|_|
  3|_|_|_|"""
  print "You need to enter 3 O\'s in a row: horizontal, vertical or diagonal. Like this:"
  print """
  _|A|B|C|
  1|0|_|_|
  2|_|0|_|
  3|_|_|0|"""

  cells = { "1A": " ",
            "1B": " ",
            "1C": " ",
            "2A": " ",
            "2B": " ",
            "2C": " ",
            "3A": " ",
            "3B": " ",
            "3C": " "}

  field_keys = cells.keys()

  print "Computer will start. You need to enter coordinates like this 1A, 3C, etc. Good luck!"
  while player_won() == False:
    comp_move()
    if computer_won() == False:
      if draw() == False:
        your_move()
      else:
        break
    else:
      break
  play_again()

def comp_move():
  global cells
  global field_keys
  print "Computer\'s move:"
  selection = random.choice(field_keys)
  cells[selection] = "X"
  field_keys.remove(selection)
  field =  "\n" \
           "_|A|B|C|\n" \
           "1|"+cells["1A"]+"|"+cells["1B"]+"|"+cells["1C"]+"|\n" \
           "2|"+cells["2A"]+"|"+cells["2B"]+"|"+cells["2C"]+"|\n" \
           "3|"+cells["3A"]+"|"+cells["3B"]+"|"+cells["3C"]+"|\n"
  print field

def your_move():
  global cells
  global field_keys
  output = True
  your_cell = raw_input("\nEnter coordinates of cell you want to enter. Your move:\n")
  while(output):
    if your_cell in field_keys:
      cells[your_cell] = "0"
      field =  "\n" \
               "_|A|B|C|\n" \
               "1|"+cells["1A"]+"|"+cells["1B"]+"|"+cells["1C"]+"|\n" \
               "2|"+cells["2A"]+"|"+cells["2B"]+"|"+cells["2C"]+"|\n" \
               "3|"+cells["3A"]+"|"+cells["3B"]+"|"+cells["3C"]+"|\n"
      field_keys.remove(your_cell)
      print field
      output = False
    elif your_cell == "Python the King":
      print "You win, cheater!"
      print """
      _|A|B|C|
      1|0|0|0|
      2|0|0|0|
      3|0|0|0|"""
      play_again()
      output = False
    else:
      your_cell = raw_input("\nThis cell is ocupated or you enter invalid character enter other:\n")

def computer_won():
  global cells
  computer_win = False
  combination_to_win = [["1A", "2A", "3A"], ["1B", "2B", "3B"], ["1C", "2C", "3C"], 
                        ["1A", "1B", "1C"], ["2A", "2B", "2C"], ["3A", "3B", "3C"], 
                        ["1A", "2B", "3C"], ["1C", "2B", "3A"]]                     
  for x in combination_to_win:
    all_x = []
    for i in x:
      if cells[i] == "X":
        all_x.append(cells[i])
    if len(all_x) == 3:
      print "COMPUTER WIN, YOU LOSE!"
      computer_win = True
      break
  return computer_win

def player_won():
  global cells
  player_win = False
  combination_to_win = [["1A", "2A", "3A"], ["1B", "2B", "3B"], ["1C", "2C", "3C"], 
                        ["1A", "1B", "1C"], ["2A", "2B", "2C"], ["3A", "3B", "3C"], 
                        ["1A", "2B", "3C"], ["1C", "2B", "3A"]]                    
  for x in combination_to_win:
    all_o = []
    for i in x:
      if cells[i] == "0":
        all_o.append(cells[i])
    if len(all_o) == 3:
      print "CONGRATULATIONS YOU WIN!"
      player_win = True
      break
  return player_win

def draw():
  global field_keys
  draw_result = False
  if (len(field_keys) == 0) and (player_won() == False) and (computer_won() == False):
    print "This is draw!"
    draw_result = True
  return draw_result

def play_again():
  output = True
  final = raw_input("\nWant to play again?\n1. Yes;\n2. No\n")
  while(output):
    if final == "1":
      x_and_o()
      output = False
    elif final == "2":
      print "\nBYE-BYE!"
      sys.exit()
    else:
      final = raw_input("\nYou entered something wrong\nWant to play again?\n1. Yes;\n2. No\n")

start()

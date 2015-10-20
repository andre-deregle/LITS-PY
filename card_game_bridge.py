#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
import random
deck = []
comp_tries = 0
your_tries = 0

def create_deck_of_cards():
  suits = ['♠', '♦', '♥', '♣']
  values = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
  global deck
  for suit in suits:
    for value in values:
      deck.append(value+suit)
  return deck

def hands_creation():
  create_deck_of_cards()
  global deck
  global comp_hand
  comp_hand = random.sample(deck, 5)
  for each in comp_hand:
    deck.remove(each)
    assert((each not in deck) == True), "Same card at Deck and at Comp Hand"
  global your_hand
  your_hand = random.sample(deck, 4)
  for each in your_hand:
    assert((each not in comp_hand) == True), "Same card at Your Hand and at Comp Hand"
  for each in your_hand:
    deck.remove(each)
    assert((each not in deck) == True), "Same card at Deck and at Your Hand"

def card_template_creation(card):
  if "10" in card:
    card_template = "┌─────────┐\n" \
                    "|"+card+"      |\n" \
                    "|         |\n" \
                    "|         |\n" \
                    "|   "+card+"   |\n" \
                    "|         |\n" \
                    "|         |\n" \
                    "|      "+card+"|\n" \
                    "└─────────┘"
  else:
    card_template = "┌─────────┐\n" \
                    "|"+card+"       |\n" \
                    "|         |\n" \
                    "|         |\n" \
                    "|   "+card+"    |\n" \
                    "|         |\n" \
                    "|         |\n" \
                    "|       "+card+"|\n" \
                    "└─────────┘"
  return card_template

def print_your_hand():
  global your_hand
  card_line = []
  for card in your_hand:
    card_template = card_template_creation(card)
    card_line.append(card_template)
  for index in range(len(card_template.split("\n"))):
    card_line_string = ""
    for each_card in card_line:
      card_line_string += each_card.split("\n")[index]
    print card_line_string

def print_comp_hand(hidden = False):
  global comp_hand
  card_line = []
  for card in comp_hand:
    if hidden:  
      card_template = "┌─────────┐\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "|░░░░░░░░░|\n" \
                      "└─────────┘"
    else:
      card_template = card_template_creation(card)
    card_line.append(card_template)
  for index in range(len(card_template.split("\n"))):
    card_line_string = ""
    for each_card in card_line:
      card_line_string += each_card.split("\n")[index]
    print card_line_string

def starting_card():
  global deck
  global start_card
  start_card = random.choice(deck)
  card_template = card_template_creation(start_card)
  deck.remove(start_card)
  print card_template

def game():
  global deck
  global your_hand
  global comp_hand
  global start_card

  for each in your_hand:
    if start_card[0:1] in each:
      first_your_card = raw_input("You have card with same value as start card, you need to put it.\n")
      output = True
      while output:
        if first_your_card[0:1] == start_card[0:1]:
          your_move(first_your_card)
          output = False
        else:
          first_your_card = raw_input("\nPlease, select card with same value!\n")
      break
  if is_card_special(start_card):
    special_card_actions(start_card, False, True)
  while your_win() == False:
    comp_move()
    if comp_win() == False:
      your_move()
    else:
      break

def is_card_special(card):
  if card[0:1] in ["6", "7", "8", "J", "A"]:
    return True
  else:
    return False

def special_card_actions(card, comp, you):
  global deck
  global comp_hand
  global your_hand
  if card[0:1] == "6":
    print "You got to cover card with another."
    if comp:
      comp_move()
    elif you:
      your_move()
  elif card[0:1] == "7":
    print "Opponent got to take two extra cards from deck and miss move."
    if comp:
      extra_cards = random.sample(deck, 2)
      your_hand.extend(extra_cards)
      for each in extra_cards:
        deck.remove(each)
      comp_move()
    elif you:
      extra_cards = random.sample(deck, 2)
      comp_hand.extend(extra_cards)
      for each in extra_cards:
        deck.remove(each)
      your_move()
  elif card[0:1] == "8":
    print "Opponent got to take one extra card from deck and make a move."
    if comp:
      extra_cards = random.sample(deck, 1)
      your_hand.extend(extra_cards)
      for each in extra_cards:
        deck.remove(each)
      your_move()
    elif you:
      extra_cards = random.sample(deck, 1)
      comp_hand.extend(extra_cards)
      for each in extra_cards:
        deck.remove(each)
      comp_move()
  elif card[0:1] == "J":
    print "You are selecting suit."
  elif card[0:1] == "A":
    print "Opponent miss a move."
    if comp:
      comp_move()
    elif you:
      your_move()

def rules():
  print "In this game you need to put card on another with same value or same suit. There are special cards, we will help you with that:"
  print "6 - you got to cover sixes with another card."
  print "7 - when you or opponent put seven, opponent or you got to take two extra cards from the deck and miss move."
  print "8 - when you or opponent put this eight, opponent or you got to take one extra card from the deck."
  print "J - Jack allows you or your opponent to select suit, it can differs from suit of the last card. Jack can be put on any suit."
  print "A - when you or your opponent put Ace, than opponent or you miss a move."
  print "\nCards of same values should be put together in one move."
  print """\n
When there is your move you got to enter value with suit. Suit you enter should be first capital letter of it:
♠ - Spade as S;
♦ - Diamond as D;
♥ - Heart as H;
♣ - Club as C;
So you need to put something like: 10S, AH etc.
"""
  print "\nLet\'s the game begin! Good luck!"

def comp_move():
  global deck
  global comp_hand
  global your_hand
  global start_card
  global comp_tries

  possible_moves = []
  for each in comp_hand:
    if "10" in each:
      print "Comp cards:"
      print each
      if each[0:2] == start_card[0:2]:
        possible_moves.append(each)
      if each[2:] == start_card[2:]:
        possible_moves.append(each)
    elif "10" not in each:
      print "Comp cards:"
      print each
      if each[0:1] == start_card[0:1]:
        possible_moves.append(each)
      if each[1:] == start_card[1:]:
        possible_moves.append(each)
  if (len(possible_moves) == 0) and (comp_tries == 0):
    additional_card = random.choice(deck)
    deck.remove(additional_card)
    comp_hand.extend(additional_card)
    global comp_tries
    comp_tries = 1
    print "Comp took additional card:"
    print_comp_hand(hidden = True)
    card_template = card_template_creation(start_card)
    print card_template
    print_your_hand()
    comp_move()
  elif (len(possible_moves) != 0):
    comp_tries = 0
    start_card = random.choice(possible_moves)
    comp_hand.remove(start_card)
  elif (len(possible_moves) == 0) and (comp_tries == 1):
    comp_tries = 0
    print "Comp has no card to make a move"
    print_comp_hand(hidden = True)
    print card_template
    print_your_hand()
    your_move()
  card_template = card_template_creation(start_card)
  print "Computer made a move:"
  print_comp_hand(hidden = True)
  print card_template
  print_your_hand()
  if is_card_special(start_card):
    special_card_actions(start_card, True, False)

def your_move(card = None):
  global deck
  global comp_hand
  global your_hand
  global start_card
  global your_tries

  if card != None:
    if card[-1] == "H":
      card = card[0:-1] + "♥"
    elif card[-1] == "S":
      card = card[0:-1] + "♠"
    elif card[-1] == "C":
      card = card[0:-1] + "♣"
    elif card[-1] == "D":
      card = card[0:-1] + "♦"
    start_card = card
  else:
    possible_moves = []
    for each in your_hand:
      if "10" in each:
        print each
        if each[0:2] == start_card[0:2]:
          possible_moves.append(each)
        if each[2:] == start_card[2:]:
          possible_moves.append(each)
      elif "10" not in each:
        print each
        if each[0:1] == start_card[0:1]:
          possible_moves.append(each)
        if each[1:] == start_card[1:]:
          possible_moves.append(each)
    print possible_moves
    if (len(possible_moves) == 0) and (your_tries == 0):
      additional_card = random.choice(deck)
      deck.remove(additional_card)
      your_hand.extend(additional_card)
      your_tries = 1
      print "You took additional card:"
      print_comp_hand(hidden = True)
      print card_template
      print_your_hand()
      your_move()
    elif (len(possible_moves) != 0):
      your_tries = 0
      start_card = random.choice(possible_moves)
      your_hand.remove(start_card)
    elif (len(possible_moves) == 0) and (your_tries == 1):
      your_tries = 0
      print "You have no card to make a move"
      print_comp_hand(hidden = True)
      print card_template
      print_your_hand()
      comp_move()
    selected_card = raw_input("Select your card to move:\n")
    output = True
    while output:
      if selected_card[-1] == "H":
        selected_card = selected_card[0:-1] + "♥"
      elif selected_card[-1] == "S":
        selected_card = selected_card[0:-1] + "♠"
      elif selected_card[-1] == "C":
        selected_card = selected_card[0:-1] + "♣"
      elif selected_card[-1] == "D":
        selected_card = selected_card[0:-1] + "♦"
      if selected_card in possible_moves:
        output = False
      else:
        selected_card = raw_input("You select impossible or incorrect card. Select your card to move:\n")
    start_card = selected_card
  card_template = card_template_creation(start_card)
  print "You made a move:"
  print_comp_hand(hidden = True)
  print card_template
  print_your_hand()
  if is_card_special(start_card):
    special_card_actions(start_card, False, True)

def comp_win():
  global comp_hand
  if len(comp_hand) == 0:
    return True
  else:
    return False

def your_win():
  global your_hand
  if len(your_hand) == 0:
    return True
  else:
    return False

hands_creation()
rules()
print_comp_hand(hidden = True)
starting_card()
print_your_hand()

game()

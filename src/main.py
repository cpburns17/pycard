
from game import Game
from player import Player
from deck import Deck
import ipdb

if __name__ == "__main__":
    '''
    Here we'll run simulations of our game playing, then print out the win 
    rate for each player. 
    '''

    player1 = Player("player 1")
    player2 = Player("player 2")
    deck = Deck()
    game = Game(p1=player1, p2=player2, deck=deck)
    game.play()
    for i in range(0,10):
        deck.reset()
        game = Game(player1, player2, deck)
        game.play()
    print(f"{player1.name}'s win rate {player1.win_rate}")
    print(f"{player2.name}'s win rate {player2.win_rate}")


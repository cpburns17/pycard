
from game import Game
from player import Player
from deck import Deck
import ipdb

if __name__ == "__main__":
    '''
    Here we'll run simulations of our game playing, then print out the win 
    rate for each player. 
    '''

    # import ipdb;
    # ipdb.set_trace()

    player1_name = input('Enter Player 1\'s name')
    player1 = Player(player1_name)
    player2_name = input('Enter Player 2\'s name')
    player2 = Player(player2_name)
    deck = Deck()
    game = Game(p1=player1, p2=player2, deck=deck)
    game.play()
    for i in range(0,10):
        deck.reset()
        game = Game(player1, player2, deck)
        game.play()
    print(f"{player1.name}'s win rate {player1.float_to_percent(player1.win_rate)}")
    print(f"{player2.name}'s win rate {player2.float_to_percent(player2.win_rate)}")


import random


class Card:

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def get_value(self):
        if self.rank == 'A':
            return 11
        elif self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
            return int(self.rank)

    def __str__(self):
        return f"{self.rank}{self.suit}"


class Deck:
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ["♠", "♥", "♦", "♣"]

    def __init__(self, number_of_decks=6):
        self.all_cards = []
        for _ in range(number_of_decks):
            for suit in Deck.suits:
                for rank in Deck.ranks:
                    self.all_cards.append(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def draw(self):
        if len(self.all_cards) < 20:
            print("Deck running low, reshuffling...")
            self.__init__(6)
            self.shuffle()
        return self.all_cards.pop()

    def __len__(self):
        return len(self.all_cards)


class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_score(self):
        score = 0
        aces = 0

        for card in self.hand:
            score += card.get_value()
            if card.rank == 'A':
                aces += 1

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1
        return score

    def show_hand(self):
        card_strs = [str(card) for card in self.hand]
        cards = ', '.join(card_strs)
        score = self.get_score()

        if score == 21 and len(self.hand) == 2:
            print(f"{self.name} cards: {cards} (Blackjack!)")
        else:
            print(f"{self.name} cards: {cards} ({score})")

    def reset_hand(self):
        self.hand = []


class Dealer(Player):

    def show_hand(self, reveal_all=False):
        if not reveal_all and self.hand:
            print(f"{self.name} cards: {self.hand[0]}, [Hidden]")
        else:
            super().show_hand()


class BlackjackGame:

    def __init__(self, num_decks=6):
        self.deck = Deck(num_decks)
        self.deck.shuffle()
        self.player = Player("Player")
        self.dealer = Dealer("Dealer")

    def deal_initial_cards(self):
        print("Dealing initial cards...")
        self.player.reset_hand()
        self.dealer.reset_hand()

        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

        self.dealer.show_hand()
        self.player.show_hand()

    def check_for_natural_blackjack(self):
        player_bj = self.player.get_score() == 21 and len(self.player.hand) == 2
        dealer_bj = self.dealer.get_score() == 21 and len(self.dealer.hand) == 2

        if player_bj or dealer_bj:
            print("\n*** Checking for Blackjack! ***")
            self.dealer.show_hand(reveal_all=True)
            if player_bj and dealer_bj:
                print("It's a PUSH! Both have Blackjack.")
            elif player_bj:
                print("Player WINS with Blackjack!")
            elif dealer_bj:
                print("Dealer WINS with Blackjack!")
            return True
        return False

    def player_turn(self):
        print("\n--- Player's Turn ---")
        while self.player.get_score() < 21:
            choice = input("Do you want to Hit (h) or Stand (s)? ").lower()

            if choice == 'h':
                self.player.add_card(self.deck.draw())
                print(f"Player hits: {self.player.hand[-1]}")
                self.player.show_hand()

                if self.player.get_score() > 21:
                    print("Player BUSTS! Dealer wins.")
                    return False

            elif choice == 's':
                print("Player stands.")
                break

            else:
                print("Invalid input. Please enter 'h' or 's'.")
        return True

    def dealer_turn(self):
        print("\n--- Dealer's Turn ---")
        print("Dealer reveals hand:")
        self.dealer.show_hand(reveal_all=True)

        while self.dealer.get_score() < 17:
            print("Dealer must hit (score is less than 17)...")
            self.dealer.add_card(self.deck.draw())
            print(f"Dealer hits: {self.dealer.hand[-1]}")
            self.dealer.show_hand(reveal_all=True)

        if self.dealer.get_score() > 21:
            print("Dealer BUSTS! Player wins.")
            return False

        print("Dealer stands.")
        return True

    def determine_winner(self):
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()

        print("\n--- Final Showdown ---")
        self.player.show_hand()
        self.dealer.show_hand(reveal_all=True)

        if player_score > dealer_score:
            print("\n🎉 Player WINS!")
        elif dealer_score > player_score:
            print("\n😔 Dealer WINS!")
        else:
            print("\n🤝 PUSH! It's a tie.")

    def play_round(self):
        self.deal_initial_cards()

        if self.check_for_natural_blackjack():
            return

        player_active = self.player_turn()

        if player_active:
            dealer_active = self.dealer_turn()

            if dealer_active:
                self.determine_winner()


if __name__ == '__main__':
    game = BlackjackGame()

    while True:
        game.play_round()

        play_again = input("\nDo you want to play another hand? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

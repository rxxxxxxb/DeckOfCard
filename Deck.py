import random 

class Card(): #Card Class for a single card 
    def __init__(self,card,value):
        self.card = card
        self.value = value

    def show(self):
        print("{} of {}".format(self.value,self.card))

class Deck: #Deck class
    def __init__(self):
        self.cards = []
        self.build()


    def build(self): #Build method for building deck
        for card in  ['Clubs',"Spades","Hearts",'Diamonds']:
            for val in range(1,14):
                self.cards.append(Card(card,val))


    def shuffle(self): # Shuffle method for shuffeling 
        l = len((self.cards)) #total number of cards
        for le in range(l):
            r = random.randint(0,le)
            self.cards[le],self.cards[r] = self.cards[r],self.cards[le]



    def show(self): #print built deck
        for v in self.cards:
            v.show()            


    def drawCard(self): #draw 1 card
        return self.cards.pop()    


class Player: #Player class
    def __init__(self,name):
        self.name = name
        self.hand = []

    def draw(self):
        for card in range(5): #Draw 5 Card for player
            self.hand.append(deck.drawCard())  

    def showHand(self): #SHow PLayer Cards
        for i in self.hand:
            i.show() 

    def discard(self): #Discard 1 Card
        return self.hand.pop()   


# clubs = Card("clubs","8")

# clubs.show()

deck = Deck()
deck.shuffle()
# #deck.show()
# deck.drawCard()
# deck.show()

cartman = Player("Cartman") #Create a plaer nammmed cartman 


cartman.draw()
print("---Showing hand---")
cartman.showHand()
print("------------------")
cartman.discard()
print("--Showing Hand again after Discarding---")
cartman.showHand()

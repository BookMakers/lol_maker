import csv

class Team:
    players = None

    def __init__(self, val):
        self.players = csv.DictReader(val)

        
            
    def removeOut(self):
        name = ''
        while(name != '~'):
            name = input("Please enter in an absent player: ")
            delEntry(self, 'Name', name)
            
    def delEntry(self, col, item):
        for row in self.players:
            if(row[col] == item):
                try:
                    del self.players[com]
                except:
                    print("Not in list")
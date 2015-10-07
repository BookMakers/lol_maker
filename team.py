"""
Team Compo:
TOP
MID
JNG
AD
SUP
FLEX
FLEX
TEAM 
"""

import csv
import copy

class Team:
    players = None
    team = {
    'TOP':'',
    'MID':'',
    'JNG':'',
    'AD':'',
    'SUP':'',
    'FLEX':'',
    'FLEX':'',
    'TEAM':''
    }


    def __init__(self, val):
        reader = csv.DictReader(val)
        self.players = [row for row in reader]
    def removeOut(self):
        name = ''
        remlist = []
        while(name != '-w'):
            name = input("Please enter in an absent player or -w to finish and write or -q to quit: ")
            if(name == '-q'):
                exit()
            if(self.delEntry('Name', name)):
                remlist.append(name)
                print("added")
            
        self.rewrite(remlist)
    def rewrite(self, rem):
        f = open('roster','r')
        roster = f.readlines()
        f.close()
        f = open('roster','w')
        for player in roster:
            bad = False
            for name in rem:
                if(name in player):
                    print("found")
                    bad = True
                    rem.pop(rem.index(name))
            if(not(bad)):
                f.write(player)
    
    def delEntry(self, col, item):
        for row in self.players:
            #print(row[col], item)
            if(item in row[col]):
                del row
                return True
    def build(self, budget):
        pass
        
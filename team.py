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
    team = []

    def __init__(self, val):
        reader = csv.DictReader(val)
        self.players = [row for row in reader]
                    
    def removeOut(self):
        name = ''
        while(name != '~'):
            name = input("Please enter in an absent player: ")
            self.delEntry('Name', name)
            
    def delEntry(self, col, item):
        for row in self.players:
            #print(row[col], item)
            if(item in row[col]):
                print("Found")
                return
            
        """
        for row in self.players:
            print(row[col])
            if(item in row):
                print("found")
                try:
                    print("deleted row " + row)
                    del row
                except:
                    print("Error")
        """
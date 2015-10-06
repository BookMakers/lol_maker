import csv
import urllib
players = None

def grabCsv():
    pass

def loadCsv():
    global players
    with open('DKSalaries.csv') as csvfile:
        players = csv.DictReader(csvfile)
        
        
def removeOut():
    pass

def makeTeam():
    global players
    

def main():
    grabCsv()
    loadCsv()
    removeOut()
    makeTeam()
    


main()
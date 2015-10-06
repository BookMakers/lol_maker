import csv
import urllib


def loadCsv():
    with open('DKSalaries.csv') as csvfile:
        players = csv.DictReader(csvfile)
        print(players.fieldnames)
        for row in players:
            #print(row)
            pass


def main():
    loadCsv()
    


main()
import requests
import os
import sys
from team import Team


url = "https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=26&draftGroupId=7387"

def grabCsv():
    try:
        return open("roster", "r")
    except:
        page = requests.get(url)
        roster = open("roster", "w")
        roster.write(page.text)
        roster.close
        return open("roster", "r")
def clean():
    os.remove('roster')
    

def main():
    if('-c' in sys.argv):
        clean()
    val = grabCsv()
    t = Team(val)
    t.removeOut()
    


main()
import requests
import os
import sys
import json
from team import Team


url = ""
budget = 0
config = None

def load():
    global config
    global url
    global budget
    config = json.loads(open('config.json','r').read())
    url = config["csv_url"]
    budget = int(config["budget"])
    return grabCsv()
    
    
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
    val = load()
    t = Team(val)
    
    if('-r' in sys.argv):
        t.removeOut()
        
    t.build(budget)
    


main()
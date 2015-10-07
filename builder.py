import requests
from team import Team


url = "https://www.draftkings.com/lineup/getavailableplayerscsv?contestTypeId=26&draftGroupId=7387"

def grabCsv():
    page = requests.get(url)
    return page.text

    

def main():
    val = grabCsv()
    t = Team(val)
    t.removeOut()
    


main()
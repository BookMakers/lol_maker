
team = {
    'TOP':{'Salary':'0'},
    'MID':{'Salary':'0'},
    'JNG':{'Salary':'0'},
    'ADC':{'Salary':'0'},
    'SUP':{'Salary':'0'},
    'FLEX1':{'Salary':'0'},
    'FLEX2':{'Salary':'0'},
    'TEAM':{'Salary':'0'}
}

def default(budget,players):
    global team
    pos = ''
    for player in players:
        
        choice = {
            'TOP':lambda pos: addTop(player),
            'MID':lambda pos: addMid(player),
            'JNG':lambda pos: addJng(player),
            'ADC':lambda pos: addAdc(player),
            'SUP':lambda pos: addSup(player),
            'TEAM':lambda pos: addTeam(player)
        }[player['Position']](pos)
    

    for player in team.items():
        print(player)
        
    return team
def addTop(player):
    global team
    if(player['Salary']>team['TOP']['Salary']):
        team['TOP'] = player
    
def addMid(player):
    global team
    if(player['Salary']>team['MID']['Salary']):
        team['MID'] = player
def addJng(player):
    global team
    if(player['Salary']>team['JNG']['Salary']):
        team['JNG'] = player
def addAdc(player):
    global team
    if(player['Salary']>team['ADC']['Salary']):
        team['ADC'] = player
def addSup(player):
    global team
    if(player['Salary']>team['SUP']['Salary']):
        team['SUP'] = player
def addTeam(player):
    global team
    if(player['Salary']>team['TEAM']['Salary']):
        team['TEAM'] = player
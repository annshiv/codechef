table = {'B':'BattleShip','C':'Cruiser','D':'Destroyer','F':'Frigate'}

for _ in range(int(input())):
    ID = input().upper()
    print(table[ID])


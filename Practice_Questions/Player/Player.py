class Player(object):
	def __init__(self, name, country, age, matches, runs, wicket):
		self.playerName = name
		self.playerCountry = country
		self.playerAge = age
		self.noOfMatches = matches
		self.noOfRuns = runs
		self.noOfWickets = wicket
		
	
class Team:
	def getMinRuns(self, playerObjects):
		playerObjects = sorted(playerObjects, key=lambda x: x.noOfRuns)
		return playerObjects[0]
		
	def getMaxWickets(self, playerObjects):
		playerObjects = sorted(playerObjects, key=lambda x: x.noOfWickets)
		return playerObjects[-1]
		
	
if __name__ == "__main__":
	n = int(input())
	team = list()
	for _ in range(n):
		name = input()
		country = input()
		age = int(input())
		matches = int(input())
		runs = int(input())
		wicket = int(input())
		team.append(Player(name, country, age, matches, runs, wicket))
		
	T = Team()
	minRuns = T.getMinRuns(team)
	maxWicket = T.getMaxWickets(team)
	print(f'{minRuns.playerName}\n{minRuns.noOfRuns}\n{minRuns.playerCountry}')
	print(f'{maxWicket.playerName}\n{maxWicket.noOfWickets}\n{maxWicket.playerCountry}')
	

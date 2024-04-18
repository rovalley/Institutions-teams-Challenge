institutions = set()
teams = set()
with open ("2015.csv", "r") as readFile:
    lines = readFile.readlines()
    for i in range(1,len(lines)):
        line = lines[i].strip()
        while '"' in line:
            firstQuote = line.index('"')
            secondQuote = line[firstQuote + 1:].index('"') + firstQuote + 1
            line = line[:firstQuote] + line[firstQuote + 1:secondQuote].replace(",","") + line[secondQuote + 1:]
        lineData = line.split(",")
        institutionName = lineData[0]
        city = lineData[2]
        stateProv = lineData[3]
        country = lineData[4]
        institutions.add((institutionName, city, stateProv, country))
        teamNumber = lineData[2]
        advisor = lineData[5]
        problem = lineData[6]
        ranking = lineData[7]
        teams.add((teamNumber, advisor, problem, ranking,(institutionName,city,stateProv,country)))

institutionIDByName = dict()
with open("Institutions.csv", "w") as file1:
    institutionID = 1
    file1.write("Institution ID,Institution Name,City,State/Province,Country\n")
    for institutionInfo in institutions:
        file1.write(str(institutionID))
        file1.write(",")
        file1.write(institutionInfo[0])
        file1.write(",")
        file1.write(institutionInfo[1])
        file1.write(",")
        file1.write(institutionInfo[2])
        file1.write(",")
        file1.write(institutionInfo[3])
        file1.write("\n")
        institutionIDByName[institutionInfo] = institutionID
        institutionID += 1

with open("Teams.csv", "w") as file1:

    file1.write("Team Number,Advisor,Problem,Ranking,Institution ID\n")
    for team in teams:
        file1.write(team[0])
        file1.write(",")
        file1.write(team[1])
        file1.write(",")
        file1.write(team[2])
        file1.write(",")
        file1.write(team[3])
        file1.write(",")
        institutionID = institutionIDByName[team[4]]
        file1.write(str(institutionID))
        file1.write("\n")



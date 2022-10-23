def findbyID(str,soup):
    try:
        b=soup.find_all("td",class_=str)
        classment=[]
        for i in b: 
            classment.append(i.getText())
        Classment=[]
        for i in classment:
            Classment.append(' '.join(i.split()))
        return Classment
    except:
        print(str,"not found")
        
class Team:
    def __init__(self,rank,name,points):
        self.rank=rank
        self.name=name
        self.points=points
    def __str__(self):
        return str(self.rank)+"----------"+self.name+"-----------"+str(self.points)
    
    
    
def getclassement(Country,Ligue):
    try:
        from bs4 import BeautifulSoup
        import requests
        data="https://www.footmercato.net/"+Country+"/"+Ligue+"/classement"
        page = requests.get(data)
        page
        soup = BeautifulSoup(page.content, 'html.parser')
        classment=findbyID("classement__rank",soup)
        team=findbyID("classement__team",soup)
        points=findbyID("classement__highlight",soup)
        Teams=[]
        for (a, b, c) in zip(classment, team, points):
            team=Team(a,b,c)
            Teams.append(team)
        return Teams
            
    except:
        print("not found")
        
        
class Ligue:
    def __init__(self,Country,name):
        self.Country=Country
        self.name=name
    
    def show(self):
        teams=getclassement(self.Country,self.name)
        for team in teams:
            print(team)
            
    def __str__(self):
        teamsnum=0
        teams=getclassement(self.Country,self.name)
        for team in teams:
            teamsnum+=1
        return self.name+"--------country: "+self.Country+"-------Teams number :"+str(teamsnum)
Action=True
country=input("country : ")
ligue=input("botola : ")  
while(Action):
    botola=Ligue(country,ligue)
    print("1 to get ligue info  \n2 to get the ranking table  \n3 to get new ligue \n0 to exit")
    inpt=input("your choise : ")
    match inpt:
        case "1":
            print(botola)
        case "2":
            botola.show()
        case "3":
            country=input("country : ")
            ligue=input("botola : ")  
        case "0":
            print("bye bye")
            Action = False
        case _:
            print("invalid input")
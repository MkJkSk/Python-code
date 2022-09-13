import json


with open("Content_jason.txt","r")as file:
    file_content = json.load(file)
    print(file_content['Customer'] [2] )

    cricket = [
          {"name": "Virat" ,    "Runs": 12000 },
          {"name": "sachin" ,   "Runs":34000 },
          {"name": "Rohit",     "Runs": 9000}

    ]


with open("Scorecard.txt","w")as file:

    json.dump(cricket,file)





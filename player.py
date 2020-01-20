from attributes import attdict, typdict, reqdict

class Player:

    def __init__(self, name):
        self.name = name
        self.question = ""
        self.char = ""
        self.chars = ""
        self.quest_att = ""
        self.quest_typ = ""
        self.request = ""

    def getQuestion(self):
        return "{}, {}, odpowiedź to: {}".format(attdict[self.quest_att], typdict[self.quest_typ], reqdict[self.request])
    
    def getQuestAtt(self):
        return attdict[self.quest_att]
    
    def getQuestTyp(self):
        return typdict[self.quest_typ]

class Event:
    def __init__(self, name, date, participants = 0):
        self.name = name
        self.date = date
        self.participants = participants
    
    def add_participant(self):
        self.participants += 1
        
    def get_participant_count(self):
        return self.participants
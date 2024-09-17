class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
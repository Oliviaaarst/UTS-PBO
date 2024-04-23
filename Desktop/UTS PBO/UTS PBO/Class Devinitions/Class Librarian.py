class Librarian:
    def __init__(self, member_id, name, addres, date_of_birth, email): 
        self.member_id = member_id
        self.name = name
        self.addres = addres
        self.date_of_birth = date_of_birth
        self.email = email

    def get_member_id(self):
        return self.member_id
    
    def get_name(self):
        return self.name
    
    def get_addres(self):
        return self.addres
    
    def get_date_of_birth(self):
        return self.date_of_birth
    
    def get_email(self):
        return self.email
    

member1 = Librarian("422023025", "Olivia Kristiani", "Bogor, Jawa Barat", "2004-13-10", "olivia.422023025@civitas.ac.id")


print("Member Information:")
print("Member ID:", member1.get_member_id())
print("Name:", member1.get_name())
print("Address:", member1.get_addres())
print("Date Of Birth:", member1.get_date_of_birth())
print("Email:", member1.get_email())


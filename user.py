
import datetime

class User:
    """A member, storing name and birthday
    for now """
    def __init__(self, full_name, birthday):
        self.name = full_name
        self.birthday = birthday ##yyyymmdd

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        """Returns the age of the user in years"""
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        today = datetime.date.today()
        dob = datetime.date(yyyy,mm,dd)
        age_in_days = (today - dob).days
        return int(age_in_days / 365)

    def legal_age(self):
        age = self.age()
        if age >= 18:
            return True
        else:
            return False

        
user = User("Sayed Miah", "19980831")
print(user.name)
print(user.first_name)
print(user.legal_age())

from user import User


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts=0):
        self.first_name = first_name
        self.last_name = last_name
        self.privileges = ['Allowed to add message', 'Allowed to delete users',
                           'Allowed to ban users']
        self.login_attempts = login_attempts

    def show_privileges(self):
        print(self.privileges)

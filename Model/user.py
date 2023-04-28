# User class
class User:

    # Constructor
    def __init__(self, user_name, user_email, user_password, role):
        self.user_name = user_name,
        self.user_email = user_email,
        self.user_password = user_password,
        self.role = role

    # Getters
    def getUserName(self):
        return self.user_name

    def getUserEmail(self):
        return self.user_email

    def getUserPassword(self):
        return self.user_password

    def getRole(self):
        return self.role

    # Setters
    def setUserName(self, user_name):
        self.user_name = user_name

    def setUserEmail(self, user_email):
        self.user_email = user_email

    def setUserPassword(self, user_password):
        self.user_password = user_password

    def setRole(self, role):
        self.role = role

    def user_info(self):
        return f'Nombre: {self.getUserName()}\nEmail: {self.getUserEmail()}\nPassword: {self.getUserPassword()}\nRole: {self.getRole()}'

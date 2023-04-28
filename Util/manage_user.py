from Model.role import *
from Model.user import *


def toFillUser(user, user_data):
    role = Role(user_data[3])

    # Fill user with data list
    User.setUserName(user, user_data[0])
    User.setUserEmail(user, user_data[1])
    User.setUserPassword(user, user_data[2])
    User.setRole(user, role.getRoleName())


def comparePasswords(user, password):
    return True if user.getUserPassword() == password else False

from Infrastructure.database import *
from Util.json_reader import *
from Util.manage_user import *
from Model.user import *

# Obtain connection string data
connection_tuple = readJson()

# Performance connection with DataBase
db_connection = configureConnection(connection_tuple)

email = str(input('Email:'))

query = f"SELECT * FROM Users u WHERE u.Email like '{email}'"

user_data = executeSimpleGetSql(db_connection, query)

user = User('', '', '', '')

toFillUser(user, user_data)

password = str(input(f'Password:'))


print('Login succes') if comparePasswords(
    user, password) else print('Access denied')

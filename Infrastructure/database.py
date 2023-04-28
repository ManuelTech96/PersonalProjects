import pyodbc

# Method to configure connection with database


def configureConnection(connection_list):

    # .strip() elimina los espacios en blanco de una cadena.
    # Si la cadena esta vacia devuelve false, si no, devuelve true
    if connection_list[0].strip() and connection_list[1].strip() and connection_list[2].strip() and connection_list[3].strip() and connection_list[4].strip():
        db_connection = pyodbc.connect(
            f'Driver={connection_list[0]};Server={connection_list[1]};Database={connection_list[2]};UID={connection_list[3]};PWD={connection_list[4]};')

    return db_connection

# Method to execute a query that return a unique value


def executeSimpleGetSql(db_connection, query):
    cursor = db_connection.cursor()
    cursor.execute(query)
    data_dic = []

    for row in cursor:
        values = row[1:]
        for value in values:
            data_dic.append(value)

    return data_dic

# Method to execute a query that retun True or False if the action was performed


def executePostSql(db_connection, query):
    cursor = db_connection.cursor()
    try:
        cursor.execute(query)
        return True
    except:
        return False

import json


def readJson():
    with open('F:\proyectos\proyecto1\Settings\settings.json', 'r') as f:
        config = json.load(f)

    driver = None
    server = None
    database = None
    uid = None
    pwd = None

    for connection in config['ConnectionStrings']:
        if connection['name'] == 'DataBase1':
            for conn in connection['connection_string']:
                driver = conn['driver']
                server = conn['server']
                database = conn['database']
                uid = conn['uid']
                pwd = conn['pwd']

    return (driver, server, database, uid, pwd)

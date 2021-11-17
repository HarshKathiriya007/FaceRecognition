def get_database():
    from pymongo import MongoClient
    import pymongo


    #CONNECTION_STRING = "mongodb+srv://admin:1234@Project_1.mongodb.net/Testcollection"
    CONNECTION_STRING = "mongodb+srv://admin:1234@cluster0.qthhh.mongodb.net/Testcollection?retryWrites=true&w=majority"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    print ("\n\n\n\n ********", client['Testcollection'])
    return client['Testcollection']


if __name__ == "__main__":    


    dbname = get_database()
    print("\n\n\n\n\n --------db", dbname)
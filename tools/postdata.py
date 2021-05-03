from config.configuration import collection

def insert_tweet(user_name,user_location,day,favorites,text):
    dict_insert = {"user_name": user_name,
    "user_location": user_location,
    "date": day,
    "favorites": favorites,
    "text": text
    }
    collection.insert_one(dict_insert)
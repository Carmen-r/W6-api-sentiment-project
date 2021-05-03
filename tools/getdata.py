from config.configuration import db, collection

def mensajespersona(person):
    """
    Funtion returns every tweet of a person in the database.
    """
    query = {"user_name": f"{person}"}
    tweets = list(collection.find(query,{"_id": 0}))
    return tweets

def mensajeslocation(location):
    """
    Funtion returns every tweet of a location in the database
    """
    query = {"user_location": f"{location}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

def mensajesdate(date):
    """
    Funtion returns every phrase of a date in the database
    """
    query = {"date": f"{date}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

def mensajeshashtag(hashtag):
    """
    Funtion returns every phrase of a hashtag in the database
    """
    query = {"hashtags": f"{hashtag}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

def mensajesfavorites(fav):
    """
    Funtion returns every phrase of favorites in the database
    """
    query = {"favorites": f"{fav}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

def date_hashtag(date,hashtag):
    """
    Funtion returns every phrase of a hashtag and date in the database
    """
    query = {"date": f"{date}", "hashtags": f"{hashtag}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

def location_date_hashtag(location,date,hashtag):
    """
    Funtion returns every phrase of a location, date and hashtag in the database
    """
    query = {"user_location": f"{location}", "date": f"{date}", "hashtags": f"{hashtag}"}
    tweet = list(collection.find(query,{"_id": 0}))
    return tweet

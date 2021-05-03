# API-SENTIMENT-PROYECT 

## GOAL ⚡️

This is a proyect is design to work with Apis, mongo DB, and sentiment analysis
The objetive of this proyect is to you create an API. The API will be able to receive information, store and serve it when you need.

## WHAT IS NEED? TOOLS 👀

Among other things for this project you need MongoDB, FLASK, collections, NLTK, pandas, functions.


## LIBRARIES 🤓

[Pandas][id]

[id]: https://pandas.pydata.org/  "Pandas"

[NumPy][id]

[id]: https://numpy.org/ "NumPy"

[Regex][id]

[id]: https://docs.python.org/3/library/re.html "Regex"

[TextBlob][id]

[id]: https://textblob.readthedocs.io/en/dev/ "TextBlob"

[WordCloud][id]

[id]:https://pypi.org/project/wordcloud/ "WordCloud"

[Matplotlib][id]

[id]: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html "Matplotlib"

[Os][id]

[id]: https://python101.pythonlibrary.org/chapter16_os.html "Os"

[Request][id]

[id]: https://docs.python-requests.org/en/master/ "Request"

[PyMongo][id]

[id]: https://pymongo.readthedocs.io/en/stable/ "PyMongodb"

[Dotenv][id]

[id]: https://pypi.org/project/python-dotenv/ "Dotenv"

## PROYECT 🧪

1.Import and clean a [Kaggle][id] dataset about the tweets of Covid Vaccines around the world.

[id]: https://www.kaggle.com/ "Kaggle"

2.Write an API using flask to receive tweets and store them in a database like mongodb 

3.Read and serve data from the chats database using different endpoints

4.Extract the emotional value of tweets

### Endpoints GET

     "http://0.0.0.0:5000/tweets/**person**/": Gives the tweets of the person you select
     
     "http://0.0.0.0:5000/favorites/**fav**/": Gives the tweets of the favorites numbers 
     
     "http://0.0.0.0:5000/locations/**location**/": Gives the tweets of the location you select
     
     "http://0.0.0.0:5000/dates/**date**/": Gives the tweets of the day you select
     
     "http://0.0.0.0:5000/hashtags/**hashtag**": Gives the tweets of the hashtags you select
     
     "http://0.0.0.0:5000/locations/**l**/dates/**d**/hashtags/**h**": Gives the tweets of the location, date and hashtag select
     

### Enpoints POST

    "http://0.0.0.0:5000/nuevafrase": Add a recent tweet


### Sentiment&Visualization 

1.Clean the text and separte the words
 
2.Sentimental Analysis with polarity and subjetivity, and emotion of the tweet. 

3.Visualization of the sentiments.


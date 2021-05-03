import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind

def clean_data(text):
    """
    Cleans the dataframe
    Args:
        text: Text of the dataframe that will be cleaned
    Returns:
        clean text
    """
    import regex as re
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#', '', text)
    text = re.sub(r'RT[\s]+', '', text)
    text = re.sub(r'https?:\/\/\S+', '', text)
    text = text.lower()
    return text

def wordcloud_tweet(tweets):
    """
    Most-tweeted words in texts containing the covid-19 vaccine seeing with word cloud
    Args:
        tweets: the text that is going to be stop
    """
    stopwords = set(STOPWORDS)
    stopwords.update(["covid", "covid19", "vaccines", "Â", "vaccine", "will", "coronavirus", "rt"])
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white",stopwords=stopwords, random_state = 2016).generate(" ".join([i for i in tweets['text'].str.upper()]))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")

def sentimentAnalysis(sentence):
    """
    Analize the sentiment of the text
    Args:
        sentence: text that is the object of the analysis
    Return:
        The dataFrame with the text compound
    """
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol

def grade_to_sent(grade):
    """
    Clasify the grades of the polarity and subjetivity in sentimients
    Args:
        grade: polarity and subjetivity
    Return:
        The classification in negative, positive and neutral.
    """
    if grade >= 0.05:
        return 'positive'
    elif grade <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def get_subjectivity(text):
    return TextBlob(text).sentiment.subjectivity

def get_polarity(text):
    return TextBlob(text).sentiment.polarity

def most_frequent_values(data):
    """
    Count the frequency value of the columns in the dataset
    Args:
        data: count the values of the dataframe
    Retuns:
        The dataFrame with the frequency
    """
    total = data.count()
    tt = pd.DataFrame(total)
    tt.columns = ['Total']
    items = []
    vals = []
    for col in data.columns:
        itm = data[col].value_counts().index[0]
        val = data[col].value_counts().values[0]
        items.append(itm)
        vals.append(val)
    tt['Most frequent item'] = items
    tt['Frequence'] = vals
    tt['Percent from total'] = np.round(vals / total * 100, 3)
    return(np.transpose(tt))

def plot_count(feature, title, df, size=1, ordered=True):
    f, ax = plt.subplots(1,1, figsize=(4*size,4))
    total = float(len(df))
    if ordered:
        g = sns.countplot(df[feature], order = df[feature].value_counts().index[:20], palette='Set3')
    else:
        g = sns.countplot(df[feature], palette='Set3')
    g.set_title("Number and percentage of {}".format(title))
    if(size > 2):
        plt.xticks(rotation=90, size=8)
    for p in ax.patches:
        height = p.get_height()
        ax.text(p.get_x()+p.get_width()/2.,
                height,
                '{:1.2f}%'.format(100*height/total),
                ha="center") 
    plt.show() 


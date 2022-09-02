from operator import contains
from timeit import repeat
import snscrape.modules.twitter as sntwitter
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import sys, os
from os import path
os.chdir(sys.path[0])

#twitter filter
query = "(#Sources, OR #NBA) (from:NbaTradeReport)"
tweets = ["Trade","Trades","trade","trades","Blockbuster Trade","blockbuster trade","Blockbuster trade","blockbuster Trade",
          "Trading","Deal","Free Agent", "FA", "Sign", "Signing","sign", "Signing"]
limit = 3000


#for loop for printing content
for tweet in sntwitter.TwitterHashtagScraper(query).get_items():
    
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.content])
        
#printing to csv file
df = pd.DataFrame(tweets, columns=['Tweet'])
print(df)

# save to csv file
df.to_csv('tweets.csv')

# Read text
text = open('tweets.csv', mode='r', encoding='utf-8').read()

#STOPWORDS
nba_logo = np.array(Image.open(path.join( "NBA-icon.png")))
stopwords = set(STOPWORDS)
stopwords.add("NBA")


wc = WordCloud(background_color="white", max_words=2000, mask=nba_logo,
               stopwords=stopwords, max_font_size=40, random_state=42)


wc.generate(text)

#Adding color to the image based off images original color
image_colors = ImageColorGenerator(nba_logo)
wc.recolor(color_func=image_colors)

#storing word cloud to file
wc.to_file('wordcloud_output.png')
import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []

# scrape 100 tweets from username FMoHealth with hashtag #covid19ethiopia
for count,tweet in enumerate(sntwitter.TwitterSearchScraper('from:FMoHealth #covid19ethiopia').get_items()): 
    if count>100:
        break
    tweet_without_commas = tweet.content.replace(",", "")
    numbers = [numbers for numbers in tweet_without_commas.split() if numbers.isdigit()]
    if len(numbers) == 4:

        attributes_container.append([tweet.date, numbers[0], numbers[1], numbers[2], numbers[3]])
    
# Creating a dataframe from the tweets list above 
tweets_df = pd.DataFrame(attributes_container, columns=["Date Tweeted","Period(Hrs)", "Samples Tested", "New Infections", "Total Infections"])
tweets_df.to_csv("downloads/ethiopia_twitter.csv", index=False)

import json
import re
import pandas as pd
import matplotlib.pyplot as plt


## Appends data to json format

tweets_data_path = 'new.txt'
tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue

## Filtering and organizing tweets by country and number of tweets

tweets = pd.DataFrame()
tweets['text'] = list(map(lambda tweet: tweet['text'], tweets_data))
tweets['lang'] = list(map(lambda tweet: tweet['lang'], tweets_data))
tweets['country'] = list(map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data))


tweets_by_lang = tweets['lang'].value_counts()

print("Plotting")
fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('languages', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

tweets_by_country = tweets['country'].value_counts()

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Countries', fontsize=15)
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('top 5 countries', fontsize=15, fontweight='bold')
tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')



def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['uber'] = tweets['text'].apply(lambda tweet: word_in_text('uber', tweet))
tweets['lyft'] = tweets['text'].apply(lambda tweet: word_in_text('lyft', tweet))
tweets['taxi'] = tweets['text'].apply(lambda tweet: word_in_text('taxi', tweet))

print(tweets['uber'].value_counts()[True])
print(tweets['lyft'].value_counts()[True])
print(tweets['taxi'].value_counts()[True])


prg_langs = ['uber', 'lyft', 'taxi']
tweets_by_prg_lang = tweets['uber'].value_counts()[True], \
                     tweets['lyft'].value_counts()[True], \
                     tweets['taxi'].value_counts()[True]

x_pos = list(range(len(prg_langs)))
print(x_pos)
print(tweets_by_prg_lang)
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_prg_lang)


## Setting axis labels and ticks"""

ax.set_ylabel('Number of tweets', fontsize=15)
ax.tick_params(axis='x', labelsize=15)
ax.set_title('Ranking: uber vs. lyft vs. taxi (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(prg_langs)
ax.set_xlabel('prg_langs', fontsize=15)
plt.grid()
plt.show()



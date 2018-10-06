import praw
import numpy as np
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

class PRAWW:
    common_words = ["http","https","com","www","imgur","r","a","about","all","are","an","also","and","as","at","be","because","but","by","can","come","could","day","do","deleted","even","find","first","for","from","get","give","go","have","he","her","here","him","has","his","how","i","is","if","in","into","it","its","it's","i'm","just","know","like","look","make","man","many","me","more","my","new","no","not","now","of","on","one","only","or","other","our","out","people","say","see","she","so","some","take","tell","than","that","the","their","them","then","there","these","they","thing","think","this","those","time","to","two","up","use","very","want","was","way","we","were","well","what","when","which","who","will","with","would","year","you","your"]

    def __init__(self):
        self.reddit = praw.Reddit(client_id='Wa_QQy6c8J6w_Q',
                     client_secret='i7XCwT6iYlE4O1wLqjJCfDRsFV0',
                     user_agent='diggity_diggity_doge')
        self.word_count = 0

    def get_comments_top_year(self, subreddit, number, group):
        texts = []
        labels = []
        for submission in self.reddit.subreddit(subreddit).top('year', limit=number):
            submission.comment_sort = 'top'
            submission.comments.replace_more(limit=0)
            for top_level_comment in submission.comments:
                texts.append(self.parse_comment(top_level_comment.body))
                labels.append(group)
        return (texts, labels)

    def get_comments_top_all(self, subreddit, number, group):
        texts = []
        labels = []
        for submission in self.reddit.subreddit(subreddit).top(limit=number):
            submission.comment_sort = 'top'
            submission.comments.replace_more(limit=0)
            for top_level_comment in submission.comments:
                texts.append(self.parse_comment(top_level_comment.body))
                labels.append(group)
        return (texts, labels)

    def get_comments_hot(self, subreddit, number, group):
        texts = []
        labels = []
        for submission in self.reddit.subreddit(subreddit).hot(limit=number):
            submission.comment_sort = 'top'
            submission.comments.replace_more(limit=0)
            for top_level_comment in submission.comments:
                texts.append(self.parse_comment(top_level_comment.body))
                labels.append(group)
        return (texts, labels)
    

    def parse_comment(self, comment):
        comment_arr = []
        new_comment = comment.translate ({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        for word in new_comment.split():
            self.word_count = self.word_count + 1
            if word.lower() not in self.common_words:
                comment_arr.append(word.lower())
        return " ".join(comment_arr)


    def tokenize_words(self, texts):
        max_words = 10000

        tokenizer = Tokenizer(num_words=max_words)
        tokenizer.fit_on_texts(texts)
        return tokenizer    

    def generate_occurance_data(self, tokenizer):
        word_counts = tokenizer.word_counts
        sorted_by_value = sorted(tokenizer.word_counts.items(), key=lambda kv: kv[1])

        data = pd.DataFrame(sorted_by_value, columns=['word', 'count']).tail(25)
        print(data.info())
        print(data)
        data.plot(kind='bar')

    

p = PRAWW()
(texts, labels) = p.get_comments_top_year('me_irl', 5, 0)
print(pd.DataFrame(texts).shape)
token = p.tokenize_words(texts)
p.generate_occurance_data(token)
# political-alignment

Politics are a large dividing factor in our country, and online discussions frequently become heated with political ideologies. On Reddit, a social forum-based website, communities called subreddits (sub) are passionate about specific issues. Often, it is confusing to determine the political viewpoints of each community.

My project can show the political stance of a specific sub. This helps users decide which communities have like-minded individuals and which have opposing viewpoints. It accomplishes this through creating graphs and networks of common words and phrases in the comment section of a post. It then uses a trained neural network to determine whether the subreddit leans politically right or left. This information can also be used to create targeted posts and advertisements specific to a subreddit, assuring optimal marketing strategies.

My project uses the PRAW Reddit wrapper to scrape for comments from different posts. Comments can be scraped from 'hot', top of all year, and top of all time posts. This data is then parsed, tokenized, and fed into a RNN (Recurrent Neural Network). Comment data is also counted and fed into another network to determine the relationships between words. This model achieved a classification accuracy of 73%, with graphs succinctily showing the gathered information.

In the future, I plan to increase the accuracy of the model by collecting more data and parsing it better. I would like to implement lemmatization, and my stopword list could be improved. The ultimate goal is for the network to accept a comment and generate the opposite viewpoint. As for data visualization, everything could be pushed to a Python/Angular website that would allow easier access.

subreddit_analysis.ipynb would be the notebook to run.

It needs Jupyter Notebook, Keras, Pandas, Numpy, Sklearn, and Matplotlib
Download the entire project and install required libraries
# **Fanalytics: Find Your Bandwagon**

NBA league makes >$1 billion from merchandise annually. Meanwhile, there is a online sports forum wiht 2.7 million NBA fans. In order to capitalize on this big fan group, NBA could push ads for jerseys and gear to those users. On this forum, half of the fans have already tagged themselves as fans of a certain team. So, it is convinient to push team-specific ads to those users. However, for the other half of the users, how can we identify their favorite teams?  
I took a Natural Language Processing approach to classify fans' teams by their comments and visiting history. By applying different feature extraction techniques and an ensemble model, the prediction reached a classificaiton accuray of 60%, which is 18.8x to the chance level and 2.2x to the MVP model.   
![approach](https://github.com/bearsun/insight_code/raw/master/figures/approach.png)
![performance](https://github.com/bearsun/insight_code/raw/master/figures/performance.png)
With this model, NBA could make about $607k from merchandise. My model could also generate to any online sports forums.  


## List of Other Files

### Week 1

scrapping data using reddit api praw  
./notebooks/praw_scrap_pilot.ipynb  

EDA for week 1 demo  
./notebooks/Wk1_Demo.ipynb  

### Week 2

scrapping all NBA 18-19 regular season thread IDs from pushshift api (directory of all posts)  
./notebooks/pushshift_scrap_submissions_reg18.ipynb  

scrapping all regular season threads/comments from praw api (all data)  
./notebooks/praw_scrap_comments_reg18.ipynb  

NLP, model training, etc. for week 2 demo  
./notebooks/Wk2_mvp.ipynb  

### Week 3
scrapping all users' comment history (which subreddits they commented before)  
./notebooks/scrap_user_history.ipynb  

updated models for week 3 demo  
./notebooks/Wk3_ner_textrank.ipynb  

code to run Name Entity Recognition (NER)  
./scripts/ner1.py  

code to run TextRank keyword extraction  
./scripts/textrank.py  

### miscs

dictionary of {team names : team abbrev.}  
./notebooks/teams

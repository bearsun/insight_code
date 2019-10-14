# **Fanalytics: Find Your Bandwagon**

NBA league makes >$1 billion from merchandise annually. Meanwhile, there is an online sports forum with 2.7 million NBA fans. In order to capitalize on this large fan group, NBA could push ads for jerseys and gear to those users. On this forum, half of the users have already tagged themselves as fans of a certain team. So, it is convenient to push team-specific ads to those users. However, for the other half of the users, how do we identify their favorite teams?  

I took a Natural Language Processing approach to classify fans' teams by their comments and visiting history on other forums. By applying different feature extraction techniques and an ensemble model, the prediction reached a classification accuracy of 64%, which is 20x to the chance level and 2.2x to my MVP model.  

With my model, NBA could make about $648k from merchandise. My model could also be applied to other online sports forums.  

![approach](https://github.com/bearsun/insight_code/raw/master/figures/approach.png)
![performance](https://github.com/bearsun/insight_code/raw/master/figures/performance.png)

## Webapp: NBA Fan Identifier
[Type in your comment then we can tell which NBA team you like](http://datadriveway.me/).  

## Presentation on the project
[Insight Project](https://sites.google.com/site/liweisunpro/insight)  

## Dependencies
* Data Scraping:
  * [praw 6.3.1](https://praw.readthedocs.io/en/latest/)
* NLP:
  * [spaCy 2.1.8](https://spacy.io/)
  * [gensim 3.7.3](https://radimrehurek.com/gensim/)
* Machine Learning:
  * [scikit-learn 0.21.2](https://scikit-learn.org/stable/)
  * [imblearn 0.5.0](https://imbalanced-learn.readthedocs.io/en/stable/index.html)
## Usage
* Scrap data
  1. Scrap titles/ids of all comment threads:  
    python ./scripts/scraping/pushshift_scrap.py (Also see ./notebooks/pushshift_scrap_submission_reg18.ipynb)
  2. Scrap all comments  
    python ./scripts/scraping/praw_scrap.py (Also see ./notebooks/praw_scrap_comments_reg18.ipynb)
  3. Scrap users' visiting history  
    python ./scripts/scraping/praw_scrap_history.py (Also see ./notebooks/scrap_user_history.ipynb)

* Run models  
  ./notebooks/Wk3_Final_Model.ipynb

## Overview of notebooks
* Week 1: Pilot data scraping and EDA  
  ./notebooks/Wk1_pilot_EDA.ipynb  
* Week 2: Building a MVP model  
  ./notebooks/Wk2_EDA_MVP.ipynb  
* Week 3: Optimizing the model and creating an ensemble model  
  ./notebooks/Wk3_Final_Model.ipynb  
## List of other scripts
Run Named Entity Recognition with spaCy  
./scripts/ner.py  

Run TextRank keywords extraction with gensim  
./scripts/textrank.py  

Load all data  
./scripts/load_data.py  

Preprocess texts, remove emoji, special charactors, etc.  
./scripts/preprocess.py  

Standerdize all team names in training data into 3 letters (e.g. TOR)  
./scripts/teamname_stdize.py  

Calculate AUC for a model  
./scripts/cal_auc.py  

A simple unit test for cal_auc  
./scripts/test_cal_auc.py  

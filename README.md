# BERT for Sequence Classification 

Solution repository for WNUT-2020 Shared Task 2 : Identification of informative COVID-19 English Tweets

Link to paper : https://www.aclweb.org/anthology/2020.wnut-1.47/

Team Name : Phonemer

Username : anshul.wadhawan

Private Leaderboard Global Rank : 6 (F1-score = 0.9037)

Task : Classification of COVID-19 related tweets into informative/uninformative given training data of 8000 tweets.

Methodology : Used BERT-large model pre-trained on 22.5 million COVID-19 tweets. Inculcated ensemble learning by fine tuning on 7 subsets of labelled data for sequence classification using PyTorch to get an F1-score of 90.36% on unseen test data of 2000 tweets. Performed bagging (ensemble) of 7 models, each trained on a randomly shuffled subset of training data (7000 tweets) to get an increase in F1 score by 0.8% on test set when compared with the best model trained on the whole training data (8000 tweets).

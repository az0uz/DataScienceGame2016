
MVA2016 datascience game 2016

code to train and test models

### Bonus
 'Leaderboard.py' let you track best submissions in real time, with stdev, mean and number of submissions per teams

# 1. Compute 5-fold
 run the python notebook profiling.ipynb, this will:
 - give insignt and statistics about the data
 - compute 'fold_train.csv' a 5-fold separation taking user into account

# 2. Compute Augmented Features (train and test)
 run the python notebook features.ipynb on train, validation and test values, this will:
 - compute the augmented features 'AugmentedFeatures{Train|Test|Priv}.csv'

# 3. Learn LDA
  run lda_topics_learn.ipynb to get
  - 'lda_alex_5_topics.p'
  - 'topics_alex.dict'

# 4. compute LDA features
  use 'lda_features_generator_traintest.ipynb' or 'lda_features_generator_priv.ipynb' to get LDA features in file:
  'lda_features_5_{train|test|priv}_topics_df.csv'

# train XGboost
  run the 'Xgboost_v7.ipynb' several time and change the parameter 'fold_value' from 0 to 4 to get several models
  (change the output file for each run)

# compute probability
  run 'Test_final_prediction.ipynb' specifying the model file to get the Y_{train|test|priv}.predict

# Submit #1
  run 'Bagging_vfinal.ipynb' choosing the 5 folds results file

# Submit #2
  run 'PearsonCorrelations.ipynb' on all models (we trained 11 different ones), to choose the 4 least correlated
  then run 'Bagging_vfinal.ipynb' to get results using the choosen models


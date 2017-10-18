#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    File Name: TMDB.py
    Date: 10/14/2017
    Author: hackrflov
    Email: hackrflov@gmail.com
    Python Version: 2.7
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

movie_df = pd.read_csv('../input/tmdb_5000_movies.csv')
credit_df = pd.read_csv('../input/tmdb_5000_credits.csv').drop('title', axis=1)
train_df = pd.merge(movie_df, credit_df, how='outer', left_on='id', right_on='movie_id').drop('movie_id', axis=1)
train_df.head()

###### Overlook ######
# Q: Which features are available in the dataset?
train_df.columns.values
# A: We got 22 available features

# Q: Which features are categorical/numerical/mixed data types?
train_df.head()
# A: Categorical fields: [categorical] homepage, original_title, tagline, title, overview, original_language, status [ordinal]
# A: Numerical fields: [continuous] popularity, runtime, vote_average [discrete] id, budget, revenue, release_date, vote_count
# A: Mixed fileds: [numeric+alpha] genres, keywords, production_companies, cast, crew [alpha] production_countries, spoken_lagunages

# Q: Which features may contain errors or typos?
train_df.tail()
# A: homepage, overview, tagline, cast, crew

# Q: Which features contain blank, null or empty values?
train_df.info()
# A: homepage > tagline > overview > runtime > release_date

# Q: What are the data types for various features?
train_df.info()
# A: 7 features are integer or floats, 15 features are strings

# Q: What is the distribution of numerical features across the samples?
train_df.describe(percentiles=[.1,.2,.3,.4,.5,.6,.7,.8,.9,.99])
# A: We got 5,000 samples from 460,000 total set.
# A: Budget varies significantly with few movies(<1%) costing 380,000,000.
# A: 90% of popularities are less than 50, while the max one is 875.
# A: The mean of revenue is nearly three times of budget.
# A: Most movie runtimes fall between 87 and 132 minutes.
# A: 40% of vote scores are smaller than 6.0, far from perfection.
# A: vote count has similar features with popularity

# Q: What is the distribution of categorical features?
train_df.describe(include=['O'])
#train_df['status'].describe(include=['O'])
# A: Some fields(original_titles, overview, tagline, title, cast, crew) are almost unique across the sample.
# A: Genres has suitable kinds and freq, and the most frequent genres, drama, accounts for 7.7%.
# A: English is the most popular language within 544 kinds of languages in the sample.

###### Assumption ######
# Q: Which features may have correlation with dependent data?
# A: Genres, keywords, original_language, production_companies, production_countries, release_date

# Q: Which features need to be completed?
# A: release_date, runtime

# Q: Which features need to be corrected?
train_df = train_df.drop(['homepage','id'], axis=1)
train_df.info()
# A: homepage, id

# Q: Which features need to be created?
# A: language, tag, company, country


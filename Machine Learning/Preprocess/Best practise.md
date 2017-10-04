# Workflow goals
- Classifying.
- Correlating.
- Converting.
- Completing.
- Correcting.
- Creating.
- Charting.

Step 1. Analyze by describing data
------------------------------------
### Overlook Phase
+ **Q: Which features are available in the dataset?**  
  A: print `df.columns.values` to preview both indepedent and dependent params.
+ **Q: Which features are categorical/numerical/mixed data types?**  
  A: use `df.head()`, `df.tail()`, `df.info()` to distinguish data types.
+ **Q: Which features may contain errors or typos?**  
  A: use `df.sample()` to check errors.
+ **Q: Which features contain blank, null or empty values?**  
  A: use `df.info()` to count size for each column.
+ **Q: What are the data types for various features?**  
  A: use `df.info()` to get types. 
+ **Q: What is the distribution of numerical feature values across the samples?**   
  A: use `df.describe()` to get mean/std/min/max and other statistics values.
+ **Q: What is the distribution of categorical features?**  
  A: use `df.describe(include=['0'])` to get unique/top/freq and other values.
### Assumption Phase
+ **Q: Which features may have correlation with *dependent data*?**  
  A: use experience with sample data to judge, and even add fields if needed.
+ **Q: Which features need to be completed?**  
  A: whichever contains missing data and satisfies correlation.
+ **Q: Which features need to be corrected?**  
  A: non-related or non-regular features should be dropped.
+ **Q: Which features need to be created?**  
  A: integrate fields, extract fields, convert continous numerical(distinct) to ordinal categorical(range),...

Step 2. Analyze by pivoting features
------------------------------------
1. choose features you want to gain insight upon. Let's say f1, f2, f3, ..., fn.
2. use following function to get features' impact: df[[fm, d]].groupby([fm]), as_index=False).mean().sort_values(by=d, ascending=False) [m: 1~n, d: dependent feature]
3. draw conclusions from tables and establish rough ranks in mind.

Step 3. Analyze by visualizing data
-----------------------------------
1. choose prime features from observations in step 2.
2. use `seaborn.FacetGrid()` to highlight pivotal fields.
3. think which features to be dropped/added/converted.

Step 4. Wrangle data
--------------------
1. correct by dropping features to focus.
2. create new features extracting from existing. (with one goal: simplify our data structure)
3. create new features combining existing features. 
4. complete categorical features.
5. convert categorical feature to numerical. (text to number)
6. complete and convert numerical features. (distinct to range)


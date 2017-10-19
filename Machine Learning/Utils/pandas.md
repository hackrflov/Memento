```python
# Aggreagtion
df[['a','b']].groupby('a').agg(['mean','count']).sort_values(by=[('b','mean')], ascending=False)
```

## Cheat-sheet
+ df.value_counts(): show how many rows for each unique value
+ df.shape()
+ df.corr(): Compute pairwise correlation of columns, excluding NA/null values
+ s.unique(): return all unique values in series
+ s.isin(): return boolean array showing existing status in every position
+ s.str.startswith(): return boolean Series/array indicating whether each string in the Series/Index starts with passed pattern.

+ pd.to_datetime()
+ pd.get_dummies(): Convert categorical variable into dummy/indicator variables
+ pd.cut(): Return indices of half-open bins to which each value of x belongs

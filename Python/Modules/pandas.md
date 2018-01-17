```python
# Aggreagtion
df[['a','b']].groupby('a').agg(['mean','count']).sort_values(by=[('b','mean')], ascending=False)

# Write to multiple sheets
from pandas import ExcelWriter
writer = ExcelWriter(xls_path)
df.to_excel(writer, sheet_name='sn')
writer.save()
```

## Cheat-sheet
+ df.value_counts(): show how many rows for each unique value
+ df.shape()
+ df.corr(): Compute pairwise correlation of columns, excluding NA/null values
+ df.sort_index(): Sort object by labels (along an axis)
+ df.pivot(): Produce 'pivot' table based on 3 columns of this DataFrame. Uses unique values from index / columns and fills with values.
+ df.drop(): Return new object with labels in requested axis removed.
+ df.reset_index(): Transfer index values(multi-index) into columns.
+ df.set_value(): Put single value at passed column and index (deprecated, use .at instead)
+ df.at[index, col]: Use to access and modify cell
+ s.unique(): return all unique values in series
+ s.isin(): return boolean array showing existing status in every position
+ s.str.startswith(): return boolean Series/array indicating whether each string in the Series/Index starts with passed pattern.
+ mi.swaplevel(): Swap level i with level j. Do not change the ordering of anything

+ pd.to_datetime()
+ pd.get_dummies(): Convert categorical variable into dummy/indicator variables
+ pd.cut(): Return indices of half-open bins to which each value of x belongs

+ ~s: inverse boolean series


```python
# Write to same excel
writer = pd.ExcelWriter(path)
df.to_excel(writer, sheetname, encoding='utf-8', index=False, float_format='%.2f')
writer.save()

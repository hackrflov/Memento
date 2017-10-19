+ Axis grids:
    - FacetGrid(): Subplot grid for plotting conditional relationships.
```python
import seaborn as sns
import matplotlib.pyplot as plt
g = sns.FacetGrid(data, col='a', row='b')   
g = g.map(plt.hist, 'c')   # c is the target feature 
```
    - PairGrid(): Subplot grid for plotting pairwise relationships in a dataset.
```python
g = sns.PairGrid(data)
g = g.map(plt.scatter)
```
    - jointplot(): Draw a plot of two variables with bivariate and univariate graphs.
```python
g = sns.jointplot(x='a', y='b', data=data)
```
+ Categorical plots:
    - boxplot(): Draw a box plot to show distributions with respect to categories.  
```python
ax = sns.boxplot(x='a', y='b', data=data) 
```
+ Distribution plots:
    - distplot(): Flexibly plot a univariate distribution of observations.
```python
x = np.random.normal(size=100)
sns.distplot(x)
```
+ Matrix plots:
    - heatmap(): Plot rectangular data as a color-encoded matrix.
```python
sns.heatmap(data, cmap=cmap)
```
+ Color palettes:
    - diverging_palette(): Make a diverging palette between two HUSL colors.
```python
cmap = sns.diverging_palette(240, 10, n=9)
sns.palplot(cmap)
```

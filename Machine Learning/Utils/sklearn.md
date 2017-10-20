## Pipeline: chaining estimators
Pipeline serves two purposes:
- Convenience and encapsulation 
- Joint parameter selection
- Safety  

```python
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.decomposition import PCA
pipe = make_pipline(PCA(), SVC())
pipe.steps[0]
pipe.fit(X_train, y_train)
```

## Preprocessing data
### Standardization, or mean removal and variance scaling

### Binarization
Applied if the input data is distributed according to a multi-variate Bernoulli distribution.
```python
from sklearn import preprocessing
binarizer = preprocessing.Binarizer().fit(X)
binarizer.transform(X)
```

### Encoding categorical features
Instead convert and form an order, we use one-hot encoder to encode categorical features.
```python
enc = preprocessing.OneHotEncoder()
enc.fit(origin_df)
new_df = enc.transform(to_change_df)
```

### Imputation of missing values
A better method than just discarding entire row is that we fill the blank with the mean, meadian or mode of the row of column.
```python
imp = preprocessing.Imputer(missing_values='NaN', strategy='mean', axis=0)
imp.fit(X)
imp.transform(X)
```

### Generating polynomial features


## GridSearchCV
`model_selection.GridSearchCV(estimator, param_grid)`  
Exhaustive search over specified parameter values for an estimator. 






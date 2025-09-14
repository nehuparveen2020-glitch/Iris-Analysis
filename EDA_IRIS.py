import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   

def remove_outliers(col):
    sorted(col)
    Q1,Q3 = col.quantile([0.25,0.75])
    IQR = Q3 - Q1
    lower_range = Q1 - (1.5 * IQR)
    upper_range = Q3 + (1.5 * IQR)
    return lower_range, upper_range


# To read dataset
df = pd.read_csv(r"C:\Users\nehup\Downloads\IRIS.csv")
print(df.head())
print(df.shape)
print(df.info())
print(df.describe())

# To check for duplicates
dups = df.duplicated()
print("Number of duplicate rows = %d " %(dups.sum()))
df[dups]

# To remove duplicates
df.drop_duplicates(inplace=True)
print("\nAfter removing duplicates rows = %d " %(df.duplicated().sum()))
print(df.shape)

# To check outliers as boxplot using for loop
for col in df.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        sns.boxplot(df[col])
        plt.show()

# To remove outliers by calling remove_outliers function
for col in df.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        lower_range, upper_range = remove_outliers(df[col])
        df = df[(df[col] > lower_range) & (df[col] < upper_range)]

print(df.shape)

# To check for outliers in categorical columns
for col in df.columns:
    if df[col].dtype == 'object':
        sns.boxplot(df[col])
        plt.show()
# No outliers in categorical columns

# To chech whether outliers are treated or not
for col in df.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        sns.boxplot(df[col])
        plt.show()

# To chek for missing values in all columns
print(df.isnull().sum())

# No missing values in dataset so no use of imputation(Mean, median, mode)

print(df.dtypes)

# Univariate analysis
for col in df.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        sns.distplot(df[col])
        plt.show()

# Bivariate analysis
for col in df.columns:
    if df[col].dtype == 'int64' or df[col].dtype == 'float64':
        sns.scatterplot(x=df[col],y=df['sepal_length'])
        plt.show()

# Multivariate analysis
sns.pairplot(df)
plt.show()











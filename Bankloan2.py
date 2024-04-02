import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Loading the Dataset
data = pd.read_csv(r'C:\Users\Sumit Prajapat\PycharmProjects\pythonBANKProject1\application_data (1).csv')


# Univariate Analysis
# Calculate descriptive statistics
descriptive_stats = data[['TARGET', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY']].describe()
print("Descriptive Analysis:")
print(descriptive_stats)

# Create histograms for numeric variables
plt.figure(figsize=(12, 6))
plt.subplot(131)
plt.hist(data['AMT_INCOME_TOTAL'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Income Total')
plt.ylabel('Frequency')
plt.title('Histogram - Income Total')

plt.subplot(132)
plt.hist(data['AMT_CREDIT'], bins=20, color='blue', edgecolor='black')
plt.xlabel('Credit Amount')
plt.ylabel('Frequency')
plt.title('Histogram - Credit Amount')

plt.subplot(133)
plt.hist(data['AMT_ANNUITY'], bins=20, color='lightgreen', edgecolor='black')
plt.xlabel('Annuity Amount')
plt.ylabel('Frequency')
plt.title('Histogram - Annuity Amount')

plt.tight_layout()
plt.show()

# Segmented Univariate Analysis
# Segmenting data based on 'TARGET' and analyzing 'AMT_INCOME_TOTAL'
income_segments = data.groupby('TARGET')['AMT_INCOME_TOTAL']

# Calculate descriptive statistics for each segment
income_segment_stats = income_segments.describe()
print("\nSegmented Univariate Analysis - 'AMT_INCOME_TOTAL':")
print(income_segment_stats)

# Create box plots to visualize the distribution of 'AMT_INCOME_TOTAL' for each segment
plt.figure(figsize=(8, 6))
sns.boxplot(x='TARGET', y='AMT_INCOME_TOTAL', data=data)
plt.title("Segment Univariate Analysis")
plt.xlabel("Loan Default")
plt.ylabel("Income Total")
plt.show()

# Bivariate Analysis
# Bivariate Analysis using scatter plot
sns.FacetGrid(data, hue="TARGET", height=5).map(plt.scatter, "AMT_ANNUITY", "AMT_CREDIT").add_legend()
plt.title("Bivariate Analysis")
plt.xlabel("AMT_ANNUITY")
plt.ylabel("AMT_CREDIT")
plt.show()
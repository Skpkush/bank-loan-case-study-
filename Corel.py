import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the Dataset
data = pd.read_csv(r'C:\Users\Sumit Prajapat\PycharmProjects\pythonBANKProject1\application_data (1).csv')

data_cleaned = data.dropna()

# case 1: Clients with payment difficulties (target == 1)
payment_difficulties = data[data['TARGET'] == 1]

# case 2: Clients with no payment difficulties (targat == 0)
no_payemnt_difficulties = data[data['TARGET'] == 0]


# Step 2: Calculate and visualize correlations
def plot_correlation_heatmap(data, title, selected_columns):
    # selecting numerical column and droping non numerical
    numeric_data = data[selected_columns].select_dtypes(include='number').drop(columns='TARGET')

    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f', vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

# List of important columns to consider for correlation analysis
numerical_columns = ['TARGET', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY', 'AMT_GOODS_PRICE', 'DAYS_BIRTH',
                     'DAYS_EMPLOYED']

# Correlations for payment difficulties
plot_correlation_heatmap(payment_difficulties, "Correlation Heatmap", numerical_columns)
# Correlations for no payment diff.
plot_correlation_heatmap(no_payemnt_difficulties, "Correlation Heatmap", numerical_columns)

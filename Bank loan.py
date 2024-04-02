import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Loading the Dataset
data = pd.read_csv(r'C:\Users\Sumit Prajapat\PycharmProjects\pythonBANKProject1\application_data (1).csv')

#Missing Data
missing_data = data.isnull().sum()
missing_value = missing_data / len(data)
print(missing_value)

#ploting Missing Data
plt.figure(figsize=(10, 6))
missing_value.plot(kind='bar')
plt.title('Missing Values ')
plt.xlabel('Variables')
plt.ylabel('Missing Values')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#Remove missing
data_cleaned = data.dropna()

#specific columns for outlier analysis
columns_for_outliers = ["AMT_INCOME_TOTAL", "AMT_CREDIT", "AMT_ANNUITY", "AMT_GOODS_PRICE"]

#Outliers using IQR Method
outliers = pd.DataFrame()

for column_name in columns_for_outliers:
    Q1 = data[column_name].quantile(0.25)
    Q3 = data[column_name].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR



    column_outliers = data[(data[column_name] < lower_bound) | (data[column_name] > upper_bound)].copy()
    column_outliers["Column"] = column_name
    outliers = pd.concat([outliers, column_outliers])

# Step 2: Visualize Outliers using Box Plots
plt.figure(figsize=(12, 8))
data.boxplot(column=columns_for_outliers)
plt.title("Outliers")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()

# Step 3: Print Quantile Analysis
print("Quantile Analysis for the specified columns:")
for column_name in columns_for_outliers:
    Q1 = data[column_name].quantile(0.25)
    Q3 = data[column_name].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    print(f"{column_name}:")
    print(f"  1st quartile (Q1): {Q1:.2f}")
    print(f"  3rd quartile (Q3): {Q3:.2f}")
    print(f"  Interquartile Range (IQR): {IQR:.2f}")
    print(f"  Lower Bound: {lower_bound:.2f}")
    print(f"  Upper Bound: {upper_bound:.2f}")
    print()

# Step 4: Print the Outliers
print("Outliers in the specified columns:")
print(outliers[columns_for_outliers + ["Column"]])


#Task: 3 data Imbalanced
#Calculate the target
class_for1 = data["TARGET"].value_counts()
class_for0 = data["TARGET"].value_counts(normalize=True)

# Step 2: Print the class for 0 and 1
print("Class for0:")
print(class_for0)

print("\nClass for1:")
print(class_for1)


# Step 3: Visualize for target variable
plt.figure(figsize=(6, 6))
colors = ['darkblue', 'darkred']
plt.pie(class_for1, labels=class_for1.index, colors=colors, startangle=90, shadow=True,autopct='%1.1f%%')
plt.axis('equal')  # pie chart
plt.title('Data Imbalanced')
plt.legend(labels=['Repaid', 'Not Repaid'])
plt.show()

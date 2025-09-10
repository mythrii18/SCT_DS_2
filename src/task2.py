# TASK 2- PERFORMING DATA CLEANING AND EXPLORATORY DATA ANALYSIS
# DATASET- HEART DISEASE DATASET (CLEVELAND)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\MYTHRI  MR\OneDrive\Desktop\SCT_DS_2\data\Heart_disease_cleveland_new.csv")
# 1. Data Cleaning
print("\n🔹 Dataset Shape:", df.shape)
print("\n🔹 Column Names:", df.columns.tolist())
print("\n🔹 Missing Values:\n", df.isnull().sum())
print("\n🔹 Summary Statistics:\n", df.describe())
print("\n🔹 Duplicates:", df.duplicated().sum())

df = df.drop_duplicates()


#2. Exploratory Data Analysis
fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# Target distribution
sns.countplot(data=df, x="target", palette="Set2", ax=axes[0])
axes[0].set_title("Target Distribution")

# Age distribution
sns.histplot(df["age"], bins=20, kde=True, color="skyblue", ax=axes[1])
axes[1].set_title("Age Distribution")

# Sex vs Heart Disease
sns.countplot(data=df, x="sex", hue="target", palette="Set1", ax=axes[2])
axes[2].set_title("Sex vs Heart Disease")

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
# Chest Pain Type vs Target
sns.countplot(data=df, x="cp", hue="target", palette="coolwarm", ax=axes[0])
axes[0].set_title("Chest Pain vs Heart Disease")

# Cholesterol distribution
sns.histplot(df["chol"], bins=30, kde=True, color="green", ax=axes[1])
axes[1].set_title("Cholesterol Distribution")

# Resting BP distribution
sns.histplot(df["trestbps"], bins=20, kde=True, color="orange", ax=axes[2])
axes[2].set_title("Resting BP Distribution")
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(10,7))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# Load the population dataset
df = pd.read_csv("API_SP.POP.TOTL_DS2_en_csv_v2_127006.csv", skiprows=4)

# Filter relevant columns: Country Name and Year 2022
df_2022 = df[['Country Name', '2022']].dropna()

# Sort and take top 20 countries by population
top_20 = df_2022.sort_values(by='2022', ascending=False).head(20)

# Plotting
plt.figure(figsize=(12, 7))
plt.bar(top_20['Country Name'], top_20['2022'], color='skyblue')
plt.title('Top 20 Most Populated Countries (2022)')
plt.ylabel('Population')
plt.xticks(rotation=75)
plt.tight_layout()
plt.show()

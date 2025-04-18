import pandas as pd

file_path= "earthquakes2.csv"
df=pd.read_csv(file_path)
print(df.head())

df.dropna(inplace=True)
df['Time']=pd.to_datetime(df['Time'])
df.drop_duplicates(inplace=True)
print(df.info())

import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10, 6))
sns.histplot(df['Magnitude'], bins=30, kde=True, color="blue")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.title("Distribution of Earthquake Magnitudes")
plt.show()

deepest_earthquakes = df.nlargest(10, 'Depth (km)')
print(deepest_earthquakes[['Time', 'Place', 'Depth (km)', 'Magnitude']])

import folium

# إنشاء خريطة تتمركز عند متوسط الإحداثيات
m = folium.Map(location=[df['Latitude'].mean(), df['Longitude'].mean()], zoom_start=2)

# إضافة نقاط الزلازل
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=row['Magnitude'] * 2,  # حجم الدائرة بناءً على القوة
        popup=f"Magnitude: {row['Magnitude']}\nDepth: {row['Depth (km)']} km",
        color='red' if row['Magnitude'] >= 5 else 'blue',
        fill=True,
        fill_color='red' if row['Magnitude'] >= 5 else 'blue'
    ).add_to(m)

# عرض الخريطة
m

df['Year'] = df['Time'].dt.year  # استخراج السنة من عمود الوقت
earthquakes_per_year = df['Year'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x=earthquakes_per_year.index, y=earthquakes_per_year.values, marker="o", color="purple")
plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.title("Number of Earthquakes per Year")
plt.grid(True)
plt.show()

import numpy as np
df.to_csv("earthquakes_cleaned.csv", index=False, encoding='utf-8')



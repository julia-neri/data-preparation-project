df = df.dropna()
df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
print("\nData after cleaning:")
print(df.head())
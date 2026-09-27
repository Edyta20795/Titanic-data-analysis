import pandas as pd

# Wczytanie danych
df = pd.read_csv("titanic.csv")

# Podstawowe informacje o danych
print("Podstawowe info:")
print(df.info())

# Sprawdzenie liczby pustych wartości
print("\nBraki danych w każdej kolumnie:")
print(df.isnull().sum())

# Usuwanie wierszy z pustymi wartościami (prosta metoda)
df_clean = df.dropna()

print("\nLiczba wierszy po wyczyszczeniu:")
print(len(df_clean))

# Podstawowe statystyki
print("\nStatystyki:")
print(df_clean.describe())

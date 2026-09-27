#dodawanie bibliteki pandas
import pandas as pd

# Wczytanie danych
df = pd.read_csv("titanic.csv")

# Basic data information
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

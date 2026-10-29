import pandas as pd

# 1. Cargar el dataset original (100%)
df = pd.read_csv("heart-disease.csv")

# 2. Guardar la versión completa (100%)
df.to_csv("heart_100.csv", index=False)

# 3. Guardar la versión al 50%
df_50 = df.sample(frac=0.5, random_state=42)
df_50.to_csv("heart_50.csv", index=False)

# 4. Guardar la versión al 25%
df_25 = df.sample(frac=0.25, random_state=42)
df_25.to_csv("heart_25.csv", index=False)

print("¡Archivos generados con éxito!")

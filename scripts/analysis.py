import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('../data/processed/primates_dataset.csv')

# Comparação da Expectativa de Vida entre as Diferentes Dietas
plt.figure(figsize=(10, 6))
sns.barplot(x='diet', y='avg_lifespan', data=df, palette='viridis')
plt.title('Comparação da Expectativa de Vida entre Diferentes Dietas')
plt.xlabel('Dieta')
plt.ylabel('Expectativa de Vida (anos)')
plt.savefig('../data/processed/img/comparacao_expectativa_vida_dieta.png')
plt.show()


# Comparação da População Absoluta das Espécies por Dieta
plt.figure(figsize=(10, 6))
sns.barplot(x='diet', y='population', data=df, palette='viridis')
plt.title('Comparação da População Absoluta das Espécies por Dieta')
plt.xlabel('Dieta')
plt.ylabel('População')
plt.savefig('../data/processed/img/comparacao_populacao_dieta.png')
plt.show()

# Comparação da População Absoluta das Espécies por Dieta e Região
plt.figure(figsize=(10, 6))
sns.barplot(x='habitat_region', y='population', hue='diet', data=df, palette='viridis')
plt.title('Comparação da População Absoluta das Espécies por Dieta e Região')
plt.xlabel('Dieta')
plt.ylabel('População')
plt.legend(title='Região de Habitat')
plt.savefig('../data/processed/img/comparacao_populacao_dieta_regiao.png')
plt.show()

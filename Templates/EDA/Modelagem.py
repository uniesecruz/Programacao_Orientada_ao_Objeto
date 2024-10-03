import pandas as pd
import matplotlib.pyplot as plt

class AnaliseExploratoria:
    def __init__(self):
        self.data=None
    def read_data(self,path):
        self.data=pd.read_csv(path)
        return self.data

    def summarize(self,data):
        if self.data is not None:
            return self.data.describe()
        else:
            return "não carregado"

    def value_counts(self,column):
        if self.data is not None:
            return  self.data[column].value_counts()
        else:
            return "Não carreegado"


# Classe para geração de gráficos
class GeradorGraficos:
    def grafico_linhas(self, data, x_col, y_col):
        """Gera um gráfico de linhas entre duas colunas especificadas."""
        if data is not None:
            plt.figure(figsize=(10, 6))
            plt.plot(data[x_col], data[y_col], marker='o', linestyle='-')
            plt.title(f'Gráfico de Linhas: {x_col} vs {y_col}')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.grid(True)
            plt.show()
        else:
            print("Nenhum dado foi fornecido.")

    def grafico_barras(self, data, x_col, y_col):
        """Gera um gráfico de barras entre duas colunas especificadas."""
        if data is not None:
            plt.figure(figsize=(10, 6))
            plt.bar(data[x_col], data[y_col])
            plt.title(f'Gráfico de Barras: {x_col} vs {y_col}')
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            plt.show()
        else:
            print("Nenhum dado foi fornecido.")

    def histograma(self, data, col, bins=10):
        """Gera um histograma para uma coluna específica."""
        if data is not None:
            plt.figure(figsize=(10, 6))
            plt.hist(data[col], bins=bins, edgecolor='black')
            plt.title(f'Histograma de {col}')
            plt.xlabel(col)
            plt.ylabel('Frequência')
            plt.show()
        else:
            print("Nenhum dado foi fornecido.")
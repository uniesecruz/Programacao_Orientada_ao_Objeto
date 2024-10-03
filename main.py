from Templates.EDA.Modelagem import AnaliseExploratoria
from Templates.EDA.Modelagem import GeradorGraficos
analise = AnaliseExploratoria()

dados = analise.read_data("D:\Python\calculo\pacientes.csv")

summario=analise.summarize(dados)
#
# contagem=analise.value_counts("ID")

# print((summario))


graficos = GeradorGraficos()

graficos.grafico_linhas(dados,'ID', 'Idade')
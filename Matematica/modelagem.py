class Funcoes:
    def __init__(self,x,p=None):
        self.x=x
        self.p=p

    def calcular_media(self):
        if self.x is not None and len(self.x) > 0 :
            somatorio = sum(self.x)
            n = len(self.x)
            return  somatorio / n

        else:
            return "divido por zero"

    def calcular_media_ponderada(self):
        if self.x is not None and self.p is not  None and len(self.x)  == len(self.p) and len(self.x) > 0:
            somatorio_pesos_valores = sum(p*x for p,x in zip(self.p,self.x))
            somatorio_pesos = sum(self.p)
            if somatorio_pesos == 0 :
                return "Divisão por zero"
            return somatorio_pesos_valores/somatorio_pesos
        else:
            return "Erro: listas de valores e pesos devem ter o mesmo tamanho, e não podem "



x = [10, 20]
p = [1,2]
media_calculadora  = Funcoes(x)
media = media_calculadora.calcular_media()
print(f"A média dos valores {x} é {media}")

# Cálculo da média ponderada
media_ponderada_calculadora = Funcoes(x, p)
media_ponderada = media_ponderada_calculadora.calcular_media_ponderada()
print(f"A média ponderada dos valores {x} com os pesos {p} é {media_ponderada}")
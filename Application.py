import matplotlib.pyplot as plt
import numpy as np

# Dados/amostras que serão utilizados como exemplo
# Diâmetros (cm)
Diametros = [[7], [10], [15], [30], [45]]

# Preços (R$)
Precos = [[8], [11], [16], [38.5], [52]]

# Define a label do eixo X
plt.xlabel('Diâmetro(cm)')
# Define a label do eixo Y
plt.ylabel('Preço(R$)')
# Define o título do plot
plt.title('Diâmetro x Preço')
# Plota o gráfico com os dados. O terceiro parâmetro "k." é uma format string, pra definir se no gráfico, será uma linha ou pontos e etc.
plt.plot(Diametros, Precos, 'k.')
# Define os limites dos eixos. Afeta na visualização dos dados.
plt.axis([0, 60, 0, 60])
# Define se o gráfico deve ter linhas de grade.
plt.grid(True)
# Função para mostrar o plot.
plt.show()

from sklearn.linear_model import LinearRegression

# Parâmetros X e Y com os valores do Diâmetro e Preço, respectivamente
X = [[7], [10], [15], [30], [45]]
Y = [[8], [11], [16], [38.5], [52]]

# Instancia o modelo de Regressão linear
modelo = LinearRegression()

# Treina o modelo com os dados fornecidos
modelo.fit(X, Y)

# Printa na tela com a "previsão" desejada. Note que o 20 não está entre os dados fornecidos. Isso significa que
# o algoritmo, através de Regressão Linear, achou a relação matemática entre o diâmetro e preço, e fez a "previsão".
print("Uma pizza de 20 cm de diâmetro deve custar: R$%.2f" % modelo.predict([20][0]))

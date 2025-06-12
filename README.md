# predicao-equipamento
Link: https://predicao-equipamento-meczwcnanonsuuxlwnau6c.streamlit.app/
Projeto Final — Sistema de Gerenciamento de Equipamentos Industriais
Título
Sistema de Gerenciamento de Equipamentos Industriais com Previsão de Preço e Classificação de Categoria

Contexto e Motivação
Uma empresa do setor industrial contratou a equipe de desenvolvimento para criar um sistema inteligente que otimize o gerenciamento de seus equipamentos.

Essa empresa possui uma variedade de máquinas e instalações, com diferentes características técnicas, níveis de tecnologia, consumo energético e necessidades de manutenção.

Com o objetivo de melhorar a precificação de novos equipamentos e oferecer atendimento personalizado aos clientes, o sistema proposto deve atender a duas frentes principais:

Previsão de Preço: Estimar o valor de venda com base nas características técnicas, usando modelos de regressão.
Classificação de Categoria: Atribuir automaticamente uma classe (A, B, C...) ao equipamento com base em seu perfil técnico.
Objetivos do Sistema
Criar um modelo preditivo para estimar o preço de venda com base em dados históricos.
Desenvolver um modelo de classificação para categorizar os equipamentos.
Realizar análise exploratória e tratamento de dados adequados para alimentar os modelos.
Armazenar os dados tratados em um banco de dados MySQL.
Apresentar os resultados usando BI (Business Intelligence) ou slides com storytelling.
Tecnologias e Ferramentas Utilizadas
Linguagem: Python
Bibliotecas: pandas, numpy, matplotlib, seaborn, sklearn
Banco de dados: MySQL
Ambiente de desenvolvimento: Google Colab
Etapa 2 — Entendimento do Problema
Tipos de Problemas Envolvidos
O projeto envolve dois tipos principais de problemas de Aprendizado de Máquina:

1. Previsão de Preço (Regressão)
Objetivo: Estimar o valor de venda de um equipamento industrial com base em suas características técnicas.

Tipo de problema: Regressão supervisionada

Variável alvo (target): preco

Exemplo de entrada:

potência = 4800
durabilidade = 3 anos
com_software = sim
iot = não
etc.
Saída esperada:

preco = 37.500,00 (valor estimado)
Modelos candidatos:

Regressão Linear
Árvore de Regressão
Random Forest Regressor
Huber Regressor
XGBoost Regressor
Métricas utilizadas:

RMSE (Root Mean Squared Error)
MAE (Mean Absolute Error)
R² (Coeficiente de Determinação)
2. Classificação da Categoria (Classificação)
Objetivo: Classificar o equipamento em uma categoria (A, B, C, D ou E) de acordo com seu perfil técnico.

Tipo de problema: Classificação supervisionada

Variável alvo (target): classe

Exemplo de entrada:

peso = 2
durabilidade = 4
sistema_refri = sim
tecnologia = 3
etc.
Saída esperada:

classe = C (categoria atribuída)
Modelos candidatos:

Decision Tree
Random Forest
K-Nearest Neighbors
Logistic Regression
XGBoost Classifier
Métricas utilizadas:

Acurácia
F1-score
Matriz de Confusão
Relatório de Classificação
Por que resolver esses dois problemas?
Melhorar a precificação automática, evitando erros humanos e otimizando a margem de lucro.
Ajudar o time de vendas a oferecer equipamentos adequados ao perfil do cliente.
Aumentar a confiabilidade das recomendações e decisões da empresa com base em dados reais.
Etapa 3 — Dataset
Fonte de Dados
Os dados foram fornecidos pela empresa industrial contratante e representam características técnicas de equipamentos já vendidos, junto com seus preços e categorias atribuídas.

Cada linha do dataset representa um equipamento industrial, com variáveis numéricas, categóricas e booleanas.

Atributos do Dataset
Campo	Tipo	Descrição
preco	Numérico	Valor de venda do equipamento em reais.
classe	Categórica	Categoria atribuída ao equipamento (A, B, C, D, E).
potencia	Numérico	Potência do equipamento (ex: em Watts ou HP).
peso	Numérico	Peso do equipamento (ex: em toneladas).
durabilidade	Numérico	Vida útil estimada do equipamento, em anos.
tecnologia	Numérico	Tipo de tecnologia utilizada:
1 = convencional
2 = automatizada
3 = embarcada
4 = avançada
necessidade_energia	Booleano	Requer energia elétrica? (sim/não)
requere_manutencao	Booleano	Requer manutenção periódica? (sim/não)
sistema_refri	Booleano	Possui sistema de refrigeração? (sim/não)
com_software	Booleano	Possui software embarcado? (sim/não)
iot	Booleano	Possui conectividade IoT? (sim/não)
garantia	Numérico	Período de garantia, em faixas:
0 = até 12 meses
1 = até 24 meses
2 = até 36 meses
3 = até 48 meses
status	Categórica	Situação de manutenção:
• sem manutenção
• em manutenção
• revisado
Observações
A variável preco será usada como alvo (target) no problema de regressão.
A variável classe será usada como alvo no problema de classificação.
As variáveis booleanas precisarão ser transformadas em valores numéricos para uso nos modelos.
Valores discrepantes (outliers) e dados faltantes devem ser identificados e tratados na próxima etapa (EDA).
Etapa 4 — Análise Exploratória de Dados (EDA)
A análise exploratória é uma etapa essencial para compreender a estrutura, os padrões, e possíveis problemas nos dados.

Estatísticas Descritivas
Vamos visualizar medidas como média, mediana, desvio padrão, mínimo e máximo para os dados numéricos.

Além disso, verificaremos:

Frequência das variáveis categóricas
Presença de valores nulos
Distribuições
Outliers (valores discrepantes)
Correlação entre variáveis
Objetivos do EDA:
Entender a distribuição dos dados
Identificar padrões e relações
Detectar outliers
Preparar os dados para modelagem

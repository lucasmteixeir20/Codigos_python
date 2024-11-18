
import pandas as pd
import numpy as np
from datetime import datetime
import os

dicionario ={
    'CPF': ['023.875.320-40', '234.768.560-60', '300.800.800-90', '600.900.300-50'],
    'FORNECEDOR': ['000230', '000340', '000900', '048589'],
    'VALOR': ['500', '1000', '600', '500'],
    'CENTRO_CUSTO': ['34050', '1061', '6041', '56040']}

print(dicionario)

# Transformar o dicionario em um dataframe

df = pd.DataFrame(dicionario)

# Extrair o primeiro algarismo

df['Primeiro_algarismo'] = df['CENTRO_CUSTO'].astype(str).str[0].astype(int)

# Quantidade Caracteres

df['Quantidade_Caracteres'] = df['CENTRO_CUSTO'].astype(str).str.len()

# Validação Empresa Promil x Soldi

df['Empresa'] = np.where(
    (df['CENTRO_CUSTO'].astype(str).str[0].astype(int)>=3) & 
    (df['CENTRO_CUSTO'].astype(str).str.len() == 5),'Promil','Soldi')

# Validação Moeda 

df['BRL'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','','BRL')

# Validacao Cambio

df['Taxa_Cambio'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','','100')

# Validação Data

df['Data_transacao'] = pd.to_datetime(datetime.today().date())

# Validação tipo de Conta 

df['Tipo_de_Conta'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','','Fornecedor')

# Validação codigo fornecedor

df['Conta'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','',df['FORNECEDOR'])

# Validação estabelecimento fiscal

df['Dimensao_Estabelecimeto_fiscal'] = np.where(df['Empresa'] == 'Promil','000130','000190')

# Validação Dimensao Produto

df['Dimensao_Produto'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','','')

# Validacao Dimensao_correspondente

df['Dimensao_correspondente'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','','')

# Validacao_Dimensao_Ponto

df['Dimensao_ponto'] = np.where(df['CENTRO_CUSTO'].str.strip() == '','',df['CENTRO_CUSTO'])

# Validação_dimensao_departamento 

df['Dimensao_departamento'] = ''

# Validação Descricao

df['Descricao'] = 'RESQ CARTAO PAYTRACK' + ' - ' + df['Data_transacao'].dt.strftime('%d/%m/%y')

# Validacao Crédito

df['Crédito'] = df['VALOR']
 
# Validacao Débito

df['Débito'] = ''

# Validacao TipoContapartida 

df['Tipo de Contrapartida'] = 'Razao'

# Conta Partida

df['Conta Partida'] = '11230000101'

# Validacao Estabelecimento_fiscal_1

df['Dimensao_Estabelecimeto_fiscal_1'] = df['Dimensao_Estabelecimeto_fiscal']

# Validacao Dimensao_produto.1

df['Dimensao_produto_1'] = df['Dimensao_Produto']

# Validacao Dimensao_correspondente.1

df['Dimensao_correspondente.1'] = df['Dimensao_correspondente']

# Validacao Dimensao_ponto

df['Dimensao_1'] = df['Dimensao_ponto']

# Validacao_ponto

df['Ponto'] = '00000003' 

# Validacao_Fatura

df['Fatura'] = 'VC RESQ' + '-' + df['Data_transacao'].dt.strftime('%m/%y') + '-' + df['CENTRO_CUSTO']

# Validacao_ Data_Vencimento 

df['Data_Vencimento'] = df['Data_transacao'] - pd.Timedelta(days=30)

# Validacao_Data_Documento 

df['Data_Documento'] = df['Data_transacao'] - pd.Timedelta(days=30)

# Validacoes simples 

df['Numero_documento'] = ''
df['Grupo de imposto Retido na fonte'] = ''
df['Grupo de imposto retido no item'] = ''
df['Perfil de lançamento'] = 'VERB COML'
df['Codigo Imposto'] = ''
df['Grupo de imposto'] = ''
df['Grupo de imposto do item'] = ''
df['Código de Barras'] = ''

# Conversao data dd/mm/aaaa

df['Data_transacao'] = df['Data_transacao'].dt.strftime('%d/%m/%y')
df['Data_Vencimento'] = df['Data_Vencimento'].dt.strftime('%d/%m/%y')
df['Data_Documento'] = df['Data_Documento'].dt.strftime('%d/%m/%y')

df_colunas_template = df[['Empresa','BRL','Taxa_Cambio','Data_transacao','Tipo_de_Conta',
'Conta','Dimensao_Estabelecimeto_fiscal','Dimensao_Produto','Dimensao_Produto','Dimensao_correspondente',
'Dimensao_ponto','Dimensao_departamento','Descricao','Crédito','Débito','Tipo de Contrapartida','Conta Partida',
'Dimensao_Estabelecimeto_fiscal_1','Dimensao_produto_1','Dimensao_correspondente.1','Dimensao_1','Ponto','Fatura',
'Data_Vencimento','Data_Documento','Numero_documento','Grupo de imposto Retido na fonte','Grupo de imposto retido no item',
'Perfil de lançamento','Codigo Imposto','Grupo de imposto','Grupo de imposto retido no item','Código de Barras']]


import os
import pandas as pd
from datetime import datetime

# Definir o nome do arquivo com data usando hífens para o formato
Nome_arquivo = 'Template_RESQ' + ' - ' + datetime.today().strftime('%d-%m-%y') + '.csv'

# Caminho do arquivo original
caminho = r'C:\Users\lucas\Desktop\Teste_template.dados_template.csv'

# Substituir barras invertidas por barras normais
caminho = caminho.replace('\\', '/')

# Encontrar a posição do ponto ('.') no caminho para separar a extensão
caminho_position = caminho.find('.')

# Extrair o caminho sem a extensão
extract = caminho[:caminho_position]

# Concatenar o caminho do diretório com o nome do arquivo
Caminho_completo = os.path.join(extract, Nome_arquivo)

# Verificar se o diretório existe, caso contrário, criar
diretorio = os.path.dirname(Caminho_completo)
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Supondo que 'df' seja o seu DataFrame
# Exemplo: df = pd.DataFrame(data)

# Salvar o DataFrame no caminho completo
df.to_csv(Caminho_completo, index=True)

print(f"Arquivo salvo em: {Caminho_completo}")

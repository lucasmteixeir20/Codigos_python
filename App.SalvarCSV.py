import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os

# Função para processar os dados
def processar_dados():
    # Dicionário com os dados
    dicionario = {
        'CPF': ['023.875.320-40', '234.768.560-60', '300.800.800-90', '600.900.300-50'],
        'FORNECEDOR': ['000230', '000340', '000900', '048589'],
        'VALOR': ['500', '1000', '600', '500'],
        'CENTRO_CUSTO': ['34050', '1061', '6041', '56040']}

    # Criar DataFrame
    df = pd.DataFrame(dicionario)

    # Processamento do DataFrame
    df['Primeiro_algarismo'] = df['CENTRO_CUSTO'].astype(str).str[0].astype(int)
    df['Quantidade_Caracteres'] = df['CENTRO_CUSTO'].astype(str).str.len()
    df['Empresa'] = np.where((df['CENTRO_CUSTO'].astype(str).str[0].astype(int) >= 3) & 
                             (df['CENTRO_CUSTO'].astype(str).str.len() == 5), 'Promil', 'Soldi')
    df['BRL'] = np.where(df['CENTRO_CUSTO'].str.strip() == '', '', 'BRL')
    df['Taxa_Cambio'] = np.where(df['CENTRO_CUSTO'].str.strip() == '', '', '100')
    df['Data_transacao'] = pd.to_datetime(datetime.today().date())
    df['Tipo_de_Conta'] = np.where(df['CENTRO_CUSTO'].str.strip() == '', '', 'Fornecedor')
    df['Conta'] = np.where(df['CENTRO_CUSTO'].str.strip() == '', '', df['FORNECEDOR'])
    df['Dimensao_Estabelecimeto_fiscal'] = np.where(df['Empresa'] == 'Promil', '000130', '000190')
    df['Descricao'] = 'RESQ CARTAO PAYTRACK' + ' - ' + df['Data_transacao'].dt.strftime('%d/%m/%y')
    df['Crédito'] = df['VALOR']
    df['Débito'] = ''
    df['Tipo de Contrapartida'] = 'Razao'
    df['Conta Partida'] = '11230000101'
    df['Fatura'] = 'VC RESQ' + '-' + df['Data_transacao'].dt.strftime('%m/%y') + '-' + df['CENTRO_CUSTO']
    df['Data_Vencimento'] = df['Data_transacao'] - pd.Timedelta(days=30)
    df['Data_Documento'] = df['Data_transacao'] - pd.Timedelta(days=30)
    df['Numero_documento'] = ''
    df['Grupo de imposto Retido na fonte'] = ''
    df['Perfil de lançamento'] = 'VERB COML'
    df['Codigo Imposto'] = ''
    df['Codigo de Barras'] = ''

    # Adicionando as colunas ausentes com valores vazios
    df['Grupo de imposto retido no item'] = ''
    df['Grupo de imposto'] = ''

    # Criar as colunas que faltam, com valores vazios
    df['Dimensao_Produto'] = ''
    df['Dimensao_correspondente'] = ''
    df['Dimensao_ponto'] = ''
    df['Dimensao_departamento'] = ''
    df['Dimensao_Estabelecimeto_fiscal_1'] = df['Dimensao_Estabelecimeto_fiscal']
    df['Dimensao_produto_1'] = df['Dimensao_Produto']
    df['Dimensao_correspondente.1'] = df['Dimensao_correspondente']
    df['Dimensao_1'] = df['Dimensao_ponto']
    df['Ponto'] = '00000003'

    # Formatando as datas
    df['Data_transacao'] = df['Data_transacao'].dt.strftime('%d/%m/%y')
    df['Data_Vencimento'] = df['Data_Vencimento'].dt.strftime('%d/%m/%y')
    df['Data_Documento'] = df['Data_Documento'].dt.strftime('%d/%m/%y')

    # Selecione as colunas necessárias
    df_colunas_template = df[['Empresa', 'BRL', 'Taxa_Cambio', 'Data_transacao', 'Tipo_de_Conta',
                              'Conta', 'Dimensao_Estabelecimeto_fiscal', 'Dimensao_Produto', 'Dimensao_correspondente', 
                              'Dimensao_ponto', 'Dimensao_departamento', 'Descricao', 'Crédito', 'Débito', 
                              'Tipo de Contrapartida', 'Conta Partida', 'Dimensao_Estabelecimeto_fiscal_1', 
                              'Dimensao_produto_1', 'Dimensao_correspondente.1', 'Dimensao_1', 'Ponto', 'Fatura', 
                              'Data_Vencimento', 'Data_Documento', 'Numero_documento', 'Grupo de imposto Retido na fonte', 
                              'Grupo de imposto retido no item', 'Perfil de lançamento', 'Codigo Imposto', 
                              'Grupo de imposto', 'Codigo de Barras']]

    # Definir o nome do arquivo com data
    Nome_arquivo = 'Template_RESQ' + ' - ' + datetime.today().strftime('%d-%m-%y') + '.csv'
    caminho = 'C:/Users/lucas/Desktop/Teste_template'
    
    # Verificar se o diretório existe, caso contrário, criar
    if not os.path.exists(caminho):
        os.makedirs(caminho)

    Caminho_completo = os.path.join(caminho, Nome_arquivo)
    
    # Salvar arquivo CSV
    df_colunas_template.to_csv(Caminho_completo, index=False)
    return Caminho_completo

# Layout da interface com Streamlit
st.title("Processador de Dados - Template RESQ")
st.write("Clique no botão abaixo para processar os dados e gerar o arquivo CSV.")

# Botão para processar os dados
if st.button('Processar Dados'):
    caminho_arquivo = processar_dados()
    st.success(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
    st.download_button(label="Baixar o arquivo", data=open(caminho_arquivo, 'rb'), file_name=os.path.basename(caminho_arquivo), mime='text/csv')

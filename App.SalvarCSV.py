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
    df['Grupo de imposto retido no item

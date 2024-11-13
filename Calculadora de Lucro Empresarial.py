import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Calculadora de Lucro",
    page_icon="💰",
    layout="wide"
)

# Título principal com estilo
st.markdown("""
    <h1 style='text-align: center; color: #2e7d32;'>
        Calculadora de Lucro Empresarial 💼
    </h1>
""", unsafe_allow_html=True)

# Criando colunas para organizar o layout
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #1976d2;'>Informações de Entrada</h3>
        </div>
    """, unsafe_allow_html=True)
    
    # Campos de entrada
    faturamento = st.number_input(
        "Digite o Faturamento (R$)",
        min_value=0.0,
        format="%.2f",
        help="Digite o valor do faturamento"
    )
    
    custo = st.number_input(
        "Digite o Custo (R$)",
        min_value=0.0,
        format="%.2f",
        help="Digite o valor do custo"
    )

    # Tabela informativa de alíquotas
    st.markdown("""
        <div style='background-color: #e3f2fd; padding: 15px; border-radius: 10px; margin-top: 20px;'>
            <h4 style='color: #1565c0;'>Tabela de Alíquotas</h4>
        </div>
    """, unsafe_allow_html=True)
    
    df_aliquotas = pd.DataFrame({
        'Faixa de Faturamento': [
            'Até R$ 9.999',
            'R$ 10.000 a R$ 19.999',
            'R$ 20.000 a R$ 29.999',
            'A partir de R$ 30.000'
        ],
        'Alíquota': ['5%', '10%', '15%', '18%']
    })
    
    st.table(df_aliquotas)

with col2:
    st.markdown("""
        <div style='background-color: #f0f2f6; padding: 20px; border-radius: 10px;'>
            <h3 style='color: #1976d2;'>Resultado do Cálculo</h3>
        </div>
    """, unsafe_allow_html=True)

    if faturamento > 0:
        # Determinando a alíquota com base no faturamento
        if faturamento <= 9999:
            aliquota = 0.05
            aliquota_texto = "5%"
        elif faturamento <= 19999:
            aliquota = 0.10
            aliquota_texto = "10%"
        elif faturamento <= 29999:
            aliquota = 0.15
            aliquota_texto = "15%"
        else:
            aliquota = 0.18
            aliquota_texto = "18%"

        # Cálculos
        imposto = faturamento * aliquota
        lucro = faturamento - imposto - custo

        # Exibindo resultados em cards
        col2_1, col2_2, col2_3 = st.columns(3)
        
        with col2_1:
            st.metric(
                label="Alíquota Aplicada",
                value=aliquota_texto,
                delta=None
            )
        
        with col2_2:
            st.metric(
                label="Valor do Imposto",
                value=f"R$ {imposto:,.2f}",
                delta=None
            )
        
        with col2_3:
            st.metric(
                label="Lucro Final",
                value=f"R$ {lucro:,.2f}",
                delta=None if lucro >= 0 else "Prejuízo",
                delta_color="normal" if lucro >= 0 else "inverse"
            )

        # Gráfico de composição
        dados_grafico = pd.DataFrame({
            'Componente': ['Impostos', 'Custos', 'Lucro'],
            'Valor': [imposto, custo, lucro]
        })

        fig = px.pie(
            dados_grafico,
            values='Valor',
            names='Componente',
            title='Composição do Faturamento',
            color_discrete_sequence=['#ef5350', '#42a5f5', '#66bb6a']
        )
        st.plotly_chart(fig, use_container_width=True)

# Adicionar informações extras
st.markdown("""
    <div style='background-color: #fff3e0; padding: 15px; border-radius: 10px; margin-top: 20px;'>
        <h4 style='color: #f57c00;'>ℹ️ Informações Importantes</h4>
        <ul>
            <li>Os cálculos são realizados automaticamente com base no faturamento informado</li>
            <li>A alíquota é selecionada automaticamente de acordo com a faixa de faturamento</li>
            <li>O gráfico mostra a distribuição percentual entre impostos, custos e lucro</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

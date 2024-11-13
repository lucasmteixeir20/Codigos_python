import streamlit as st
from datetime import datetime, timedelta

def calcular_boleto(data_fat, prazo, data_pag, valor):
    # Calcula a data de vencimento
    data_vencimento = data_fat + timedelta(days=prazo)
    
    # Calcula a diferença de dias
    diferenca_vencimento = (data_pag - data_vencimento).days
    
    # Inicializa variáveis
    resultado = ""
    valor_final = valor
    status_color = "green"
    
    # Calcula multas e juros
    if diferenca_vencimento < 0:
        resultado = 'Título ainda não venceu'
        status_color = "green"
    elif diferenca_vencimento == 0:
        resultado = 'Título está vencendo hoje'
        status_color = "orange"
    else:
        # Calcula multa
        if diferenca_vencimento <= 10:
            multa = valor * 0.02
        elif diferenca_vencimento <= 30:
            multa = valor * 0.03
        else:
            multa = valor * 0.05
            
        # Calcula juros
        juros = valor * 0.0003 * diferenca_vencimento
        valor_final = valor + multa + juros
        resultado = f'Valor com juros: R$ {valor_final:.2f}'
        status_color = "red"
    
    return resultado, data_vencimento, diferenca_vencimento, status_color, valor_final

def main():
    st.set_page_config(page_title="Calculadora de Boletos Financeiros", layout="centered")
    
    # Título com estilo
    st.title("💰 Calculadora de Boletos Financeiros")
    st.markdown("---")
    
    # Container para inputs
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            data_faturamento = st.date_input(
                "Data do Faturamento",
                min_value=datetime(2000, 1, 1),
                max_value=datetime(2100, 12, 31),
                value=datetime.today()
            )
            
            prazo = st.number_input(
                "Prazo (em dias)",
                min_value=0,
                max_value=365,
                value=30
            )
        
        with col2:
            data_pagamento = st.date_input(
                "Data do Pagamento",
                min_value=datetime(2000, 1, 1),
                max_value=datetime(2100, 12, 31),
                value=datetime.today()
            )
            
            valor_boleto = st.number_input(
                "Valor do Boleto (R$)",
                min_value=0.0,
                max_value=1000000.0,
                value=0.0,
                format="%.2f"
            )
    
    # Botão calcular
    if st.button("Calcular", type="primary", use_container_width=True):
        if valor_boleto > 0:
            resultado, data_venc, dias_atraso, status_color, valor_final = calcular_boleto(
                data_faturamento,
                prazo,
                data_pagamento,
                valor_boleto
            )
            
            # Container para resultados
            st.markdown("---")
            resultados_container = st.container()
            
            with resultados_container:
                # Métricas em cards
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        label="Valor Original",
                        value=f"R$ {valor_boleto:.2f}"
                    )
                
                with col2:
                    st.metric(
                        label="Valor Final",
                        value=f"R$ {valor_final:.2f}",
                        delta=f"R$ {valor_final - valor_boleto:.2f}"
                    )
                
                with col3:
                    st.metric(
                        label="Dias em Atraso",
                        value=max(0, dias_atraso)
                    )
                
                # Status com cor apropriada
                st.markdown(f"""
                    

                        {resultado}
                    

                """, unsafe_allow_html=True)
                
                # Informações adicionais
                st.info(f"Data de Vencimento: {data_venc.strftime('%d/%m/%Y')}")
        else:
            st.error("Por favor, insira um valor válido para o boleto.")

    # Informações sobre multas e juros
    with st.expander("ℹ️ Informações sobre Multas e Juros"):
        st.markdown("""
        **Regras de cálculo:**
        
        **Multas:**
        - Até 10 dias de atraso: 2%
        - De 11 a 30 dias de atraso: 3%
        - Acima de 30 dias de atraso: 5%
        
        **Juros:**
        - 0,03% ao dia sobre o valor do boleto
        """)

if __name__ == "__main__":
    main()

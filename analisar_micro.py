# BIBLIOTECAS IMPORTADAS:
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import datetime
from datetime import timedelta
import streamlit as st
import time


# SIGLA E NOME DO ATIVO ANALISADO:
sigla_ativo = "MNQ=F"
nome_ativo = "NASDAQ 100 FUTUROS"

# LISTA PERÍODO GRÁFICO:
periodo = ['5m', '15m', '30m', '60m', '1d', '1wk']

# DADOS HISTÓRICOS PERÍODO DE VENCIMENTO:
data_inicial_vencimento = '2022-12-16'
data_final_vencimento = '2024-03-15'  
    
with st.sidebar:
    st.image('baixados2.JPG')
    st.divider()
    
    selecao_periodo = st.selectbox('Selecione o Período Gráfico a Pesquisar:', periodo)
    
    
    
    st.divider()
    
    input_periodo_inicial = st.date_input('Selecione o período Inicial de Pesquisa: ', format='DD/MM/YYYY')
    input_periodo_final = st.date_input('Selecione o período Final de Pesquisa: ', format='DD/MM/YYYY')
    st.divider()
    

dados_historico_vencimento = yf.download(sigla_ativo, input_periodo_inicial, input_periodo_final, interval='1d')
dados_historico_intraday = yf.download(sigla_ativo, input_periodo_inicial, input_periodo_final, interval=selecao_periodo)



# Gráfico interativo do Nasdaq com Plotly:
fig = go.Figure(data=[go.Candlestick(x=dados_historico_intraday.index, 
                open=dados_historico_intraday['Open'],
                high=dados_historico_intraday['High'],
                low=dados_historico_intraday['Low'],
                close=dados_historico_intraday['Close'])])



fig.update_layout(title=f"GRÁFICO ANÁLISE MICRO DO {nome_ativo} ({sigla_ativo})", xaxis_title='Data Histórico', yaxis_title='Preço Ativo', template = 'plotly_dark', title_x=0.25, title_font_color="#00FFFF", title_font_family="Times New Roman")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_layout(height=720, width=1080)
fig.update_xaxes(title_font_family="Times New Roman", title_font_color="#00FF00")
fig.update_yaxes(title_font_family="Times New Roman", title_font_color="#00FF00")




# Adicionando Container do Gráfico Interativo:
with st.container():
    st.title('Análise de Dados Micros')
    
    with st.spinner('Aguarde por favor...'):
        time.sleep(5)
    
    st.success('Carregamento concluído com sucesso!')

    st.header('Gráfico Interativo:', divider='rainbow')
    st.plotly_chart(fig)
    
    st.dataframe(dados_historico_intraday)

st.divider()

     
fig.update_layout()



    
    

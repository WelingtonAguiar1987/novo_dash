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


with st.sidebar:
    st.image('images.JPG')
    st.divider()
    
    input_data_inicial = st.date_input('Selecione a Data Inicial de Pesquisa: ', format='DD/MM/YYYY')
    input_data_final = st.date_input('Selecione a Data Final de Pesquisa: ', format='DD/MM/YYYY')

       
    # DADOS HISTÓRICOS PERÍODO DE VENCIMENTO:
    data_inicial_vencimento = '2022-12-16'
    data_final_vencimento = '2024-03-15'

    dados_historico_vencimento = yf.download(sigla_ativo, input_data_inicial, input_data_final, interval='1d')
    dados_historico_vencimento['Volatilidade'] = dados_historico_vencimento['High'] - dados_historico_vencimento['Low']
    dados_historico_vencimento['Retornos'] = dados_historico_vencimento['Adj Close'].pct_change() * 100
    media_retornos = dados_historico_vencimento['Retornos'].sum()
    
    pontos_volatilidade = (dados_historico_vencimento['High'].max() - dados_historico_vencimento['Low'].min())
    
    
    
    if media_retornos >= 0.01:
        st.metric(label="Retorno Acumulado no período:", value=f'{pontos_volatilidade} Pontos.', delta=f'{media_retornos:.2f}%', delta_color='normal')
    elif media_retornos <= -0.01:
        st.metric(label='Retorno Acumulado no período:', value=f'{pontos_volatilidade} Pontos.', delta=f'{media_retornos:.2f}%', delta_color='off')
    else:
        st.subheader('Selecione as datas com atenção...')
    
        
    st.divider()
    
    preco_ultimo_fechamento = dados_historico_vencimento['Close'][-1]
    ultima_abertura = dados_historico_vencimento['Open'][-1]
    

# Gráfico interativo do Nasdaq com Plotly:
fig = go.Figure(data=[go.Candlestick(x=dados_historico_vencimento.index,
                open=dados_historico_vencimento['Open'],
                high=dados_historico_vencimento['High'],
                low=dados_historico_vencimento['Low'],
                close=dados_historico_vencimento['Close'])])



fig.add_hline(preco_ultimo_fechamento, line=dict(color='blue', width=2, dash='dash'), name=f'Último Fechamento: {preco_ultimo_fechamento:.2f}')
fig.add_hline(ultima_abertura, line=dict(color='white', width=2, dash='dash'), name=f'Última Abertura: {ultima_abertura:.2f}')
fig.update_layout(title=f"GRÁFICO DE TODO O PERÍODO DE VENCIMENTO DO {nome_ativo} ({sigla_ativo})", xaxis_title='Data Histórico', yaxis_title='Preço Ativo', template = 'plotly_dark', title_x=0.25, title_font_color="#00FFFF", title_font_family="Times New Roman")
fig.update_layout(xaxis_rangeslider_visible=False)
fig.update_layout(height=720, width=1080)
fig.update_xaxes(title_font_family="Times New Roman", title_font_color="#00FF00")
fig.update_yaxes(title_font_family="Times New Roman", title_font_color="#00FF00")


# Adicionando Container do Gráfico Interativo:

with st.container():
    st.title('Análise de Dados de Todo o Período de Vencimento')
    
    with st.spinner('Aguarde por favor...'):
        time.sleep(10)
    
    st.success('Carregamento concluído com sucesso!')


    st.header('Gráfico Interativo:', divider='rainbow')
    st.plotly_chart(fig)

st.divider()


# Adicionando Container do Gráfico Estático:
with st.container():
    st.subheader('Tabela de Dados Históricos deste Vencimento:', divider='rainbow')
    st.dataframe(dados_historico_vencimento)
    
    
st.divider() 


fig.update_layout()



    
    

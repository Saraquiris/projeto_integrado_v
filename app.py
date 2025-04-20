import qualRpy.qualR as qr
import pandas as pd


def extrair_parametro(param_code, parametro_nome, user_name, my_password, start_date, end_date, pin_code):
    dados = qr.cetesb_retrieve(user_name, my_password, start_date, end_date, param_code, pin_code)
    if dados is not None and not dados.empty:
        dados['parametro'] = parametro_nome
    else:
        print(f"Não foram encontrados dados para o parâmetro {parametro_nome}.")
    return dados


user_name = "brunoavast2000@hotmail.com"
my_password = "Qualar5873@"
start_date = "01/01/2024"
end_date = "17/04/2024"
pin_code = 269  # Código da estação

# Códigos dos medidores
codigo_pm25 = 57   
codigo_pm10 = 12   
codigo_no2  = 15


df_pm25 = extrair_parametro(codigo_pm25, "PM2.5", user_name, my_password, start_date, end_date, pin_code)
df_pm10 = extrair_parametro(codigo_pm10, "PM10", user_name, my_password, start_date, end_date, pin_code)
df_no2  = extrair_parametro(codigo_no2,  "NO2",  user_name, my_password, start_date, end_date, pin_code)


df_aqi = qr.cetesb_retrieve(user_name, my_password, start_date, end_date, 63, pin_code)
if df_aqi is not None and not df_aqi.empty:
    df_aqi['parametro'] = "AQI"

# Unir os dataframes
dataframes = [df for df in [df_pm25, df_pm10, df_no2, df_aqi] if (df is not None and not df.empty)]
if dataframes:
    df_final = pd.concat(dataframes, ignore_index=True)
    
    df_final.to_csv("dados_parametros.csv", index=False)
    print("Dados extraídos e salvos com sucesso no arquivo 'dados_parametros.csv'.")
else:
    print("Nenhum dado foi extraído para os parâmetros especificados.")
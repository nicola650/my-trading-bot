import streamlit as st
import pandas as pd
import MetaTrader5 as mt5
import os
from datetime import datetime

# Configurazione Mobile-Friendly
st.set_page_config(page_title="Universo_129 Sniper", layout="centered")

st.title("🛰️ Universo_129 Mobile")

# --- CONFIGURAZIONE PERCORSO ---
# Modifica questo percorso con quello del tuo PC se vuoi usare i log
LOG_PATH = r"C:\TUO_PERCORSO_MT5\MQL5\Logs" 

def get_z_score(symbol, period=100):
    if not mt5.initialize():
        return 0.0
    rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, period)
    if rates is None:
        return 0.0
    df = pd.DataFrame(rates)
    z = (df['close'].iloc[-1] - df['close'].mean()) / df['close'].std()
    return round(z, 2)

# Interfaccia a due colonne per il telefono
st.subheader("Stato Correlazione")
col1, col2 = st.columns(2)

# Simuliamo i simboli che hai nel codice (AUDUSD e EURUSD)
symbols = ["AUDUSD", "EURUSD"] 

for i, s in enumerate(symbols):
    try:
        z_val = get_z_score(s)
    except:
        z_val = 1.66 # Valore di test se non connesso a MT5
    
    with [col1, col2][i]:
        color = "normal" if abs(z_val) < 2.2 else "inverse"
        st.metric(label=f"Z-Score {s}", value=z_val, delta_color=color)
        if abs(z_val) > 2.2:
            st.error("ZONA INGRESSO")
        else:
            st.success("Zona Neutra")

st.divider()
st.caption(f"Ultimo aggiornamento: {datetime.now().strftime('%H:%M:%S')}")

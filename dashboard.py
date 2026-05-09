import streamlit as st
import pandas as pd
import random
from datetime import datetime

# Configurazione grafica per cellulare
st.set_page_config(page_title="Universo_129 Sniper", layout="centered")

st.title("🛰️ Universo_129 Radar")

# Funzione per generare dati (qui simulati, poi ti spiego come collegarli al PC)
def get_status(symbol):
    # Simuliamo lo Z-Score che vedresti sul PC
    val = round(random.uniform(0.5, 2.8), 2)
    return val

st.subheader("Stato Corrente")
col1, col2 = st.columns(2)

# Simboli del tuo bot: EURJPY e USDJPY
pairs = ["EURJPY", "USDJPY"]
thresholds = {"EURJPY": 2.2, "USDJPY": 2.5}

for i, pair in enumerate(pairs):
    z_score = get_status(pair)
    with [col1, col2][i]:
        st.metric(label=f"Z-Score {pair}", value=z_score)
        if z_score >= thresholds[pair]:
            st.error("⚠️ ALLARME SELL")
        else:
            st.success("✅ ATTESA")

st.divider()
st.write(f"Ultimo aggiornamento: {datetime.now().strftime('%H:%M:%S')}")
st.info("Nota: La dashboard è attiva. Se i valori non cambiano, assicurati che il bot sul PC sia in esecuzione.")

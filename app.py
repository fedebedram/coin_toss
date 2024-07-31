import pandas as pd
import scipy.stats as ss
import time
import streamlit as st

# estas son variables de estado que se conservan cuando Streamlin vuelve a ejecutar este script
if "experiment_no" not in st.session_state:
    st.session_state["experiment_no"] = 0

if "df_exp_res" not in st.session_state:
    st.session_state["df_exp_res"] = pd.DataFrame(columns = ["no","iteraciones","media"])


    



st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

def toss_coin(n):
    trial_outcome = ss.bernoulli.rvs(p=.5, size=n)

    mean = None
    outcome_no = 0
    outcome_c1 = 0

    for r in trial_outcome:
        outcome_no += 1
        if r == 1:
            outcome_c1 += 1
            
        mean = outcome_c1/outcome_no
        chart.add_rows([mean])
        time.sleep(.05)

    return mean




number_of_trials = st.slider("¿Número de intentos?",1,1000,10)
start_button = st.button("Ejecutar")

if start_button:
    st.write(f"Experimento con {number_of_trials} intentos en curso.")
    st.session_state["experiment_no"] += 1
    mean = toss_coin(number_of_trials)
    st.session_state["df_exp_res"] = pd.concat([
        st.session_state["df_exp_res"],
        pd.DataFrame(data = [[st.session_state["experiment_no"],
                              number_of_trials,
                              mean
                              ]],
                     columns = ["no","iteraciones","media"]),
        ],
        axis = 0)
    st.session_state["df_exp_res"] = st.session_state["df_exp_res"].reset_index(drop = True)
                     
st.write(st.session_state["df_exp_res"])



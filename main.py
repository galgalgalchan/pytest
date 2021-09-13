import streamlit as st
import numpy as np
import pandas as pd


st.title("St　reamlit 入門　てすと")

st.write('DATAFRAME')

df = pd.DataFrame(

    np.random.rand(120, 2)/[50, 50]+[35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)

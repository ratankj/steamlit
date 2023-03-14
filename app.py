import streamlit as st
import pandas as pd
import streamlit as st
import pandas as pd
import time



#    UPLOADING A FILE

file=st.file_uploader('upload a file')

if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.head())
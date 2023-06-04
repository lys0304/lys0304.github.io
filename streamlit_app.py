import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

st.header('st.write')

st.write('Hello *world* :sunglasses:')


st.write(1234)

df = pd.read_csv('data.txt',sep='\t',)
df.head()
# st.write(df)


st.write('Below is a DataFrame', df, 'above is ...')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
st.write(df2)
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='b', color='c', tooltip=['a', 'c', 'b'])
st.write(c)
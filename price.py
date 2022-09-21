import streamlit as st
import pickel
pickel_in=open('diamond.pkl','rb')
mond=pickel.load(pickel_in)
a=st.number_input('carat')
b=st.number_input('cut')
c=st.number_input('color')
d=st.number_input('depth')
e=st.number_input('table')
if st.button('PREDICT'):
  st.success(f'DIAMOND PRICE IS {PRICE})

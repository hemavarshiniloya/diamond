import streamlit as st
import pickel
pickel_in=open('diamond.pkl','rb')
mond=pickel.load(pickel_in)
a=st.number_input('enter carat')
b=st.number_input('enter cut')
c=st.number_input('enter color')
d=st.number_input('enter depth')
result=0
if st.button('PREDICT'):
  result=clf.predict([[a,b,c,d]]).squeeze()
  st.success(f'DIAMOND PRICE IS {PRICE})

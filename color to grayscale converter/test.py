import streamlit as st 

user_choice=st.radio("Amount",options=[10,30,20])
if user_choice==30:
    st.info("You made right choice")
    
else:
    st.info("wrong choice!")    
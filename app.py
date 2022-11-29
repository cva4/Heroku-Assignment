import streamlit as st

st.write("""
# Division of two Numbers
""")

#Get Input
st.header('User Input Parameters')

def user_input_features():
    try:
        
        num1 = st.number_input("Numerator",step=1)
        num2 = st.number_input("Denominator",step=1)

        return f'Division of {num1} and {num2} is {num1/num2}'
    except ZeroDivisionError:
        return 'Denominator cannot be Zero'

result = user_input_features()

st.subheader('Result')
st.write(result)

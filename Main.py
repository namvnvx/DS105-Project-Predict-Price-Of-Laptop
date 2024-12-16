from Source import FrontEnd
from Source import BackEnd
import streamlit as st

def Main():
    Input = FrontEnd.Main()
    print('Input', Input)
    result = BackEnd.Main(Input)
    st.header('result : ', result)
    return 0

if __name__ == "__main__":
    Main()
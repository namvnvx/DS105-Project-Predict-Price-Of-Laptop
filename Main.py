from Source import FrontEnd
from Source import BackEnd
import streamlit as st

def Main():
    Input = FrontEnd.Main()

    result = BackEnd.Main(Input)
    st.header('result : ' + str(result))
    return 0

if __name__ == "__main__":
    Main()
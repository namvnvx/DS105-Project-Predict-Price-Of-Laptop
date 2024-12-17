from Source import FrontEnd
from Source import BackEnd

import streamlit as st

def Main():

    #============= Xử lý nhập liệu =============#
    Input = FrontEnd.Input()

    #============= Dự đoán =============#
    result = BackEnd.Main(Input)


    #============= Xử lý hiển thị =============#
    FrontEnd.Output(result)

    return 0

#================ Main ================#

if __name__ == "__main__":
    Main()
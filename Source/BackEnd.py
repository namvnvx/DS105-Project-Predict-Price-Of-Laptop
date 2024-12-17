import joblib
import numpy as np
import pandas as pd

def Encoder(data, col = "Chưa Nhập"):
    # Chuyển đổi cột feature

    if col != "Chưa Nhập":
        link = ".\\Source\\Model_Encoder\\" + col + '.joblib'
        encoder = joblib.load(link)

        try:
            return encoder.transform([data])[0]
        except:
            return 0
    
def ProcessInput(data):
    # Chỉnh sửa đầu vào để đem đi predict

    columns = ['Brand', 'Type', 'Brand_CPU', 'Type_CPU', 'Hard_Drive', 'Length',
                'Width', 'Thick', 'Key_light', 'Cores_CPU', 'Threads_CPU', 'Speed_CPU',
                'MaxSpeed_CPU', 'Cache', 'RAM', 'BusSpeed_RAM', 'MaxSup_Ram',
                'Screen_Size', 'Refresh_Rate', 'Weight', 'Charging_Power', 'Release']

    cate_list = ['Brand', 'Brand_CPU', 'Hard_Drive', 'Key_light', 'MaxSup_Ram',
                 'Screen_Size', 'Type_CPU', 'Type']
    for col in cate_list:
        data[col] = Encoder(data[col], col)

    result = []
    for col in columns:
        result.append(data[col])
    result = np.array(result).astype('float64').reshape(1, 22)

    return result

def ProcessResult(data):
    # Trả về giá trị được làm đẹp

    temp = data[0] / 1000000.

    return temp

def Predict(data):
    # Dự đoán 

    link = ".\\Source\\Model.joblib"
    model = joblib.load(link)
    result = model.predict(data)

    return ProcessResult(result)


#================ Main ================#

def Main(data):
    data = ProcessInput(data)

    return Predict(data)
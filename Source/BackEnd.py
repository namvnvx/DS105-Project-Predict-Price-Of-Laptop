import joblib
import numpy as np

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

    cate_list = ['Brand', 'Brand_CPU', 'Hard_Drive', 'Key_light', 'MaxSup_Ram',
                 'Screen_Size', 'Type_CPU', 'Type']
    for col in cate_list:
        data[col] = Encoder(data[col], col)

    data = np.array(data.values).astype('float64').reshape(1, 22)

    return data

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
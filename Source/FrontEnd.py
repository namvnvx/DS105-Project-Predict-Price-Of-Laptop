import streamlit as st
import pandas as pd
import numpy as np


def Run():
#========================================= Hàm & Truy vấn ==================================================#

    df = pd.read_csv('Source/Df_SuperUltra_Provjp.csv')

    resulf = {}

    def select_items(feature_name):
        # lấy giá trị unique thông thường
        return df[feature_name].unique().tolist()

    def select_items_capitalized(feature_name):
        # lấy giá trị unique kèm theo Upper chữ đầu tiên
        unique_items = df[feature_name].unique().tolist()
        capitalized_items = [item.capitalize() for item in unique_items]
        return capitalized_items

    def select_type(feature_name, feature_value, items_name):
        # lấy item theo value của feature
        return df.loc[df[feature_name] == feature_value][items_name].unique().tolist()

    def select_int_value(list_1):
        # lấy giá trị sô nguyên
        return [int(item) for item in list_1]
        
#========================================= Danh sách lựa chọn ==================================================#

    # 1 - 2: Brand & Type
    opt1 = np.sort(select_items_capitalized('Brand'))
    select1 = st.sidebar.selectbox("Lựa chọn hãng máy", options=opt1, )
    resulf['Brand'] = select1.lower()

    with st.sidebar:
        if select1:
            opt2 = np.sort(select_type('Brand', select1.lower(), 'Type'))
            select2 = st.selectbox("Lựa chọn loại máy theo hãng", options=opt2)
            resulf['Type'] = select2

    # 3: RAM
    opt3 = np.sort(select_int_value(select_items('RAM')))
    select3 = st.sidebar.selectbox("Lựa chọn RAM (**GB**)", options=opt3, index=1)
    resulf['RAM'] = select3

    # 4 - 5: Brand_CPU & Type_CPU
    opt4 = np.sort(select_items_capitalized('Brand_CPU'))
    select4 = st.sidebar.selectbox("Lựa chọn hãng CPU", options=opt4)
    resulf['Brand_CPU'] = select4

    with st.sidebar:
        if select4:
            opt5 = np.sort(select_type('Brand_CPU', select4.lower(), 'Type_CPU'))
            select5 = st.selectbox("Lựa chọn loại CPU", options=opt5)
            resulf['Type_CPU'] = select5

    # 6: Hard_Drive
    opt6 = np.sort(select_int_value(select_items('Hard_Drive')))
    select6 = st.sidebar.selectbox("lựa chọn dung lượng ổ cứng (**GB**)", options=opt6)
    resulf['Hard_Drive'] = select6

    # 7 - 8 - 9: Length, Width & Thick
    opt7 = np.sort(select_items('Length'))
    select7 = st.sidebar.selectbox("Độ dài (**mm**)", options=opt7)
    resulf['Length'] = select7

    opt8 = np.sort(select_items('Width'))
    select8 = st.sidebar.selectbox("Độ rộng (**mm**)", options=opt8)
    resulf['Width'] = select8

    opt9 = np.sort(select_items('Thick'))
    select9 = st.sidebar.selectbox("Độ dày (**mm**)", options=opt9)
    resulf['Thick'] = select9

    # 10: Cores_CPU
    opt10 = np.sort(select_int_value(select_items('Cores_CPU')))
    select10 = st.sidebar.selectbox("Số lượng nhân (lõi) CPU", options=opt10)
    resulf['Cores_CPU'] = select10

    # 11: Threads_CPU
    opt11 = np.sort(select_int_value(select_items('Threads_CPU')))
    select11 = st.sidebar.selectbox("Số lượng luồng xử lý của CPU", options=opt11)
    resulf['Threads_CPU'] = select11

    # 12: Speed_CPU
    opt12 = np.sort(select_items('Speed_CPU'))
    select12 = st.sidebar.selectbox("Tốc độ xử lý của CPU", options=opt12)
    resulf['Speed_CPU'] = select12

    # 13: MaxSpeed_CPU
    opt13 = np.sort(select_items('MaxSpeed_CPU'))
    select13 = st.sidebar.selectbox("Tốc độ xử lý TỐI ĐA của CPU (**GHz**)", options=opt13)
    resulf['MaxSpeed_CPU'] = select13

    # 14: Key_Light
    opt14 = np.sort(select_items('Key_Light'))
    select14 = st.sidebar.selectbox("Đèn bàn phím", options=opt14)
    resulf['Key_light'] = select14

    # 15: Cache
    opt15 = np.sort(select_int_value(select_items('Cache')))
    select15 = st.sidebar.selectbox("Dung lượng bộ nhớ đệm (**Byte**)", options=opt15)
    resulf['Cache'] = select15

    # 16: BusSpeed_RAM
    opt16 = np.sort(select_int_value(select_items('BusSpeed_RAM')))
    select16 = st.sidebar.selectbox("Tốc độ (tần số hoạt động) của RAM (**MHz**)", options=opt16)
    resulf['BusSpeed_RAM'] = select16

    # 17: MaxSup_RAM
    #opt17 = np.sort(select_int_value(select_items('MaxSup_RAM')))
    #select17 = st.sidebar.selectbox("Hỗ trợ RAM tối đa (**GB**)", options=opt17)
    #resulf['MaxSup_Ram'] = select17
    opt17 = np.sort(select_int_value(select_items('MaxSup_RAM')))

    opt17_1 = [str(item) for item in opt17]
    opt17_1[0] = "Không hỗ trợ"

    select17 = st.sidebar.selectbox("Hỗ trợ RAM tối đa (**GB**)", options=opt17_1)

    if select17 == 'Không hỗ trợ':
        resulf['MaxSup_RAM'] = 0
    else:
        resulf['MaxSup_RAM'] = int(select17)
    

    # 18: Screen_Size
    opt18 = np.sort((select_items('Screen_Size')))
    select18 = st.sidebar.selectbox("Kích cỡ màn hình (**Inch**)", options=opt18)
    resulf['Screen_Size'] = select18

    # 19: Refresh_Rate
    opt19 = np.sort(select_int_value(select_items('Refresh_Rate')))
    select19 = st.sidebar.selectbox("Tần số quét - tốc độ làm mới màn hình (**Hz**)", options=opt19)
    resulf['Refresh_Rate'] = select19

    # 20: Weight
    opt20 = np.sort((select_items('Weight')))
    select20 = st.sidebar.selectbox("Khối lượng của máy (**Kg**)", options=opt20)
    resulf['Weight'] = select20

    # 21: Charging_Power
    opt21 = np.sort(select_int_value(select_items('Charging_Power')))
    select21 = st.sidebar.selectbox("Công suất bộ sạc (**W**)", options=opt21)
    resulf['Charging_Power'] = select21

    # 22: Release
    opt22 = np.sort(select_int_value(select_items('Release')))
    select22 = st.sidebar.selectbox("Thời điểm ra mắt sản phẩm (**Năm 20__**)", options=opt22)
    resulf['Release'] = select22

#========================================== Phần web chính ====================================================#

    # title và header
    st.title('Dự đoán giá Laptop',)
    st.header('_'*39)
    st.subheader("FROM: Tổ đội phép thuật UIT")

    # body
    st.write("Nhằm đưa đến cho **Người tiêu dùng phổ thông** khả năng nhận biết tầm giá của 1 chiếc **Laptop** trên thị trường chung hiện nay.")
    st.write("*Sản phẩm chỉ mang tính chất tham khảo, không tránh khỏi sai sót.*")
    
    st.subheader("Kết quả lựa chọn")
    
    data = pd.Series(resulf)
    p1 = data[:8].to_frame().rename(columns={0: "Giá trị đã chọn"}) 
    p2 = data[8:15].to_frame().rename(columns={0: "Giá trị đã chọn"})
    p3 = data[15:].to_frame().rename(columns={0: "Giá trị đã chọn"})

    # Tạo 3 cột trong Streamlit
    col1, col2, col3 = st.columns(3)

    # Hiển thị từng phần trong mỗi cột
    with col1:
        st.dataframe(p1, width=220)
    with col2:
        st.dataframe(p2, width=220)
    with col3:
        st.dataframe(p3, width=220)

    return data

#================ Input ================#
def Input():
    # Hàm lấy dữ liệu

    return Run()



#================ Output ================#
def Output(result):
    # Hàm xuất kết quả
    print(result)
    st.header('Kết quả dự đoán : ' + str(result))

    return
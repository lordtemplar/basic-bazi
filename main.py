import streamlit as st
import pandas as pd
from datetime import datetime

def calculate_heavenly_stem_and_earthly_branch(year, month, day, hour):
    """
    ฟังก์ชันคำนวณธาตุฟ้าและธาตุดินจากข้อมูลวันเดือนปีและเวลาเกิด
    
    Parameters:
    - year: ปี ค.ศ.
    - month: เดือน
    - day: วัน
    - hour: ชั่วโมงเกิด (0-23)
    
    Returns:
    - DataFrame ที่มีตารางแสดงผล 4 เสาฟ้าดิน
    """
    # รายการ Heavenly Stems (ธาตุฟ้า) และ Earthly Branches (ธาตุดิน)
    heavenly_stems = ['Jia', 'Yi', 'Bing', 'Ding', 'Wu', 'Ji', 'Geng', 'Xin', 'Ren', 'Gui']
    earthly_branches = ['Zi (Rat)', 'Chou (Ox)', 'Yin (Tiger)', 'Mao (Rabbit)', 'Chen (Dragon)',
                        'Si (Snake)', 'Wu (Horse)', 'Wei (Goat)', 'Shen (Monkey)', 'You (Rooster)',
                        'Xu (Dog)', 'Hai (Pig)']
    
    # คำนวณเสาปี
    stem_year = heavenly_stems[(year - 3) % 10]
    branch_year = earthly_branches[(year - 3) % 12]
    
    # คำนวณเสาเดือน (ใช้ตารางเดือนสัมพันธ์กับปี)
    month_base = [2, 4, 6, 8, 0, 2, 4, 6, 8, 0]  # ฐาน Stem ของเดือนสำหรับแต่ละปีฟ้า
    stem_month_index = (month_base[(year % 10) % 5] + month - 1) % 10
    stem_month = heavenly_stems[stem_month_index]
    branch_month = earthly_branches[(month + 1) % 12]  # เดือนเริ่มที่ 2
    
    # คำนวณเสาวัน (ใช้ตาราง 60 วัน)
    day_of_year = (datetime(year, month, day) - datetime(year, 1, 1)).days + 1
    stem_day = heavenly_stems[(day_of_year % 10) % 10]
    branch_day = earthly_branches[(day_of_year % 12) % 12]
    
    # คำนวณเสาชั่วโมง (ชั่วยาม)
    hour_branch_index = hour // 2 % 12  # ชั่วโมงหาร 2 แล้วหาดัชนี
    branch_hour = earthly_branches[hour_branch_index]
    stem_hour = heavenly_stems[(day_of_year % 10 * 2 + hour // 2) % 10]  # Stem ตามชั่วยาม
    
    # สร้าง DataFrame สำหรับแสดงตาราง 4 เสา
    data = {
        'Pillar': ['Year', 'Month', 'Day', 'Hour'],
        'Heavenly Stem': [stem_year, stem_month, stem_day, stem_hour],
        'Earthly Branch': [branch_year, branch_month, branch_day, branch_hour]
    }
    df = pd.DataFrame(data)
    return df

# Streamlit UI
st.title("โปรแกรมคำนวณ 4 เสาฟ้าดิน (Bazi)")

# Input widgets
with st.form("bazi_form"):
    year = st.number_input("กรุณาใส่ปีเกิด (ค.ศ.):", min_value=1900, max_value=2100, value=2000)
    month = st.number_input("กรุณาใส่เดือนเกิด (1-12):", min_value=1, max_value=12, value=1)
    day = st.number_input("กรุณาใส่วันเกิด (1-31):", min_value=1, max_value=31, value=1)
    hour = st.number_input("กรุณาใส่เวลาเกิด (0-23 น.):", min_value=0, max_value=23, value=0)
    submitted = st.form_submit_button("คำนวณ")

# Process and display result
if submitted:
    bazi_table = calculate_heavenly_stem_and_earthly_branch(year, month, day, hour)
    st.write("### ผลลัพธ์ 4 เสาฟ้าดิน:")
    st.dataframe(bazi_table)

import streamlit as st
import pandas as pd
import numpy as np

#제목
st.title('Uber pickups in NYC')

#데이터 가져오기
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

#압축된 파일 가져오기
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows) #행 줄 수만큼 읽어오겠다~
    lowercase = lambda x: str(x).lower()  #람다식(대문자를 모두 소문자로~)
    data.rename(lowercase, axis='columns', inplace=True) #람다식 이용해서 대문자를 소문자로 바꾸고 다시 이름을 짓겠다..
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #날짜로 인식할 수 있음(to_datetime)
    return data

#준비중 화면
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

#원래 자료를 보여달라 클릭하면 원자료를 보여줄 수 있게끔...
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#히스토그램 나오고, 시간별로 데이터가 몇개인지 보여줌
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

#슬라이더 만들기(시간조정)
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

#맵에 띄워줄거다...!
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

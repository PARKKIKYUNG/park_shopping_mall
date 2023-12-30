import streamlit as st
import pandas as pd
import os




st.title("준형이의 쇼핑몰")

image_path = "QA.jpg"  # Replace with the actual path to your photo
st.image(image_path, use_column_width=True, width=200)



df = pd.read_csv("통합1차.csv")
print(df)
# Display the entire data table
st.subheader("전체 데이터")
st.dataframe(df)



# Section 3-3: Column selection for filtering
st.subheader("검색")
selected_qa_keyword=''
selected_value = ''

selected_qa = st.selectbox("질문기준 or 답변기준:", ['필터로만검색','질의 내용','답변'])
if selected_qa != '필터로만검색':
    selected_qa_keyword = st.text_input(f"{selected_qa}에서 검색할 키워드(쉼표로 구분): ")

selected_column = st.selectbox("필터링 할 열:", ['전체', '상호','제품군','대분류','답변퀄리티'])
if selected_column != '전체':
    selected_value = st.selectbox("선택 열 값:", df[selected_column].unique())

if selected_qa_keyword != '' and selected_column=='전체':
    keywords = [keyword.strip() for keyword in selected_qa_keyword.split(',')]
    filtered_df = df[df[selected_qa].apply(lambda x: all(keyword in x for keyword in keywords))]
    st.dataframe(filtered_df)

if selected_value !='' and selected_qa=='필터로만검색':
    keywords = [keyword.strip() for keyword in selected_value.split(',')]
    filtered_df = df[df[selected_column].apply(lambda x: all(keyword in x for keyword in keywords))]
    st.dataframe(filtered_df)

if selected_value != '' and selected_qa_keyword !='':
    filtered_df = df[df[selected_column]==selected_value]
    keywords = [keyword.strip() for keyword in selected_qa_keyword.split(',')]
    filtered_df = filtered_df[filtered_df[selected_qa].apply(lambda x: all(keyword in x for keyword in keywords))]
    st.dataframe(filtered_df)










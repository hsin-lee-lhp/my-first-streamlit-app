
import streamlit as st


st.header('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
numbera= st.number_input('Tham số a')
numberb= st.number_input('Tham số b')


if st.button('Giải'):
    if numbera==0 and numberb==0:
        st.success("PT có vô số nghiệm")
    elif numbera==0 and numberb!=0:
        st.success("PT vô nghiệm")
    else:
        n1='%.1f'%(-numberb/numbera)
        st.success(f'PT có 1 nghiệm là {n1}')




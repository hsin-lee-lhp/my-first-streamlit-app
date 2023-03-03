
import streamlit as st


st.header('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
numbera= st.number_input('Tham số a')
numberb= st.number_input('Tham số b')


if st.button('Giải'):
    if numbera==0 and numberb==0:
        n='PT vô số nghiệm'
    elif numbera==0 and numberb!=0:
        n='PT vô nghiệm'
    else:
        n1='%.1f'%(-numberb/numbera)
    n="Phương trình có 1 nghiệm" + " " + str(n1)
    st.write(n)
import streamlit as st

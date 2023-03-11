
import streamlit as st


st.header('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
numbera= st.number_input('Tham số a')
numberb= st.number_input('Tham số b')


if st.button('Giải'):
    if numbera==0 and numberb==0:
        n1=' có vô số nghiệm'
    elif numbera==0 and numberb!=0:
        n1='vô nghiệm'
    else:
        n1='%.1f'%(-numberb/numbera)
        n1= "có một nghiệm là " + " " + str(n1)
n="Phương trình " + " " + str(n1)
st.write(n)
import streamlit as st

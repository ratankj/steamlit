import streamlit as st
import pandas as pd
import time

## TEXT BASED UTILITY

#title

st.title('Startup Dashboard')

#header

st.header('i m working on streamlit')

#subheader

st.subheader('this is really great')

#write
st.write('this is a normal text')


#markdown
st.markdown("""
### my favorite movies

- race3
- housefull
- golmall

""")


#code

st.code("""
def foo(input):
    return foo**2

x=foo(2)

""")


# latex

st.latex('x^2 + y^2 +2 = 0')


### DISPLAY ELEMENT


#dataframe
df=pd.DataFrame({
    'name':['Nitish','ratan','raman'],
    'marks':[50,60,70],
    'package':[10,12,14]
})

st.dataframe(df)

#metrix

st.metric('Revenue','Rs 3L','3%')

st.metric('Revenue','Rs 3L','-3%')


# json

st.json({
    'name':['Nitish','ratan','raman'],
    'marks':[50,60,70],
    'package':[10,12,14]
})



# work with image

st.image('ratan.jpg')


# work with video

st.video('20230314191753.mp4')

# work with audio

#st.audio('filename')



##   CREATING LAYOUT

# sidebar

st.sidebar.title('sidebar ka title')

st.sidebar.metric('Revenue','Rs 3L','3%')


# column

st.write('here we are using 2 column')

col1,col2 = st.columns(2)  # no. of column

with col1:
    st.markdown("""
    ### my favorite movies

    - race3
    - housefull
    - golmall

""")

with col2:
    st.markdown("""
    ### my favorite color

    - blue
    - black
    - green

""")


#    SHOWING STATUS

#progress bar

st.error('login failed')

st.success('login successfull')

st.info('login done')

st.warning('this migh be error')


# if something take time to execute then we can show a progress msg -- progress of task
# first import time

st.write('this is progress bar wrrite which sow that how much time it will take ')

bar=st.progress(0)

for i in range(1,101):
    #time.sleep(0.1)
    bar.progress(i)



## TAKING USER INPUT

#taking text input

email = st.text_input('enter email')


# number input

number = st.number_input('enter age')


# date input

st.date_input('enter a number')


st.time_input('enter time')



# BUTTON



email = st.text_input('enter email')

password = st.text_input('enter password')

#this is used for dropdown
gender = st.selectbox('select gender',['male','female','others'])

#creating a button
btn = st.button('login karo')

# if button is clicked

if btn:  # agar buttoin press hua hai then 
    if email == 'ratan@gmail.com' and password =='1234':
        st.balloons()
        #st.success('login successful')
        st.write(gender)

    else:
        st.error('login failed')
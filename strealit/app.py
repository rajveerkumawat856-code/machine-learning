import streamlit as st

# st.title("My First Streamlit App") ## to give the heading to the webpage
# st.subheader('Made by streamlit')
# st.text('this is use to add text to the webpage')
# st.write('my name is rajveer')

# ## selectbox --> use to make the box box which can be selected

# chai=st.selectbox('Your Fav Chai',['A','B','C'])
# st.write(f"Your Choise {chai}. Excellent Choise")
# st.success('your option is been selected') ### it will give the option a green shadow 

# ## it is use to add the radio butter 

# chai_type=st.radio('Select the chai type',['X','Y'])

# ## it is use to make the slider

# suger=st.slider('choose the range',2,4,6)

# # if we have to take the uncontrolled input then we use

# cusp=st.number_input('how many cups',min_value=1,max_value=10)


# name=st.text_input("enter the name")
# if name:
#     st.write(f"welcome {name} your chai is on the way")


# dob=st.date_input('enter the dob')
# st.write(f"your dob is {dob}")


# # to make the col in the webpage

# col1,col2= st.columns(2)
# with col1:
#     st.header('rajveer')
#     vote1=st.button('rajveer')
# with col2:
#     st.header('kumawat')
#     vote2=st.button('kumawat')


# # to add the side bar in the webpage

# name=st.sidebar.text_input('enter your name')
# tra=st.sidebar.selectbox('choose the appropriate things',['a','b'])

# with st.expander('show the tips for ML'):
#     st.write("""
#               1.what are you doing.
#               2.how is your life is going on
#             """)


# for data science part we are going for the dataset and how to work with it and also with the pandas

# import pandas as pd
# st.title('Chocolate sales dataset')
# file=st.file_uploader('uplode your csv type:',type=['csv'])
# if file:
#     df=pd.read_csv(file)
#     st.subheader('Preview of file')
#     st.dataframe(df)

# if file:
#     countries=df['Country'].unique()
#     selected_country=st.selectbox('filter by cities',countries)
#     filtered_data=df[df['Country']==selected_country]
#     st.dataframe(filtered_data)
import streamlit as st
from PIL import Image
answer=""
st.title("3. White")
st.write("White is able to hide everything. . .")
st.write("In this question, you have to find out a location of the image. Let's find out the word from the picture at this [Google document files](https://docs.google.com/document/d/19ue7jX9jwAhHR02uWkIxgE4DlBt7JUBBT5yHpejt2mg/edit?usp=sharing)")
st.write("Enter the word I took this picture")

answer=st.text_input("Enter the restaurant I took this picture")
if answer in ["Too bright"]:
    st.success("Perfect!")
elif answer =="":
    st.write()
else:
    st.error("Incorrect")
if st.button("Hint 1"):
    st.write("You need to edit the picture, but you don't have a permission.")
if st.button("Hint 2"):
    st.write("In google ducument, you can edit a file if you copy the file you don't have a permmission")
if st.button("Hint 3"):
    st.write("After you copy the file, click the image and Image edit function. you can see anything")
import streamlit as st
from PIL import Image

url="test"
answer=""
st.title("4.Identify the location I took the picture at")
st.write("Difficult/難しい")
st.write("I took this picture while driving from __Fujinomiya City__ to __Motosu Lake__ in Japan by __car__. There is __no information__ that can be obtained by __ropping or color adjustment__ as in other problems. Please find the location based on the above clues and the information in the image.")
st.write("Please enter the top __4 alphabetic digits__ of the Plus code of the location by Google Map")
st.write("Enter the restaurant I took this photo")

with open("data/sample1.jpg", "rb") as file:
    img_data = file.read()

# ダウンロードボタンを表示
st.download_button(
    label="Image downlord",         # ボタンに表示するラベル
    data=img_data,                     # ダウンロードするデータ
    file_name="downloaded_image.jpg",  # ダウンロードファイル名
    mime="image/jpeg"                  # MIMEタイプ
)

img = Image.open('data/sample1.jpg')
# use_column_width 実際のレイアウトの横幅に合わせるか
st.image(img)

answer=st.text_input("Enter the Plus code of the location I took this picture")
if answer in ["CHJW"]:
    st.success("Perfect!")
elif answer =="":
    st.write()
else:
    st.error("Incorrect")
if st.button("Hint 1"):
    st.write("The mountain in the photo is the famous Mt.Fuji You can check the time from the details of this photo.")
if st.button("Hint 2"):
    st.write("Furthermore, the angle of the sun can be determined from the time. [angle of sun Link](https://keisan.casio.jp/exec/system/1185781259)")
if st.button("Hint 3"):
    st.write("Look for an aerial view of Google Maps to find a place where you can stop your car.")
if st.button("Hint 4"):
    st.write("Calculations show that the sun is to the southeast at this location. On the road from Fujinomiya City to Motosuko Lake, where is the open road with no obstruction where you can stop your car and see Mt. Fuji on the southeast side?")

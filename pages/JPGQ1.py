import streamlit as st
from PIL import Image

url="test"
answer=""
st.title("1.Confidencial information of a Image")
st.write("A JPG image has some confidenccial information such as Location, time and etc.")
st.write("In this question, you have to find out a location of the image. Please downlord the iamge or copy this image url")
st.write("Enter the restaurant I took this picture")

with open("data/sample.jpg", "rb") as file:
    img_data = file.read()

# ダウンロードボタンを表示
st.download_button(
    label="Image downlord",         # ボタンに表示するラベル
    data=img_data,                     # ダウンロードするデータ
    file_name="downloaded_image.jpg",  # ダウンロードファイル名
    mime="image/jpeg"                  # MIMEタイプ
)

img = Image.open('data/sample.jpg')
# use_column_width 実際のレイアウトの横幅に合わせるか
st.image(img)

answer=st.text_input("Enter the restaurant I took this picture")
if answer in ["Blenz Coffee","blenz coffee","BlenzCoffee","blenzcoffee"]:
    st.success("Perfect!")
elif answer =="":
    st.write()
else:
    st.error("Incorrect")
if st.button("Hint 1"):
    st.write("The information attached JPG image is named EXIF information. Moreover, EXIF analysis Websites are posted in internet.")
if st.button("Hint 2"):
    st.write("Something may be happened if you visit and post the image at this [website](https://compress-or-die.com/analyze)")
import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("اصدار سند قبض")

st.write(
    "نطبع لك سند القبض باسرع و اسهل طريقة"
)

left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("ارجو كتابة المعلومات الصحيحة")
form = left.form("template_form")
student = form.text_input("أسم المكرم")
course = form.selectbox(
    "Choose course",
    ["ايجار مقدم", "تأمين مقدم"],
    index=0,
)
grade = form.slider("Grade", 500, 3500, 1000)
submit = form.form_submit_button("اطبع السند")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/Saudi Riyal",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 تم اصدار سند القبض")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )

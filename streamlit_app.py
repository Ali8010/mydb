import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="!!", page_title="Receipt Voucher")
st.title("Receipt Voucher اصدار سند قبض")

st.write(
    "نطبع لك سند القبض باسرع و اسهل طريقة"
)

left, right = st.columns(2)

right.write(" Here's the template we'll be using:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Please fill in  ارجو كتابة المعلومات الصحيحة")
form = left.form("template_form")
student = form.text_input("Name أسم المكرم")
course = form.selectbox(
    "Choose course",
    ["Rent", "Insurance"],
    index=0,
)
grade = form.slider("How much قيمة المبلغ", 500, 5000, 1000)
submit = form.form_submit_button("Print اطبع السند")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/Saudi Riyal",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Congratulations Your Receipt was issued تم اصدار سند القبض")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="diploma.pdf",
        mime="application/octet-stream",
    )

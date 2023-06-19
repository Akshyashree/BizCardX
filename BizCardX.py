import streamlit as st
import easyocr
import sqlite3
from PIL import Image
import numpy as np
import mysql.connector 

# Create a database or connect to one
#conn = sqlite3.connect('business_card.db')
conn = mysql.connector.connect(user='root', password='Csa1809', host='localhost', database="BisCardX")
c = conn.cursor()

# Create table
c.execute("""CREATE TABLE IF NOT EXISTS business_card (
            image BLOB,
            company_name text,
            card_holder_name text,
            designation text,
            mobile_number text,
            email_address text,
            website_url text,
            area text,
            city text,
            state text,
            pin_code text
            )""")

# Commit changes and close connection
conn.commit()
conn.close()

# Initialize the OCR reader
reader = easyocr.Reader(['en'])
def app():
    st.title("Bizard Extraction")
    st.subheader("Extract data from Business Card")
    st.image(Image.open(r"C:\Users\snaks\OneDrive\Desktop\DT3\Prj\prj 3\images\top_banner.jpg"))
    # Upload the image
    image_file = st.file_uploader("Upload Image", type=['jpg', 'png'])

    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        if st.button("Extract Information"):
            # Convert the image to grayscale
            gray_image = np.array(image.convert('L'))

            # Use easyOCR to extract text
            result = reader.readtext(gray_image)

            # Extracted information
            extracted_info = [item[1] for item in result]
            st.write(extracted_info)

            if st.button("Save Information"):
                # Connect to the database
                conn = sqlite3.connect('business_card.db')
                c = conn.cursor()

                # Insert the data into the database
                c.execute("INSERT INTO business_card VALUES (:image, :company_name, :card_holder_name, :designation, :mobile_number, :email_address, :website_url, :area, :city, :state, :pin_code)",
                          {
                              'image': image_file.getvalue(),
                              'company_name': extracted_info[0],
                              'card_holder_name': extracted_info[1],
                              'designation': extracted_info[2],
                              'mobile_number': extracted_info[3],
                              'email_address': extracted_info[4],
                              'website_url': extracted_info[5],
                              'area': extracted_info[6],
                              'city': extracted_info[7],
                              'state': extracted_info[8],
                              'pin_code': extracted_info[9]
                          })

                # Commit changes and close connection
                conn.commit()
                conn.close()

                st.success("Information saved successfully!")

if __name__ == "__main__":
    app()

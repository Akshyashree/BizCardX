# About BizCardX
In this streamlit web app you can upload an image of a business card and extract relevant information from it using easyOCR. You can view, modify or delete the extracted data in this app. This app would also allow users to save the extracted information into a database along with the uploaded business card image. The database would be able to store multiple entries, each with its own business card image and extracted information.

# Program Explaination

```python
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
```
- The code imports the `pandas` library for data manipulation and analysis.
- It imports the `streamlit` library for creating interactive web applications.
- It imports the `option_menu` function from the `streamlit_option_menu` library, which provides a customized option menu for selecting different sections in the application.

```python
import easyocr
import mysql.connector as sql
from PIL import Image
import cv2
import os
import matplotlib.pyplot as plt
import re
import mysql
```
- The code imports various libraries and modules required for image processing, OCR, database connectivity, and visualization. These include `easyocr` for optical character recognition, `mysql.connector` for connecting to MySQL database, `PIL` (Python Imaging Library) for image manipulation, `cv2` (OpenCV) for image processing tasks, `os` for operating system-related tasks, `matplotlib.pyplot` for plotting images, `re` for regular expression matching, and `mysql` for MySQL operations.

```python
mydb = mysql.connector.connect(host="localhost", user="root", password="Csa1809", database="bizcardx_db")
mycursor = mydb.cursor(buffered=True)
```
- These lines establish a connection to the MySQL database named "bizcardx_db" using the `mysql.connector` library. It sets the host, username, password, and database name for the connection. The `mycursor` variable is used to execute SQL queries and fetch results from the database.

```python
selected = option_menu(None, ["Home","Upload + Extract","Alter or Delete"], icons=["home","cloud-upload-alt","edit"], default_index=0, orientation="horizontal", styles={...})
```
- This line uses the `option_menu` function to create a customized menu with icons for different sections of the application. The `option_menu` function takes parameters such as the default section, section names, icons for each section, and styling options.

```python
reader = easyocr.Reader(['en'])
```
- This line creates an instance of the `easyocr.Reader` class with the language parameter set to `['en']`, indicating English language text recognition. It initializes the OCR reader for extracting text from images.

```python
mycursor.execute('''CREATE TABLE IF NOT EXISTS card_data (id INTEGER PRIMARY KEY AUTO_INCREMENT, company_name TEXT, card_holder TEXT, designation TEXT, mobile_number VARCHAR(50), email TEXT, website TEXT, area TEXT, city TEXT, state TEXT, pin_code VARCHAR(10), image LONGBLOB)''')
```
- This line executes an SQL query to create a table named `card_data` in the MySQL database if it doesn't already exist. The table schema includes columns for various extracted fields such as company name, card holder name, designation, mobile number, email, website, area, city, state, pin code, and an image column for storing the business card image as a binary large object (BLOB).

```python
if selected == "Home":
    st.video(r"C:\Users\snaks\OneDrive\Desktop\Sample\biscardimages\biscardintrovdo.mp4")
    st.subheader(":orange[About the App:] ...")
```
- If the selected option is "Home", this block of code displays a video and some text using the `st.video` and `st.subheader` functions from the Streamlit library. It shows an introductory video and provides information about the application.

```python
if selected == "Upload + Extract":
    st.image(Image.open(r"C:\Users\snaks\OneDrive\Desktop\Sample\biscardimages\updatepage.jpg"))
    st.markdown("### Upload a Business Card")
    uploaded_card = st.file_uploader("upload here", label_visibility="collapsed", type=["png","jpeg","jpg"])
    ...
```
- If the selected option is "Upload + Extract", this block of code displays an image, a heading, and a file uploader widget using the `st.image`, `st.markdown`, and `st.file_uploader` functions. It allows the user to upload a business card image in PNG, JPEG, or JPG format.

```python
if selected == "Alter or Delete":
    col1, col2, col3 = st.columns([3, 3, 2])
    st.title("Alter or Delete the data here")
    ...
```
- If the selected option is "Alter or Delete", this block of code creates three columns using the `st.columns` function and sets a title using the `st.title` function. It prepares the interface for altering or deleting the extracted data.

The code continues with further sections for processing the uploaded image, extracting data using OCR, storing the data in the database, and providing options to modify or delete the data. These sections involve functions for image processing, data extraction, dataframe creation, SQL queries, and user interface components provided by the Streamlit library.

Please note that the code assumes specific paths and filenames for images and videos. You may need to modify these paths according to your specific directory structure and file locations.

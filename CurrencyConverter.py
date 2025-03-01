# # Currency Converter

# with open("currencyData.txt") as f:
#     lines = f.readlines()

# currencyDict = {}
# for line in lines:
#     pasred = line.split("\t")
#     currencyDict[pasred[0]] = pasred[1]
    

# amount = int(input("Enter the amount: /n"))
# print("Enter the name of currency want to convert this amount to? Available options: /n")
# [print(item) for item in currencyDict.keys()]
# currency = input("Please enter one of these values: /n")
# print(f"Amount in INR is: {amount * float(currencyDict[currency])} {currency}")        










































# import os

# # Get the directory where this script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "currencyData.txt")

# # Debugging: Print the detected file path
# print(f"Looking for file at: {file_path}")

# # Check if the file exists
# if not os.path.exists(file_path):
#     print(f"Error: currencyData.txt file not found at {file_path}")
#     exit()

# # Open the file with the correct path
# with open(file_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# # Convert data into a dictionary
# currencyDict = {}
# for line in lines:
#     parsed = line.strip().split("\t")  # ✅ FIXED: Now works for tab-separated data
#     if len(parsed) >= 2:
#         currency_name = parsed[0]  # Store full name
#         exchange_rate = float(parsed[1])  # Convert rate to float
#         currencyDict[currency_name] = exchange_rate

# # User Input
# try:
#     amount = float(input("Enter the amount: \n"))  
# except ValueError:
#     print("Error: Please enter a valid numeric amount.")
#     exit()

# print("\nAvailable currency options:\n")
# [print(item) for item in currencyDict.keys()]

# currency = input("\nPlease enter one of these values: ").strip()

# # Validate currency input
# if currency not in currencyDict:
#     print("Error: Invalid currency name entered. Please try again.")
# else:
#     print(f"\nAmount in {currency}: {amount * currencyDict[currency]:.2f}")



















































# import os
# import streamlit as st

# # Get the directory where this script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "currencyData.txt")

# # Debugging: Print the detected file path
# st.text(f"Looking for file at: {file_path}")

# # Check if the file exists
# if not os.path.exists(file_path):
#     st.error(f"Error: currencyData.txt file not found at {file_path}")
#     st.stop()

# # Open the file with the correct path
# with open(file_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# # Convert data into a dictionary
# currencyDict = {}
# for line in lines:
#     parsed = line.strip().split("\t")  # ✅ FIXED: Now works for tab-separated data
#     if len(parsed) >= 2:
#         currency_name = parsed[0]  # Store full name
#         exchange_rate = float(parsed[1])  # Convert rate to float
#         currencyDict[currency_name] = exchange_rate

# # Streamlit UI
# st.title("Currency Converter")

# # User Input in Streamlit
# amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")

# # Dropdown for currency selection
# currency = st.selectbox("Select the currency:", list(currencyDict.keys()))

# # Convert Button
# if st.button("Convert"):
#     if currency in currencyDict:
#         converted_amount = amount * currencyDict[currency]
#         st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
#     else:
#         st.error("Invalid currency selection. Please try again.")



































# import os
# import streamlit as st

# # Get the directory where this script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "currencyData.txt")

# # Debugging: Print the detected file path
# st.text(f"Looking for file at: {file_path}")

# # Check if the file exists
# if not os.path.exists(file_path):
#     st.error(f"Error: currencyData.txt file not found at {file_path}")
#     st.stop()

# # Open the file with the correct path
# with open(file_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# # Convert data into a dictionary
# currencyDict = {}
# for line in lines:
#     parsed = line.strip().split("\t")  # ✅ FIX for tab-separated values
#     if len(parsed) >= 3:
#         currency_name = parsed[0]  
#         inr_to_currency = float(parsed[1])  # INR to that currency
#         currency_to_inr = float(parsed[2])  # That currency to INR

#         # Store both values in dictionary
#         currencyDict[currency_name] = {"inr_to_currency": inr_to_currency, "currency_to_inr": currency_to_inr}

# # Streamlit UI
# st.title("Currency Converter")

# # User Inputs
# amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
# currency = st.selectbox("Select the currency:", list(currencyDict.keys()))

# conversion_type = st.radio("Convert:", ["INR to Currency", "Currency to INR"])

# # Convert Button
# if st.button("Convert"):
#     if currency in currencyDict:
#         if conversion_type == "INR to Currency":
#             converted_amount = amount * currencyDict[currency]["inr_to_currency"]
#             st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
#         else:
#             converted_amount = amount * currencyDict[currency]["currency_to_inr"]
#             st.success(f"{amount} {currency} is equal to {converted_amount:.2f} INR")
#     else:
#         st.error("Invalid currency selection. Please try again.")





















































# import os
# import streamlit as st

# # Set page config (This allows dark/light mode to work better)
# st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")

# # Theme Toggle Using Session State
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "light"  # Default Theme

# # Theme Toggle Button
# if st.button("🌙 Toggle Dark/Light Mode"):
#     st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# # Apply Theme CSS
# dark_mode = st.session_state["theme"] == "dark"
# theme_css = """
#     <style>
#         body { background-color: #0e1117; color: white; }
#         .stApp { background-color: #0e1117; }
#     </style>
# """ if dark_mode else """
#     <style>
#         body { background-color: white; color: black; }
#         .stApp { background-color: white; }
#     </style>
# """
# st.markdown(theme_css, unsafe_allow_html=True)

# # Get the directory where this script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "currencyData.txt")

# # Debugging: Print the detected file path
# st.text(f"Looking for file at: {file_path}")

# # Check if the file exists
# if not os.path.exists(file_path):
#     st.error(f"Error: currencyData.txt file not found at {file_path}")
#     st.stop()

# # Open the file with the correct path
# with open(file_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# # Convert data into a dictionary
# currencyDict = {}
# for line in lines:
#     parsed = line.strip().split("\t")  # ✅ FIX for tab-separated values
#     if len(parsed) >= 3:
#         currency_name = parsed[0]  
#         inr_to_currency = float(parsed[1])  # INR to that currency
#         currency_to_inr = float(parsed[2])  # That currency to INR

#         # Store both values in dictionary
#         currencyDict[currency_name] = {"inr_to_currency": inr_to_currency, "currency_to_inr": currency_to_inr}

# # Streamlit UI
# st.title("Currency Converter")

# # User Inputs
# amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
# currency = st.selectbox("Select the currency:", list(currencyDict.keys()))

# conversion_type = st.radio("Convert:", ["INR to Currency", "Currency to INR"])

# # Convert Button
# if st.button("Convert"):
#     if currency in currencyDict:
#         if conversion_type == "INR to Currency":
#             converted_amount = amount * currencyDict[currency]["inr_to_currency"]
#             st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
#         else:
#             converted_amount = amount * currencyDict[currency]["currency_to_inr"]
#             st.success(f"{amount} {currency} is equal to {converted_amount:.2f} INR")
#     else:
#         st.error("Invalid currency selection. Please try again.")























# import os
# import streamlit as st

# # Set page config (This allows dark/light mode to work better)
# st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")

# # Theme Toggle Using Session State
# if "theme" not in st.session_state:
#     st.session_state["theme"] = "light"  # Default Theme

# # Theme Toggle Button
# if st.button("🌙 Toggle Dark/Light Mode"):
#     st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# # Apply Theme CSS
# dark_mode = st.session_state["theme"] == "dark"
# theme_css = """
#     <style>
#         body, .stApp { background-color: #0e1117; color: white; }
#         .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput, .stRadio {
#             color: white !important;
#         }
#         /* Convert Button Fix */
#         .stButton > button {
#             color: black !important; /* Button text will always be black */
#             font-weight: bold;
#         }
#     </style>
# """ if dark_mode else """
#     <style>
#         body, .stApp { background-color: white; color: black; }
#         .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput, .stRadio {
#             color: black !important;
#         }
#         /* Convert Button Fix */
#         .stButton > button {
#             color: black !important; /* Button text will always be black */
#             font-weight: bold;
#         }
#     </style>
# """
# st.markdown(theme_css, unsafe_allow_html=True)

# # Get the directory where this script is located
# script_dir = os.path.dirname(os.path.abspath(__file__))
# file_path = os.path.join(script_dir, "currencyData.txt")

# # Debugging: Print the detected file path
# st.text(f"Looking for file at: {file_path}")

# # Check if the file exists
# if not os.path.exists(file_path):
#     st.error(f"Error: currencyData.txt file not found at {file_path}")
#     st.stop()

# # Open the file with the correct path
# with open(file_path, "r", encoding="utf-8") as f:
#     lines = f.readlines()

# # Convert data into a dictionary
# currencyDict = {}
# for line in lines:
#     parsed = line.strip().split("\t")  # ✅ FIX for tab-separated values
#     if len(parsed) >= 3:
#         currency_name = parsed[0]  
#         inr_to_currency = float(parsed[1])  # INR to that currency
#         currency_to_inr = float(parsed[2])  # That currency to INR

#         # Store both values in dictionary
#         currencyDict[currency_name] = {"inr_to_currency": inr_to_currency, "currency_to_inr": currency_to_inr}

# # Streamlit UI
# st.title("Currency Converter")

# # User Inputs
# amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
# currency = st.selectbox("Select the currency:", list(currencyDict.keys()))

# conversion_type = st.radio("Convert:", ["INR to Currency", "Currency to INR"])

# # Convert Button
# if st.button("Convert"):
#     if currency in currencyDict:
#         if conversion_type == "INR to Currency":
#             converted_amount = amount * currencyDict[currency]["inr_to_currency"]
#             st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
#         else:
#             converted_amount = amount * currencyDict[currency]["currency_to_inr"]
#             st.success(f"{amount} {currency} is equal to {converted_amount:.2f} INR")
#     else:
#         st.error("Invalid currency selection. Please try again.")































































# import sqlite3
# import streamlit as st

# st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")

# st.title("Currency Converter")

# # Function to fetch exchange rate from database
# def get_exchange_rate(currency):
#     conn = sqlite3.connect("currency.db")
#     cursor = conn.cursor()
#     cursor.execute("SELECT rate FROM exchange_rates WHERE currency = ?", (currency,))
#     rate = cursor.fetchone()
#     conn.close()
#     return rate[0] if rate else None

# # User Input
# amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")
# currency = st.selectbox("Select the currency:", ["USD", "EUR", "GBP", "PKR", "AUD"])

# # Convert Button
# if st.button("Convert"):
#     rate = get_exchange_rate(currency)
#     if rate:
#         converted_amount = amount * rate
#         st.success(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
#     else:
#         st.error("Currency not found!")

# # Update Rates Button
# if st.button("Update Exchange Rates"):
#     import update_rates
#     update_rates.update_rates()
#     st.success("Exchange rates updated successfully!")










import sqlite3
import streamlit as st

st.set_page_config(page_title="Currency Converter", page_icon="💰", layout="centered")

st.title("🌍 Multi-Currency Converter")

# Theme Toggle Using Session State
if "theme" not in st.session_state:
    st.session_state["theme"] = "light"  # Default Theme

# Theme Toggle Button
if st.button("🌙 Toggle Dark/Light Mode"):
    st.session_state["theme"] = "dark" if st.session_state["theme"] == "light" else "light"

# Apply Theme CSS
dark_mode = st.session_state["theme"] == "dark"
theme_css = """
    <style>
        body, .stApp { background-color: #0e1117; color: white; }
        .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput, .stRadio {
            color: white !important;
        }
        .stButton > button {
            color: black !important;  /* Button text will always be black */
            font-weight: bold;
        }
    </style>
""" if dark_mode else """
    <style>
        body, .stApp { background-color: white; color: black; }
        .stMarkdown, .stTextInput, .stSelectbox, .stNumberInput, .stRadio {
            color: black !important;
        }
        .stButton > button {
            color: black !important;  /* Button text will always be black */
            font-weight: bold;
        }
    </style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# Function to fetch exchange rate from database
def get_exchange_rate(currency):
    conn = sqlite3.connect("currency.db")
    cursor = conn.cursor()
    cursor.execute("SELECT rate FROM exchange_rates WHERE currency = ?", (currency,))
    rate = cursor.fetchone()
    conn.close()
    return rate[0] if rate else None

# User Input
amount = st.number_input("Enter the amount:", min_value=0.0, format="%.2f")

# Dropdowns for selecting currencies
currencies = ["USD", "EUR", "GBP", "PKR", "AUD", "CAD", "JPY", "CNY", "AED", "SAR", "TRY"]
from_currency = st.selectbox("Convert From:", currencies)
to_currency = st.selectbox("Convert To:", currencies)

# Convert Button
if st.button("Convert"):
    from_rate = get_exchange_rate(from_currency)
    to_rate = get_exchange_rate(to_currency)

    if from_rate and to_rate:
        converted_amount = (amount / from_rate) * to_rate
        st.success(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        st.error("Currency not found!")

# Update Rates Button
if st.button("Update Exchange Rates"):
    import update_rates
    update_rates.update_rates()
    st.success("Exchange rates updated successfully!")

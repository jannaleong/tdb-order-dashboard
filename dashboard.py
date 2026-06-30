import streamlit as st
from order_processor import process_orders

# set windows tab
st.set_page_config(
    page_title="The Daily Blooms Dashboard",
    page_icon="🌸",
    layout="wide"
)

df = process_orders()

# display drop down menu to select date and delivery/pickup slot
dates = sorted(df["Delivery Date"].dropna().unique())
selected_date = st.selectbox(
    "Delivery Date",
    dates
)

slots = ["All"] + sorted(df["Delivery Slot"].dropna().unique())
selected_slot = st.selectbox(
    "Time Slot",
    slots
)

# filter orders according to data and delivery/pickup slot
filtered = df[
    df["Delivery Date"] == selected_date
]
if selected_slot != "All":
    filtered = filtered[
        filtered["Delivery Slot"] == selected_slot
    ]


st.dataframe(
    filtered,
    use_container_width=True,
    height=700
)
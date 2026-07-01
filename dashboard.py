import streamlit as st
from order_processor import process_orders

def check_password():
    if st.session_state.get("authenticated", False):
        return True

    st.title("🌸 The Daily Blooms Dashboard")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):
        if password == st.secrets["APP_PASSWORD"]:
            st.session_state["authenticated"] = True
            st.rerun()
        else:
            st.error("Incorrect password")

    return False

if not check_password():
    st.stop()

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


filtered = filtered.sort_values(by="SKU")
display_df = filtered.drop(columns=['Delivery Date', 'Delivery Slot'])

st.dataframe(
    filtered,
    use_container_width=True,
    height=700
)
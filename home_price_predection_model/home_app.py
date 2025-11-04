# 📊 KC House Price Analysis App (Streamlit UI)
# Save this as app.py and run using: streamlit run app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import ensemble

# 🧠 Page Configuration
st.set_page_config(page_title="KC House Price Analysis", page_icon="🏠", layout="wide")

st.title("🏠 KC House Price Analysis Dashboard")
st.markdown("Explore, visualize, and model the King County (Seattle) house dataset interactively.")

# 📂 Upload Section
uploaded_file = st.file_uploader("📤 Upload the kc_house_data.csv file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.success("✅ Data uploaded successfully!")

    # Basic Info
    st.subheader("📄 Dataset Preview")
    st.dataframe(data.head())

    st.subheader("📊 Data Summary")
    st.write(data.describe())

    # Sidebar Filters
    st.sidebar.header("🔍 Filter Options")
    selected_plot = st.sidebar.selectbox(
        "Select Visualization",
        [
            "Bedrooms Distribution",
            "Latitude vs Longitude",
            "Price vs Sqft Living",
            "Price vs Longitude",
            "Price vs Latitude",
            "Bedrooms vs Price",
            "Total Living Area vs Price",
            "Waterfront vs Price",
            "Floors Distribution",
        ],
    )

    # Visualization Section
    st.subheader("📈 Visualization")

    if selected_plot == "Bedrooms Distribution":
        fig, ax = plt.subplots()
        data["bedrooms"].value_counts().plot(kind="bar", ax=ax)
        plt.title("Number of Bedrooms")
        plt.xlabel("Bedrooms")
        plt.ylabel("Count")
        st.pyplot(fig)

    elif selected_plot == "Latitude vs Longitude":
        fig = sns.jointplot(x=data.lat.values, y=data.long.values, height=8)
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        st.pyplot(fig.fig)

    elif selected_plot == "Price vs Sqft Living":
        fig, ax = plt.subplots()
        ax.scatter(data.price, data.sqft_living, alpha=0.5)
        plt.title("Price vs Square Feet")
        plt.xlabel("Price")
        plt.ylabel("Square Feet")
        st.pyplot(fig)

    elif selected_plot == "Price vs Longitude":
        fig, ax = plt.subplots()
        ax.scatter(data.price, data.long, alpha=0.5)
        plt.title("Price vs Location (Longitude)")
        plt.xlabel("Price")
        plt.ylabel("Longitude")
        st.pyplot(fig)

    elif selected_plot == "Price vs Latitude":
        fig, ax = plt.subplots()
        ax.scatter(data.price, data.lat, alpha=0.5)
        plt.title("Latitude vs Price")
        plt.xlabel("Price")
        plt.ylabel("Latitude")
        st.pyplot(fig)

    elif selected_plot == "Bedrooms vs Price":
        fig, ax = plt.subplots()
        ax.scatter(data.bedrooms, data.price, alpha=0.5)
        plt.title("Bedrooms vs Price")
        plt.xlabel("Bedrooms")
        plt.ylabel("Price")
        st.pyplot(fig)

    elif selected_plot == "Total Living Area vs Price":
        fig, ax = plt.subplots()
        total_sqft = data["sqft_living"] + data["sqft_basement"]
        ax.scatter(total_sqft, data.price, alpha=0.5)
        plt.title("Total Living Area (SqFt) vs Price")
        plt.xlabel("Total SqFt")
        plt.ylabel("Price")
        st.pyplot(fig)

    elif selected_plot == "Waterfront vs Price":
        fig, ax = plt.subplots()
        ax.scatter(data.waterfront, data.price, alpha=0.5)
        plt.title("Waterfront vs Price (0 = No Waterfront)")
        plt.xlabel("Waterfront")
        plt.ylabel("Price")
        st.pyplot(fig)

    elif selected_plot == "Floors Distribution":
        fig, ax = plt.subplots()
        data.floors.value_counts().plot(kind="bar", ax=ax)
        plt.title("Distribution of Floors")
        plt.xlabel("Floors")
        plt.ylabel("Count")
        st.pyplot(fig)

    # Machine Learning Section
    st.subheader("🤖 Simple Price Prediction Model")

    # Drop unnecessary columns
    train1 = data.drop(["id", "date"], axis=1, errors="ignore")
    X = train1.drop("price", axis=1)
    y = data["price"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model_choice = st.selectbox("Choose Model", ["Linear Regression", "Gradient Boosting"])

    if st.button("Train Model"):
        if model_choice == "Linear Regression":
            model = LinearRegression()
        else:
            model = ensemble.GradientBoostingRegressor()

        model.fit(X_train, y_train)
        score = model.score(X_test, y_test)

        st.success(f"✅ Model trained successfully! Accuracy: {score:.2f}")

else:
    st.warning("👆 Please upload a dataset to get started.")

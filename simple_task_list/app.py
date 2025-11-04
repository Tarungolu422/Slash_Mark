# task_app.py
import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import random
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="🧠 Smart Task Manager",
    page_icon="✅",
    layout="wide"
)

# ---------- CUSTOM BACKGROUND & STYLING ----------
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(135deg, #1f1c2c, #928dab);
    background-attachment: fixed;
    background-size: cover;
}

[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

[data-testid="stSidebar"] {
    background-image: linear-gradient(180deg, #2c5364, #203a43, #0f2027);
    color: white;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: #f0f0f0 !important;
}

div.stButton > button {
    background-color: #00b4d8;
    color: white;
    border-radius: 10px;
    border: none;
    padding: 0.6em 1.2em;
    font-size: 16px;
    font-weight: 600;
    transition: all 0.3s ease;
}

div.stButton > button:hover {
    background-color: #0077b6;
    transform: scale(1.05);
}

.sidebar .sidebar-content {
    background-color: #0f2027;
}

.stDataFrame {
    background: rgba(255,255,255,0.1);
}

hr {
    border-top: 1px solid #bbb;
}

[data-testid="stMarkdownContainer"] strong {
    color: #FFD700 !important;
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown("<h1 style='text-align: center;'>🧠 Smart Task Management App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Manage your tasks and let AI predict their priority!</p>", unsafe_allow_html=True)

# ---------- LOAD OR CREATE TASKS ----------
if os.path.exists("tasks.csv"):
    tasks = pd.read_csv("tasks.csv")
else:
    tasks = pd.DataFrame(columns=["description", "priority"])

# ---------- SAVE FUNCTION ----------
def save_tasks():
    tasks.to_csv("tasks.csv", index=False)

# ---------- TRAIN ML MODEL ----------
def train_model():
    if len(tasks) > 1:
        model = make_pipeline(CountVectorizer(), MultinomialNB())
        model.fit(tasks["description"], tasks["priority"])
        return model
    return None

# ---------- SIDEBAR MENU ----------
st.sidebar.header("📋 Menu")
menu = st.sidebar.radio(
    "Choose an action:",
    ["➕ Add Task", "📋 View Tasks", "🗑️ Remove Task", "🤖 AI Recommendation"]
)

# ---------- ADD TASK ----------
if menu == "➕ Add Task":
    st.subheader("➕ Add a New Task")
    description = st.text_input("📝 Task Description:")
    priority = st.selectbox("⭐ Priority:", ["Low", "Medium", "High"])

    if st.button("Add Task"):
        if description.strip():
            new_task = pd.DataFrame({"description": [description], "priority": [priority]})
            tasks = pd.concat([tasks, new_task], ignore_index=True)
            save_tasks()
            st.success(f"✅ Task added: **{description}** with priority **{priority}**")
        else:
            st.warning("⚠️ Please enter a valid task description.")

# ---------- VIEW TASKS ----------
elif menu == "📋 View Tasks":
    st.subheader("📋 Your Current Tasks")
    if tasks.empty:
        st.info("No tasks found. Add one from the sidebar!")
    else:
        st.dataframe(tasks, use_container_width=True)

# ---------- REMOVE TASK ----------
elif menu == "🗑️ Remove Task":
    st.subheader("🗑️ Remove a Task")
    if tasks.empty:
        st.info("No tasks to remove.")
    else:
        selected_task = st.selectbox("Select a task to remove:", tasks["description"])
        if st.button("Remove Task"):
            tasks = tasks[tasks["description"] != selected_task]
            save_tasks()
            st.success(f"🗑️ Task removed: {selected_task}")

# ---------- AI RECOMMENDATION ----------
elif menu == "🤖 AI Recommendation":
    st.subheader("🤖 AI Task Priority Predictor")
    model = train_model()

    if model:
        st.markdown("### 🔍 Predict Priority for a New Task")
        new_task = st.text_input("Enter a new task description:")
        if st.button("Predict Priority"):
            if new_task.strip():
                predicted_priority = model.predict([new_task])[0]
                st.success(f"🧠 Predicted Priority: **{predicted_priority}**")
            else:
                st.warning("⚠️ Please enter a task description to predict.")

        st.markdown("---")
        st.markdown("### 🎯 Random Recommendation from Your Tasks")
        random_task = random.choice(tasks["description"])
        predicted_priority = model.predict([random_task])[0]
        st.info(f"Try this task: **{random_task}** → Predicted Priority: **{predicted_priority}**")
    else:
        st.warning("⚠️ Not enough data to train the model. Add at least 2 tasks!")

# ---------- FOOTER ----------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #ccc;'>🧩 Built with ❤️ using Streamlit & Scikit-learn | Tarun’s Smart Task App</p>", unsafe_allow_html=True)

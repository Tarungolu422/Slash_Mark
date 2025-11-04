```

```

# 🧠 Smart Task Management App

### 🚀 An AI-powered productivity assistant built with **Streamlit**, **Scikit-learn**, and **Pandas**

---

## 📋 Overview

The **Smart Task Management App** is an intelligent task organizer that not only allows you to add, view, and remove tasks but also uses **Machine Learning** to predict task priorities automatically. It’s designed for students, professionals, and anyone looking to manage their to-do lists efficiently with a touch of AI.

This app combines the simplicity of **Streamlit’s interactive UI** with the intelligence of **Natural Language Processing (NLP)** using **Scikit-learn’s Naive Bayes classifier**. As you continue adding tasks and labeling them with priorities (Low, Medium, High), the AI learns patterns from your descriptions and begins to predict which future tasks are likely to be high or low priority. It’s like having your own smart assistant that helps you decide what to work on next.

The interface is visually enhanced with a **gradient background**, modern button styles, and smooth transitions, creating a professional yet aesthetic user experience.

---

## 🌟 Features

The Smart Task Management App offers a range of features that make it both practical and intelligent. You can easily add new tasks with a description and priority label, view all existing tasks in an interactive table, and remove tasks you’ve completed. The app automatically saves all your data in a `tasks.csv` file, ensuring persistence even after restarting the application.

The highlight feature is the **AI Priority Predictor**, which uses text classification to understand your task descriptions and predict their likely priority levels. The app can also recommend a random task from your existing list and predict its priority for you. You can upload your own background image for a personalized experience, and a built-in bar chart visualizes your task distribution across priority levels. Everything runs seamlessly within a simple web browser.

---

## 🧱 Tech Stack

This project is built using a robust and lightweight stack of technologies. The **frontend** is developed with **Streamlit**, providing an interactive and reactive user interface. The **machine learning** functionality is powered by **Scikit-learn**, utilizing `CountVectorizer` for text feature extraction and `MultinomialNB` for Naive Bayes classification. Data storage and manipulation are handled with **Pandas**, while **CSV files** serve as the local database for persistence. The interface styling uses **custom CSS** injected directly into the Streamlit app to create smooth gradients, hover effects, and color themes.

---

## 📦 Installation

To get started with this app, first clone or download the repository to your local system. Then navigate to the project directory and install the required Python dependencies. The steps below explain the full setup process.

First, clone the repository:

```bash
git clone https://github.com/<your-username>/smart-task-manager.git
cd smart-task-manager
```

Next, install the dependencies from the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Finally, launch the Streamlit app by running:

```bash
streamlit run task_app.py
```

Once the command executes, your default browser will open with the app interface. From there, you can start adding tasks, exploring AI predictions, and enjoying the interactive experience.

---

## 🧭 How to Use

When you open the app, you’ll see a sidebar menu that serves as your navigation control panel. You can select one of the five main sections: **Add Task**, **View Tasks**, **Remove Task**, **AI Recommendation**, or **Settings**.

In the **Add Task** section, enter your task description and select its priority (Low, Medium, or High). Once added, it will be saved instantly.

The **View Tasks** section displays your current list of tasks in an organized table. You can also see a bar chart showing how many tasks belong to each priority category.

In **Remove Task**, you can choose a task description from the dropdown list and delete it permanently.

The **AI Recommendation** page is where the magic happens. Here, the Naive Bayes model analyzes your existing tasks, trains itself, and then predicts the priority of new tasks you type. It also gives you a random task recommendation along with its predicted priority.

The **Settings** page allows you to export your task data, clear all entries, and read troubleshooting tips about the app.

All your tasks are automatically stored in `tasks.csv`, ensuring your data remains even after closing the app.

---

## 🤖 How the AI Works

The AI system in this app is built around **text classification** using **Scikit-learn’s Naive Bayes algorithm**. It works by analyzing your past tasks and learning patterns in the text that correspond to different priority levels.

When you input a new task, the model uses the trained data to predict whether it’s likely to be a **High**, **Medium**, or **Low** priority based on the words and phrases you used. For example, if you frequently label tasks like “Submit report” or “Complete project” as “High,” the AI learns that these words are strong indicators of importance and will predict future similar tasks as “High.”

The app automatically retrains the model whenever you visit the AI page, provided you have at least two labeled tasks. This makes it adaptive and responsive as you add more examples.

---

## 🎨 UI Design and Styling

The user interface was carefully designed to be clean, modern, and easy to use. The app uses a **purple-to-grey gradient background**, providing a calm yet professional tone. Buttons are rounded, colorful, and animated on hover, creating a sense of depth and interactivity. The sidebar has a dark gradient background to make the main section stand out, while task tables have a subtle transparency effect, giving the UI a “glass” aesthetic.

Additionally, users can upload their own background image to replace the default gradient, allowing for full personalization of the visual experience.

---

## ⚙️ File Structure

The project follows a simple, modular structure to make it easy to maintain and extend:

```
smart-task-manager/
├── app.py          # Main Streamlit application file
├── tasks.csv            # Data file automatically generated by the app
├── requirements.txt     # Dependency list for easy setup
└── README.md            # Project documentation (this file)
```

---

## ⚠️ Challenges Faced

Building this project presented a few key challenges, each of which led to meaningful learning experiences.

The first major challenge was dealing with **small dataset limitations**. Since the model learns from user-inputted tasks, early predictions were inconsistent when only a few samples were available. To fix this, a condition was added to train the model only when at least two tasks exist, ensuring more stable learning.

The second challenge involved **Streamlit’s state management**. Because Streamlit re-runs the entire script whenever a user interacts with the app, maintaining data between sessions required careful use of `st.session_state` and saving all changes to a CSV file for persistence.

Another challenge came from **UI customization**. Streamlit doesn’t natively allow full background control or complex styling. This was overcome by injecting **custom CSS** via `st.markdown`, enabling gradient backgrounds, rounded buttons, and animations.

Finally, **model retraining performance** was considered. Since the model retrains every time the AI page is opened, this could become slow with larger data. For now, this isn’t an issue for small task lists, but future versions could use caching or pre-trained models to optimize performance.

---

## 💡 Future Enhancements

While the app is functional and beautiful, there are several exciting improvements planned for the future.

A **priority distribution dashboard** with pie and bar charts could provide better visual analytics.
A **chat-style AI assistant** could help users generate new tasks or categorize them automatically using natural language.
Support for **task deadlines, reminders, and progress tracking** would make the app a complete productivity suite.
Finally, migrating from **CSV files** to a database such as **SQLite or MongoDB** would enable multi-user functionality and cloud storage.

---

## 🤝 Contributing

Contributions are always welcome! If you’d like to improve the app, add visual elements, optimize the machine learning model, or enhance interactivity, simply fork the repository, make your changes, and submit a pull request. Please include descriptive commit messages and keep your code clean and modular.

---

## 🧑‍💻 Author

This project was created by **Tarun Kumar Rathore**, an aspiring professional in **Generative AI, Data Science, Machine Learning, and Data Analytics**.
Tarun’s focus is on building practical AI applications that combine strong engineering principles with accessible user experiences.

## 🌟 Final Thoughts

The **Smart Task Management App** showcases the power of combining simple UI frameworks like **Streamlit** with basic machine learning techniques to create something useful, beautiful, and intelligent.

It’s more than just a to-do list — it’s a personalized assistant that learns from you.
With future updates, it could evolve into a full-fledged productivity ecosystem.

If you enjoy this project, consider giving it a ⭐ on GitHub and sharing it with your peers. Every bit of support helps this project grow and improve.

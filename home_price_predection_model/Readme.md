# 🏠 KC House Price Analysis & Prediction App

An interactive **Streamlit web app** for exploring, visualizing, and predicting **King County (Seattle) house prices** using **machine learning** and **data visualization** techniques.

---

## 🚀 Overview

This project provides a complete data analysis workflow — from **EDA (Exploratory Data Analysis)** to **Machine Learning Model Training** — all accessible through a simple and interactive UI.

You can:
- Upload your dataset  
- Visualize different house features  
- Explore how price correlates with attributes  
- Train models like **Linear Regression** and **Gradient Boosting**  
- Instantly view accuracy results

---

## 🧩 Features

✅ Upload any CSV dataset (compatible with kc_house_data.csv)  
✅ Interactive visualizations using **Matplotlib** and **Seaborn**  
✅ Sidebar controls for selecting plots  
✅ Preprocessing & model training directly from the browser  
✅ Compare **Linear Regression** and **Gradient Boosting**  
✅ Responsive and minimal UI built with Streamlit  

---

## 🛠️ Tech Stack

| Category | Tools |
|-----------|--------|
| Language | Python |
| Framework | Streamlit |
| ML Libraries | scikit-learn, pandas, numpy |
| Visualization | Matplotlib, Seaborn |

---

## 🧠 Machine Learning Workflow

1. **Data Loading** – Upload your CSV file  
2. **Data Cleaning** – Remove null or irrelevant columns  
3. **EDA** – Interactive graphs for understanding relationships  
4. **Model Training** – Choose between Linear Regression or Gradient Boosting  
5. **Evaluation** – R² score shown instantly on UI  

---

## 💻 How to Run

### 1️⃣ Clone or Download
```bash
git clone https://github.com/yourusername/kc-house-price-app.git
cd kc-house-price-app
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App
```bash
streamlit run app.py
```

### 4️⃣ Upload Dataset
Upload the file `kc_house_data.csv` from the Streamlit sidebar and start exploring!

---

## 📊 Visualizations

The app includes multiple plot options:
- Bedrooms Distribution  
- Latitude vs Longitude  
- Price vs Sqft Living  
- Price vs Longitude  
- Price vs Latitude  
- Bedrooms vs Price  
- Total Living Area vs Price  
- Waterfront vs Price  
- Floors Distribution  

*(You can choose any from the sidebar dropdown)*

---

## 🧩 Example Dataset

You can download the **KC House Dataset** from [Kaggle – King County House Data](https://www.kaggle.com/datasets/harlfoxem/housesalesprediction)

---

## 💪 Challenges (for Practice)

Try these challenges to deepen your learning:

1. **Feature Engineering**
   - Create new columns like `price_per_sqft`, `house_age`, etc.
   - Check how they impact model performance.

2. **Model Comparison**
   - Add more ML models: Random Forest, XGBoost, Decision Tree.
   - Plot model accuracy comparison chart.

3. **Hyperparameter Tuning**
   - Use GridSearchCV to optimize Gradient Boosting parameters.

4. **Prediction UI**
   - Add a sidebar input form where users can manually enter house details and get a predicted price.

5. **Data Insights**
   - Add correlation heatmap.
   - Highlight top 5 most expensive houses.

6. **Save Model**
   - Implement model saving/loading using `joblib`.

7. **Deployment**
   - Deploy the app on **Streamlit Cloud** or **Hugging Face Spaces**.

---

## 📸 Screenshots

*(Add your screenshots here after running the app)*  
`/screenshots/home.png`  
`/screenshots/visualization.png`  
`/screenshots/model.png`

---

## 🧑‍💻 Author

**Tarun Kumar Rathore**  
💼 Data Science | Generative AI | ML Engineer | Analytics  
📧 Contact: [your email here]  
🌐 Portfolio: [your link]

---

## 🏁 License

This project is open-source under the **MIT License**.

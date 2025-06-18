# 🧠 Customer Segmentation Project

This project, completed during the Miuul Data Science Bootcamp, demonstrates how to analyze and segment customers based on their sales behavior.

## 📊 Project Overview

The goal is to study sales data to find different types of customers and group them by how much revenue they bring. This helps us understand customers better and plan marketing more easily.

Key steps include:
- Loading and exploring the dataset
- Analyzing sales distribution by country, source, gender, and age
- Creating meaningful age categories for better segmentation
- Combining demographic features to build customer personas
- Segmenting customers into revenue-based groups (A to D)
- Predicting expected revenue for new customer profiles

## 📂 Code Structure

The analysis is performed in a single script and follows a step-by-step structure:

1. **Data Loading & Initial Exploration**  
   - Load the dataset and display basic statistics and data types.
   - Check for unique values and distributions across variables.

2. **Sales Analysis by Variables**  
   - Analyze sales by `COUNTRY`, `SOURCE`, `SEX`, and `AGE`.
   - Calculate total and average revenue by groupings.

3. **Persona Creation**  
   - Convert `AGE` into categorical ranges.
   - Create level-based customer personas combining demographic features.

4. **Revenue-Based Segmentation**  
   - Segment personas into four groups (`A` to `D`) using quantiles based on average revenue.
   - Summarize each segment by mean, max, and total revenue.

5. **Prediction for New Customers**  
   - Classify hypothetical customers based on demographic profile.
   - Predict their expected segment and average revenue.

### 🧾 Dataset

The dataset (`persona.csv`) is confidential and **not included** in this repository. 

| Variable Name | Description                           |
|---------------|---------------------------------------|
| `PRICE`       | Customer's total spending amount      |
| `SOURCE`      | Device type used to access the platform |
| `SEX`         | Customer's gender                     |
| `COUNTRY`     | Customer's country                    |
| `AGE`         | Customer's age                        |

## 🛠️ Technologies Used

- Python  
- pandas library for data manipulation and analysis

## ▶️ How to Use

> **Note:** The dataset (`persona.csv`) is confidential and **not included** in this repository.  
> To run the analysis, you need to have access to the original dataset.

1. Place the dataset (`persona.csv`) in your working directory.
2. Run the script to perform the segmentation analysis.
3. Explore the results and apply insights for marketing or business decisions.

---

💬 If you have any questions, suggestions, or just want to connect — feel free to reach out!
Your feedback is always welcome!

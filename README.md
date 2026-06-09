# 🧠 GenAI-Powered Business Insights Bot

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-4CAF50?style=for-the-badge&logo=seaborn&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-EE82EE?style=for-the-badge&logo=matplotlib&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere-AI-purple?style=for-the-badge&logo=cohere&logoColor=white)


## Table of Contents
1.  [About The Project](#1-about-the-project)
2.  [Features](#2-features)
3.  [Tech Stack](#3-tech-stack)
4.  [Getting Started](#4-getting-started)
    *   [Prerequisites](#prerequisites)
    *   [Installation](#installation)
    *   [API Key Setup](#api-api-key-setup)
5.  [Usage](#5-usage)
6.  [Project Structure](#6-project-structure)
7.  [Future Enhancements](#7-future-enhancements)
8.  [License](#8-license)
9.  [Contact](#9-contact)

---

## 1. About The Project

The GenAI-Powered Business Insights Bot is an interactive web application designed to empower users with quick and insightful data analysis. By simply uploading a CSV file, the bot automates the Exploratory Data Analysis (EDA) process, generates relevant visualizations, and, most impressively, provides a comprehensive business summary and actionable insights using a Large Language Model (LLM) from Cohere. This tool aims to bridge the gap between raw data and business understanding, making data-driven decisions more accessible.

## 2. Features

*   **CSV Upload**: Easily upload your dataset in CSV format.
*   **Automated EDA**: Automatically displays data preview, information (datatypes, non-null counts), and descriptive statistics.
*   **Intelligent Visualization**: Generates common plots (histograms, bar plots, pair plots, correlation heatmaps) based on the data types and characteristics.
*   **AI-Powered Business Summary**: Leverages the Cohere API to provide:
    *   Key Business Observations
    *   Potential Issues/Anomalies in the data
    *   Actionable Insights/Recommendations
    *   Suggestions for Further Analysis
*   **SQL Querying (Bonus)**: Allows users to run SQL-like queries directly on the uploaded DataFrame using `pandasql`.
*   **Interactive UI**: Built with Streamlit for a user-friendly web interface.

## 3. Tech Stack

*   **Frontend**:
    *   [Streamlit](https://streamlit.io/) - For rapid web application development.
    *   HTML/CSS - For basic styling within Streamlit (via `st.markdown`).
*   **Backend/Data Processing**:
    *   [Python](https://www.python.org/)
    *   [Pandas](https://pandas.pydata.org/) - For data manipulation and analysis.
    *   [Seaborn](https://seaborn.pydata.org/) / [Matplotlib](https://matplotlib.org/) - For statistical data visualization.
*   **Generative AI**:
    *   [Cohere API](https://cohere.com/) - For generating AI-powered business summaries and insights.
*   **SQL Querying**:
    *   [Pandasql](https://pypi.org/project/pandasql/) - Enables SQL queries on Pandas DataFrames.
*   **Environment Management**:
    *   [python-dotenv](https://pypi.org/project/python-dotenv/) - For loading environment variables securely.

## 4. Getting Started

Follow these steps to get your project up and running on your local machine.

### Prerequisites

*   Python 3.8+
*   A Cohere API Key (You can obtain one by signing up on the [Cohere website](https://cohere.com/)).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Nehamerindsouza/Gen-AI---Powered-Business-Insights-Bot-.git
    cd Gen-AI---Powered-Business-Insights-Bot-
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **On Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **On macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### API Key Setup

1.  Create a file named `.env` in the root directory of your project (the same directory as `app.py`).

2.  Add your Cohere API key to this `.env` file in the following format:
    ```
    cohere_api_key="your_cohere_api_key_here"
    ```
    **Important:** Replace `"your_cohere_api_key_here"` with your actual API key. Do **not** commit this `.env` file to your public GitHub repository!

## 5. Usage

1.  **Run the Streamlit application:**
    Ensure your virtual environment is active, then run:
    ```bash
    streamlit run app.py
    ```
    Your browser will automatically open the application (usually at `http://localhost:8501`).

2.  **Upload Your CSV:**
    *   Click on the "Upload your CSV file" button and select a CSV file from your local machine.
    *   The application will automatically display a data preview, information, and descriptive statistics.

3.  **View Visualizations:**
    *   Scroll down to see the auto-generated histograms, bar plots, pair plots, and correlation heatmaps.

4.  **Get AI Insights:**
    *   Navigate to the "AI-Powered Business Insights Summary" section. The Cohere model will analyze your data and present key observations, potential issues, actionable insights, and suggestions for further analysis.

5.  **Run SQL Queries (Optional):**
    *   In the "SQL Querying (Bonus)" section, enter your SQL query using `df` as the table name (e.g., `SELECT * FROM df WHERE Age > 30 LIMIT 5;`).
    *   Click "Run SQL Query" to see the results.

## 6. Project Structure
genai_insights_bot/
├── app.py # Main Streamlit application script
├── requirements.txt # List of Python dependencies
├── .env # Environment variables (e.g., API keys - KEEP PRIVATE!)
└── LICENSE # The proprietary license for this project


## 7. Future Enhancements

*   **More Advanced EDA**: Incorporate outlier detection, anomaly detection, time-series specific analysis, etc.
*   **Interactive Visualizations**: Implement Plotly or Altair for interactive charts.
*   **Customizable AI Prompts**: Allow users to fine-tune the prompt sent to the LLM for more specific insights.
*   **Multiple LLM Support**: Provide options to switch between different LLMs (e.g., Google's Gemini, Anthropic's Claude).
*   **Data Cleaning Suggestions**: AI-driven recommendations for data cleaning based on initial EDA.
*   **Export Options**: Allow exporting the summary and visualizations as PDF/images.
*   **Support for other data formats**: Extend to Excel, JSON, etc.

## 8. License

This software is proprietary and all rights are reserved by Neha Merin Dsouza. It may not be used, copied, modified, or distributed without express written permission. See the `LICENSE` file for full details.

---

## 9. Contact

Neha Merin Dsouza - [wilfredneha94@gmail.com]
Project Link: [https://github.com/Nehamerindsouza/Gen-AI---Powered-Business-Insights-Bot-](https://github.com/Nehamerindsouza/Gen-AI---Powered-Business-Insights-Bot-)

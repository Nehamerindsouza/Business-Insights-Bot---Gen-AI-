import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import os
from dotenv import load_dotenv
import cohere
from pandasql import sqldf

# -------------------- CONFIG --------------------
st.set_page_config(layout="wide", page_title="GenAI Business Insights Bot 🧠")

load_dotenv()
cohere_api_key = os.getenv("cohere_api_key")

if not cohere_api_key:
    st.error("Cohere API key not found. Please set it in your .env file.")
    st.stop()

co = cohere.Client(cohere_api_key)

# -------------------- TITLE --------------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🧠 GenAI Business Insights Bot</h1>", unsafe_allow_html=True)
st.markdown("Upload a CSV → Get EDA + Visuals + AI Business Insights")

# -------------------- CACHING --------------------
@st.cache_data
def load_data(file):
    return pd.read_csv(file)

# -------------------- FILE UPLOAD --------------------
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")

if uploaded_file:

    try:
        df = load_data(uploaded_file)

        # -------------------- BASIC INFO --------------------
        st.success("CSV uploaded successfully!")

        st.subheader("📊 Data Preview")
        st.dataframe(df.head())

        st.subheader("📋 Dataset Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        st.text(buffer.getvalue())

        st.subheader("🔢 Descriptive Statistics")
        st.dataframe(df.describe(include="all"))

        # -------------------- DATA QUALITY CHECK --------------------
        st.subheader("⚠️ Data Quality Report")

        col1, col2 = st.columns(2)

        with col1:
            missing = df.isnull().sum()
            st.write("Missing Values:")
            st.dataframe(missing[missing > 0])

        with col2:
            duplicates = df.duplicated().sum()
            st.write(f"Duplicate Rows: {duplicates}")

        # -------------------- FILTER --------------------
        st.subheader("🔍 Filter Data")
        selected_col = st.selectbox("Select column to filter", df.columns)

        if df[selected_col].dtype == "object":
            selected_val = st.selectbox("Select value", df[selected_col].dropna().unique())
            df = df[df[selected_col] == selected_val]

        # -------------------- SAMPLING --------------------
        if df.shape[0] > 5000:
            st.warning("Large dataset detected. Sampling 5000 rows for visualization.")
            df_vis = df.sample(5000, random_state=42)
        else:
            df_vis = df

        # -------------------- VISUALIZATIONS --------------------
        st.subheader("📉 Visualizations")

        numerical_cols = df_vis.select_dtypes(include=['number']).columns
        categorical_cols = df_vis.select_dtypes(include=['object', 'category', 'bool']).columns

        # Histograms
        if len(numerical_cols) > 0:
            st.markdown("### Numerical Distributions")
            for col in numerical_cols:
                fig, ax = plt.subplots()
                sns.histplot(df_vis[col], kde=True, ax=ax)
                ax.set_title(f"{col}")
                st.pyplot(fig)
                plt.close(fig)

        # Categorical
        if len(categorical_cols) > 0:
            st.markdown("### Categorical Counts")
            for col in categorical_cols:
                fig, ax = plt.subplots(figsize=(8, 4))
                if df[col].nunique() > 20:
                    top = df[col].value_counts().head(20)
                    sns.barplot(x=top.index, y=top.values, ax=ax)
                else:
                    sns.countplot(x=col, data=df, ax=ax)
                plt.xticks(rotation=45)
                st.pyplot(fig)
                plt.close(fig)

        # Pairplot (FIXED)
        if len(numerical_cols) >= 2:
            st.markdown("### Pair Plot")
            cols = numerical_cols[:5]
            try:
                pairplot_fig = sns.pairplot(df_vis[cols])
                st.pyplot(pairplot_fig.fig)
                plt.close(pairplot_fig.fig)
            except Exception as e:
                st.warning(f"Pairplot failed: {e}")

        # Correlation Heatmap
        if len(numerical_cols) > 0:
            st.markdown("### Correlation Heatmap")
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.heatmap(df_vis[numerical_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)
            plt.close(fig)

        # -------------------- AI SUMMARY --------------------
        st.subheader("🧠 AI Business Insights")

        def get_ai_summary(df):

            df_info_buffer = io.StringIO()
            df.info(buf=df_info_buffer)

            df_info_str = df_info_buffer.getvalue()
            df_desc = df.describe(include="all").to_string()
            sample_data = df.head(10).to_string()

            column_details = []

            for col in df.columns:
                dtype = df[col].dtype
                unique_vals = df[col].nunique()

                if pd.api.types.is_numeric_dtype(df[col]):
                    column_details.append(
                        f"{col}: Numeric (min={df[col].min()}, max={df[col].max()}, mean={df[col].mean():.2f})"
                    )
                else:
                    column_details.append(
                        f"{col}: Categorical ({unique_vals} unique values)"
                    )

            prompt = f"""
You are a senior business data analyst.

Dataset Overview:
{column_details}

Dataset Info:
{df_info_str}

Statistics:
{df_desc}

Sample Data:
{sample_data}

Provide:
1. Key insights
2. Data issues
3. Business recommendations
4. Further analysis suggestions

Be concise and practical.
"""

            try:
                response = co.chat(
                message=prompt,
                model="command-r7b-12-2024",
                temperature=0.5,
                max_tokens=800
                )
                return response.text
            except Exception as e:
                return f"Error: {e}"

        if st.button("Generate AI Insights"):
            with st.spinner("Thinking..."):
                summary = get_ai_summary(df)
                st.markdown(summary)

        # -------------------- SQL --------------------
        st.subheader("🧮 SQL Query")

        sql_query = st.text_area("Enter SQL", "SELECT * FROM df LIMIT 10")

        if st.button("Run SQL"):
            try:
                result = sqldf(sql_query, {"df": df})
                st.dataframe(result)
            except Exception as e:
                st.error(e)

    except Exception as e:
        st.error(f"Error: {e}")

# -------------------- FOOTER --------------------
st.markdown("---")
st.caption("Built with Streamlit + Pandas + Seaborn + Cohere")
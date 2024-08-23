import streamlit as st
from streamlit_lottie import st_lottie
import requests
import mysql.connector
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
import pickle
import re

# Function to load Lottie animation from a URL
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Load Lottie animations
lottie_search = load_lottie_url("https://assets7.lottiefiles.com/packages/lf20_jcikwtux.json")

# Streamlit setup
st.markdown("<h1 style='text-align: center; color: #ff4b4b; font-weight: bold;'>YouTube Video Recommendation System</h1>", unsafe_allow_html=True)

# Show Lottie search animation
if lottie_search:
    st_lottie(lottie_search, height=150, key="search")
else:
    st.error("Failed to load animation")

# Database connection
conn = mysql.connector.connect(
    host='xxx',
    user='admin',
    password='yyy',
    port='3306',
    database='Youtube'
)
cursor = conn.cursor()

# Fetch data from the database
cursor.execute('SELECT * FROM videos')
data = cursor.fetchall()
df = pd.DataFrame(data)

# Fetch column names
cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'videos' AND TABLE_SCHEMA = 'Youtube' ORDER BY ORDINAL_POSITION")
columns = cursor.fetchall()
df.columns = [col[0] for col in columns]

# Load pre-trained models
with open('vector.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
with open('pca.pkl', 'rb') as f:
    pca = pickle.load(f)
with open('model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

def recommend_videos(query):
    # Use the pre-fitted vectorizer
    query_vector = vectorizer.transform([query])
    
    # Transform using PCA (ensure PCA was applied during model training)
    query_pca = pca.transform(query_vector.toarray())
    
    # Predict the cluster
    cluster = kmeans.predict(query_pca)[0]
    
    # Return videos from the predicted cluster
    return df[df['cluster'] == cluster]

# Sign-in form
st.sidebar.title("Sign In")

with st.sidebar.form("Sign In"):
    name = st.text_input("Your Name")
    email = st.text_input("Enter your Mail address")
    mobile = st.text_input("Enter your Mobile number")

    sign_in_btn = st.form_submit_button("Submit")
    
    if sign_in_btn:
        # Basic validation using regex
        if re.match(r"^[A-Za-z\s]+$", name) and re.match(r"^[a-z0-9]+@[a-z]+\.[a-z]+$", email) and re.match(r"^\d{10}$", mobile):
            cursor.execute("INSERT INTO Signin(`Name`, `Mail address`, `Mobile`) VALUES (%s, %s, %s)", (name, email, mobile))
            conn.commit()
            st.sidebar.success("Sign-in successful!")
        else:
            st.sidebar.error("Please enter valid details!")

# Input for search query
query = st.text_input('Enter your search:')
filter_option = st.sidebar.radio("Trending", options=["Highest Likes", "Highest Views"])

if query:
    recommended_videos = recommend_videos(query)
    
    if not recommended_videos.empty:  # Check if the DataFrame is not empty
        for _, video in recommended_videos.iterrows():
            col1, col2 = st.columns([1, 2])
            with col1:
                st.image(video["thumbnail_url"])
            with col2:
                st.write(f"**{video['title']}**")
                a, b = st.columns([1, 2])
                with a:
                    st.write(f"Views: :green[{video['views']}]")
                with b:
                    st.write(f"Likes: :red[{video['likes']}]")
    else:
        st.write("No videos found for your query.")
else:
    # Show trending videos based on the selected filter
    if filter_option == "Highest Likes":
        trending_videos = df.sort_values(by="likes", ascending=False)
    else:
        trending_videos = df.sort_values(by="views", ascending=False)

    for _, video in trending_videos.iterrows():
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(video["thumbnail_url"])
        with col2:
            st.write(f"**{video['title']}**")
            a, b = st.columns([1, 2])
            with a:
                st.write(f"Views: :green[{video['views']}]")
            with b:
                st.write(f"Likes: :red[{video['likes']}]")


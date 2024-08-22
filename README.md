# YouTube-Video-Recommendation-System #

**Overview**
The YouTube Video Recommendation System is designed to help users discover new content based on their interests by clustering similar videos and providing personalized recommendations. This project involves data collection from YouTube, data preprocessing, machine learning for clustering, and a web application for user interaction.

**Skills Acquired**
  1. Data Collection and API Integration
  2. Data Cleaning and Preprocessing (ETL)
  3. Machine Learning
  4. Database Management
  5. Web Application Development using Streamlit
  6. Cloud Deployment
     
**Domain**
Social Media and Product Recommendations

**Problem Statement**
Develop a system that:
  1. Collects YouTube channel and video data.
  2. Groups videos based on metadata tags.
  3. Provides video recommendations through a Streamlit web application.
     
**Business Use Cases**
Content Discovery: Assist users in finding new content based on their interests by clustering similar videos.
Targeted Marketing: Offer insights for targeted advertisements based on video content clusters.
User Engagement: Enhance user engagement on platforms by recommending relevant videos.
Content Categorization: Aid content creators and curators in organizing and tagging their videos.

**Approach**
**Data Collection**
    1. Use YouTube Data API to gather channel and video data, including tags, descriptions, and metadata.
    2. Store raw data in AWS S3 as JSON files.
**Data Cleaning and Structuring**
    1. Clean and preprocess data, addressing issues such as duplicates and missing values.
    Store cleaned data in AWS RDS for structured querying.

**Model Training**

Cluster videos based on tags and other features using clustering algorithms (e.g., K-Means, hierarchical clustering).
Evaluate clustering quality and fine-tune the model.
Web Application Development

Develop a Streamlit application for video search and recommendations.
Deploy the application on an AWS instance for real-time interaction.

**Results**
A functioning Streamlit web application providing personalized video recommendations based on user input.
Clusters of videos to help users find related content easily.

**Technical Tags**
1. YouTube Data API
2. AWS S3
3. AWS RDS
4. EC2
5. Streamlit
6. Clustering
7. Machine Learning
8. Python
9. Data Cleaning
10. Web Development

**Data Set**
Source: YouTube Data API
Format: JSON
Variables: Channel information, video metadata, tags, descriptions, views, likes, etc.

**Acknowledgements**
YouTube Data API for providing the video and channel data.
AWS for cloud storage and database services.
Streamlit for the web application framework.

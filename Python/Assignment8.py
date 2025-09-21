import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import re

# Title and description
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research metadata from the CORD-19 dataset")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('metadata.csv', low_memory=False)
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    df['abstract'] = df['abstract'].fillna('')
    df['title'] = df['title'].fillna('')
    df['abstract_word_count'] = df['abstract'].apply(lambda x: len(x.split()))
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
year_range = st.sidebar.slider("Select publication year range", 2019, 2022, (2020, 2021))
selected_journals = st.sidebar.multiselect("Select journals", options=df['journal'].dropna().unique(), default=[])

# Apply filters
filtered_df = df[df['year'].between(year_range[0], year_range[1])]
if selected_journals:
    filtered_df = filtered_df[filtered_df['journal'].isin(selected_journals)]

# Show sample data
st.subheader("Sample of Filtered Data")
st.write(filtered_df[['title', 'journal', 'publish_time', 'abstract_word_count']].head())

# Publications by year
st.subheader("Publications Over Time")
year_counts = filtered_df['year'].value_counts().sort_index()
fig1, ax1 = plt.subplots()
ax1.bar(year_counts.index, year_counts.values, color='skyblue')
ax1.set_xlabel("Year")
ax1.set_ylabel("Number of Publications")
ax1.set_title("Publications by Year")
st.pyplot(fig1)


st.subheader("Top Publishing Journals")
top_journals = filtered_df['journal'].value_counts().head(10)
fig2, ax2 = plt.subplots()
ax2.barh(top_journals.index[::-1], top_journals.values[::-1], color='lightgreen')
ax2.set_xlabel("Number of Papers")
ax2.set_title("Top Journals")
st.pyplot(fig2)

# Word cloud of titles
st.subheader("Word Cloud of Paper Titles")
title_words = ' '.join(filtered_df['title'].dropna()).lower()
word_list = re.findall(r'\b\w+\b', title_words)
word_freq = Counter(word_list)
wc = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
fig3, ax3 = plt.subplots()
ax3.imshow(wc, interpolation='bilinear')
ax3.axis('off')
st.pyplot(fig3)

# Distribution by source
st.subheader("Distribution of Papers by Source")
source_counts = filtered_df['source_x'].value_counts().head(10)
fig4, ax4 = plt.subplots()
ax4.pie(source_counts.values, labels=source_counts.index, autopct='%1.1f%%', startangle=140)
ax4.set_title("Top Sources")
st.pyplot(fig4)

# Footer
st.markdown("---")
st.markdown("✅ **Tips:** Use the sidebar to filter by year and journal. Explore trends, top publishers, and title patterns.")
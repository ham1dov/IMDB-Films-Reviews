IMDb Movie Reviews Preprocessing
This project preprocesses the IMDb Dataset of 50K Movie Reviews for sentiment analysis tasks. It cleans the review text by removing HTML tags, punctuation, and stop words, and normalizes whitespace to prepare the data for machine learning or natural language processing (NLP) applications.

Features
Data Source: Processes the IMDb 50K movie reviews dataset (CSV format) from Kaggle or Stanford's Large Movie Review Dataset.

Text Cleaning:
Removes HTML tags using BeautifulSoup.
Eliminates punctuation with str.translate().
Normalizes multiple whitespaces (spaces, tabs, newlines) to a single space using re.
Filters out stop words using nltk to reduce noise and dimensionality.

Performance Tracking: Measures execution time for the preprocessing pipeline.

Output: Generates a cleaned DataFrame with preprocessed reviews, ready for further analysis or modeling.

Technologies Used
Python Libraries: pandas, BeautifulSoup4, nltk, re, string, time.

Environment: Developed and tested in PyCharm with Git for version control.

Usage
Install Dependencies:
pip install pandas beautifulsoup4 nltk

Download Dataset:

Obtain IMDB_Dataset.csv from Kaggle or Stanford's Large Movie Review Dataset.
Place the CSV file in the project directory or update the file path in the script.

Run the Script:
Execute imdb_clean.py to preprocess the reviews.
The script outputs the first 20 cleaned reviews and the execution time.



Output: The cleaned reviews are stored in the review column of the DataFrame, which can be saved as a CSV or Parquet file for reus

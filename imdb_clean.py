import re
import string
import bs4
import pandas as pd
import nltk
from nltk.corpus import stopwords
nltk.download("stopwords")
import time

def clean_text(text):
    # Remove all HTML tags from the text
    text = bs4.BeautifulSoup(text, 'html.parser')  # Parse HTML to extract plain text
    text = text.get_text()  # Extract plain text from the parsed HTML

    # Remove all punctuation from the plain text
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Replace all tabs and whitespace with a single space
    text = re.sub(r'\s+', ' ', text).strip()

    # Remove stop words, which create noise and increase data dimensionality
    stop_words = set(stopwords.words('english'))
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

# Create a DataFrame from the IMDb film reviews CSV file
df = pd.read_csv('IMDB_Dataset.csv', header=0)

# Apply the cleaning function to all rows in the 'review' column
start_time = time.time()
df['review'] = df['review'].apply(clean_text)
end_time = time.time()
print(f'Execution time: {end_time - start_time} seconds')  # Calculate the execution time for applying the function to all rows
print(df['review'].head(20))  # Display the first 20 rows of the cleaned reviews

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import string
import nltk
from mlxtend.frequent_patterns import apriori, association_rules

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Define the documents
num_docs = int(input("Enter the number of documents: "))
docs = []
for i in range(num_docs):
    docs.append(input(f"Enter document {i+1}: "))

# Preprocess the documents
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]
    return tokens

docs_preprocessed = [preprocess(doc) for doc in docs]

# Define the query
query = input("Enter the query: ")

# Preprocess the query
query_preprocessed = preprocess(query)

# Use TF-IDF to vectorize the documents and query
vectorizer = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False)
docs_tfidf = vectorizer.fit_transform(docs_preprocessed)
query_tfidf = vectorizer.transform([query_preprocessed])

# Calculate cosine similarities between query and documents
cosine_similarities = cosine_similarity(query_tfidf, docs_tfidf).flatten()

# Rank the documents according to relevance to query
ranking = np.argsort(cosine_similarities)[::-1]

# Print the documents in ranked order of relevance to query
print("Documents ranked by relevance to query:")
for rank, doc_idx in enumerate(ranking):
    print(f"{rank+1}. Document {doc_idx+1} (cosine similarity: {cosine_similarities[doc_idx]:.2f}):")
    print(docs[doc_idx])
    print()

# Convert preprocessed documents into a binary pandas DataFrame
unique_tokens = list(set([token for doc in docs_preprocessed for token in doc]))
docs_binary = np.zeros((len(docs_preprocessed), len(unique_tokens)))
for i, doc in enumerate(docs_preprocessed):
    for j, token in enumerate(unique_tokens):
        if token in doc:
            docs_binary[i,j] = 1
docs_df = pd.DataFrame(docs_binary, columns=unique_tokens)

# Apply association clustering to determine correlation factors
frequent_itemsets = apriori(docs_df, min_support=0.1, use_colnames=True)
print("Frequent itemsets:")
print(frequent_itemsets)
 
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print("Association rules:")
print(rules)

# Extract antecedents and consequents from association rules
antecedents = list(rules.antecedents)
consequents = list(rules.consequents)

# Define a function to expand the query using association rules
def expand_query(query, antecedents, consequents):
    expanded_query = query.copy()
    for word in query:
        for idx, antecedent in enumerate(antecedents):
            if word in antecedent:
                expanded_query.extend(list(consequents[idx]))
    expanded_query = list(set(expanded_query))
    return expanded_query

# Expand the query using association rules
expanded_query = expand_query(query_preprocessed, antecedents, consequents)

# Print the expanded query
print("Expanded query:")
print(expanded_query)


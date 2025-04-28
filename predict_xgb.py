import pickle
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer

# load saved model
xgboost_model = pickle.load(open('xgboost_model.pkl'))

# masukkan tf-idf
tfidf_title = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
tfidf_title.fit(df['title_processed'])
tfidf_title_filename = 'tfidf_title.pkl'
with open(tfidf_title_filename, 'wb') as file:
    pickle.dump(tfidf_title, file)



# judul halaman
st.title ('News Prediction')

clean_text = st.text_input('Input Title')

xgb_detection = ' '

if st.button('Result'):
  predict.xgb = xgb_model.predict(loaded_vec.fit_transform([clean_text]))

  if (predict_xgb == 0):
    xgb_detection = 'REAL NEWS'
  else (predict_xgb == 1):
    xgb_detection = 'FAKE NEWS'


st.success(xgb_detection)
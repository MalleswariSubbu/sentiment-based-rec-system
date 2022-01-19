import pandas as pd
import pickle



def filter_top_five_best(user_input):
    item_final_rating = pd.read_pickle("pickles/item_based_reco_engine.pkl")
    df = pd.read_csv("pickles/df.csv")
    word_vectorizer = pickle.load(
        open('pickles/tfidf.pkl', 'rb'))
    classifier_sm = pickle.load(
        open('pickles/rf_model.pkl', 'rb'))
    d = item_final_rating.loc[user_input].sort_values(ascending=False)[0:20]

    # Based on positive sentiment percentage.
    i= 0
    list1 = {}
    for prod_name in d.index.tolist():
      product_name = prod_name
      product_name_review_list =df[df['prod_name']== product_name]['Review'].tolist()
      features= word_vectorizer.transform(product_name_review_list)
      classifier_sm.predict(features)
      list1[product_name] = classifier_sm.predict(features).mean()*100
      
    list2= pd.Series(list1).sort_values(ascending = False).head(5).index.tolist()
    return list2
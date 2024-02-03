from flask import Flask, jsonify, request
import pandas as pd

articles_data = pd.read_csv('articles.csv')
article_columns = articles_data[['url' , 'title' , 'text' , 'lang' , 'total_events']]
liked_articles = []
unliked_articles = []

app = Flask(__name__)

def assign_val():
    m_data = {
        "url": article_columns.iloc[0,0],
        "title": article_columns.iloc[0,1],
        "text": article_columns.iloc[0,2] or "N/A",
        "lang": article_columns.iloc[0,3],
        "total_events": article_columns.iloc[0,4]/2
    }
    return m_data

# API to display first article
@app.route("/get-article")
def get_article():

    article_info = assign_val()
    return jsonify({
        "data": article_info,
        "status": "success"
    })

# API to move the article into liked articles list
@app.route("/liked-article")
def liked_article():
    global article_columns
    article_info = assign_val()
    liked_articles.append(article_info)
    article_columns.drop([0], inplace=True)
    article_columns = article_columns.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

# # API to move the article into not liked articles list
@app.route("/unliked-article")
def unliked_article():
    global article_columns
    article_info = assign_val()
    unliked_articles.append(article_info)
    article_columns.drop([0], inplace=True)
    article_columns = article_columns.reset_index(drop=True)
    return jsonify({
        "status": "success"
    })

# run the application
if __name__ == "__main__":
    app.run()

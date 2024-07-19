from flask import Flask, render_template
import pandas as pd
from analytic import main as analytics_main
from search import main as search_main
from twitter import main as twitter_main

app = Flask(__name__)

@app.route('/')
def home():
    try:
        analytics_data = analytics_main()
        search_data = search_main()
        twitter_data = twitter_main()

        analytics_df = pd.DataFrame(analytics_data)
        search_df = pd.DataFrame(search_data)
        twitter_df = pd.DataFrame(twitter_data)

        return render_template('index.html', 
                               analytics_tables=[analytics_df.to_html(classes='data')], analytics_titles=analytics_df.columns.values,
                               search_tables=[search_df.to_html(classes='data')], search_titles=search_df.columns.values,
                               twitter_tables=[twitter_df.to_html(classes='data')], twitter_titles=twitter_df.columns.values)
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return "An error occurred. Please try again later.", 500

if __name__ == '__main__':
    app.run(debug=True)
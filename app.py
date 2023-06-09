from flask import Flask, render_template, request, redirect
from violin import *


app = Flask(__name__)

# Post JSON for violin
@app.route('/get-json-violin', methods=['GET', 'POST'])
def get_json_violin():
    # Create dataframe
    df_grpby = build_dataset(ORDERS_PATH)
    # Create json
    json_to = json_violin(df_grpby)
    return json_to
# Routing do define url
@app.route('/')
def violin():
    return render_template('violin-plot.html')


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(debug=True, port=5000)




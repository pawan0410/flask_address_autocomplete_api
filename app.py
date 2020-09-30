from flask import Flask, render_template, request, jsonify, make_response
import json
import re

app = Flask(__name__)

@app.route('/')
def index():
    """Render the input search field"""
    return render_template('index.html')


@app.route('/search')
def search():
    """Match the input string by user with the addresses in addresses.json file
        and return matching suggestions in the form of a list i.e suggested_addr"""
    q = request.args.get('q').strip()

    with open('static/addresses.json', 'r') as f:
        data = json.loads(f.read())
        suggested_addr = []
        for d in data:
            for keys,vals in d.items():
                if q in vals:
                    suggested_addr.append(d)
                    break

        resp = make_response(jsonify(suggested_addr[:10]))
        resp.headers['Access-Control-Allow-Origin'] = "*"
        return resp


if __name__ == '__main__':
    app.run(debug=True)




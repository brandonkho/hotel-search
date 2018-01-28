from flask import Flask, jsonify
import scraper
app = Flask(__name__)


#search endpoint
@app.route('/hotels/search/',methods=['GET'])
def search_hotel():
    response = scraper.search()
    return jsonify(results=response)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8000)
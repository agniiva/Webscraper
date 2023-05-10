import requests
from bs4 import BeautifulSoup

def scrape_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    text = soup.get_text()
    return text

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def api_scrape():
    url = request.args.get('url', default=None, type=str)
    if url:
        text = scrape_text(url)
        return jsonify({'text': text})
    else:
        return jsonify({'error': 'URL parameter is missing'})

if __name__ == '__main__':
    app.run(debug=True)
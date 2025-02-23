from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    url = request.form.get('url')
    if not url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract video URL
        video_element = soup.find('video')
        if video_element:
            video_url = video_element['src']
            return jsonify({'video_url': video_url})

        # Extract image URL
        image_element = soup.find('img')
        if image_element:
            image_url = image_element['src']
            return jsonify({'image_url': image_url})

        return jsonify({'error': 'Media not found'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

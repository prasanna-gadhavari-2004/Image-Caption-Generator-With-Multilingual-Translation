
from flask import Flask, render_template, request
from caption import generate_caption
from translation import translate_caption

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    image = request.files['image']
    image_path = 'static/images/' + image.filename
    image.save(image_path)

    language = request.form.get('language')
    caption = generate_caption(image_path)
    translated_caption = translate_caption(caption, target_language=language)

    return render_template('result.html', caption=caption, translated_caption=translated_caption, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # il file statico si chiama 'foto_gruppo.jpg' nella cartella static/
    foto_url = url_for('static', filename='foto_gruppo.jpg')
    return render_template('index.html', foto_url=foto_url)

if __name__ == '__main__':
    # per sviluppo: http://127.0.0.1:5000
    app.run(host='0.0.0.0', port=5000, debug=True)

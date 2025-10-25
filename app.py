from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    # Lista di tutte le immagini nella cartella static
    foto_lista = ["foto1.jpg", "foto2.jpg", "foto3.jpg"]  # metti qui i nomi dei file reali
    # Genera gli URL completi per il template
    foto_url = [url_for('static', filename=foto) for foto in foto_lista]
    return render_template('index.html', foto_url=foto_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

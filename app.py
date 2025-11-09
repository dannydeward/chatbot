from flask import Flask, render_template, jsonify, request
from chatbo import  chatbot_respuesta



app = Flask(__name__)
app.secret_key = "supersecreto"  # sigue siendo buena práctica mantener una clave




# Página principal
@app.route('/')
def home():
    return render_template('index.html')

# Página "About"
@app.route('/about')
def about():
    return render_template('about.html')

# Página "Properties"
@app.route('/properties')
def properties():
    return render_template('properties.html')

# Página "Contact"
@app.route('/contact')
def contact():
    return render_template('contact.html')


    # Página "Services"
@app.route('/services')
def services():
    return render_template('services.html')



    # Página "Services"
@app.route('/agents')
def agents():
    return render_template('agents.html')


    # Página "Services"
@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje")
    user_id = request.remote_addr  # usamos la IP como identificador básico
    respuesta = chatbot_respuesta(user_id, mensaje)
    return jsonify({"respuesta": respuesta})

if __name__ == '__main__':
    app.run(debug=True)

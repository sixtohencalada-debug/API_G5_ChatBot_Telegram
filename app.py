from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat(): 

    data = request.get_json()
    user_message = data.get('message', '')
    # Aquí puedes agregar la lógica para procesar el mensaje del usuario y generar una respuesta
    response_message = f"Recibí tu mensaje: {user_message}"
    return jsonify({'response': response_message})  



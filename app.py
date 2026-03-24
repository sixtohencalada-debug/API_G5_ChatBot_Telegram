from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/chat', methods=['POST'])
def chat(): 

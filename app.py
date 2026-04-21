from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Esta parte responde à verificação obrigatória da Meta
        verify_token = "albuquerque_secreto_123" # Senha de verificação
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        
        if mode and token:
            if mode == 'subscribe' and token == verify_token:
                return str(challenge), 200
            else:
                return 'Falha na verificação', 403
        return 'Servidor do Albuquerque Assistente Operante!', 200

    elif request.method == 'POST':
        # Aqui é onde as mensagens vão chegar depois
        dados = request.json
        print("Nova interação recebida:", dados)
        return jsonify({"status": "recebido"}), 200

if __name__ == '__main__':
    app.run(port=5000)

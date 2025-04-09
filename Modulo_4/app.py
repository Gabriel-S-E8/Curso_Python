from sqlalchemy.exc import IntegrityError
from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import (
    LoginManager,
    login_required,
    login_user,
    current_user,
    logout_user,
)
import os

# Get the absolute path to the directory where app.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Set the instance folder to be in the same directory as app.py
INSTANCE_PATH = os.path.join(BASE_DIR, "instance")

# Create the Flask app with the explicit instance_path
app = Flask(__name__, instance_path=INSTANCE_PATH)
app.config["SECRET_KEY"] = "your_secret_key"

# Construct the path to the database.db file inside the instance/ folder
app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"sqlite:///{os.path.join(INSTANCE_PATH, 'database.db')}"
)
print(f"Database path: {app.config['SQLALCHEMY_DATABASE_URI']}")

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = "login"

# # Create the instance folder if it doesn't exist
# if not os.path.exists(INSTANCE_PATH):
#     os.makedirs(INSTANCE_PATH)

# with app.app_context():
#     db.create_all()
#     # Optionally, add a user if it doesn't exist
#     if not User.query.filter_by(username="admin").first():
#         new_user = User(username="admin", password="123")
#         db.session.add(new_user)
#         db.session.commit()
#         print("User 'admin' created successfully!")


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso!"})
        else:
            return jsonify({"message": "Credenciais inválidas"}), 400

    return jsonify({"message": "Credenciais inválidas"}), 400


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso!"})


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        # Verifica se o username já existe
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return (
                jsonify({"message": "O username já está em uso. Escolha outro."}),
                400,
            )

        # Se não existe, cria o novo usuário
        user = User(username=username, password=password)
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify({"message": "Usuário cadastrado com sucesso"})
        except IntegrityError:
            db.session.rollback()  # Reverte a sessão em caso de erro
            return (
                jsonify({"message": "Erro ao criar usuário. O username já existe."}),
                400,
            )

    return jsonify({"message": "Dados inválidos"}), 400


@app.route("/user/<int:id_user>", methods=["GET"])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)

    if user:
        return {"username": user.username}

    return jsonify({"message": "Usuario não encontrado"}), 404


@app.route("/user/<int:id_user>", methods=["PUT"])
@login_required
def update_user(id_user):
    data = request.json
    user = User.query.get(id_user)

    if not user:
        return jsonify({"error": "Usuário não encontrado"}), 404

    updates = {
        "password": data.get("password"),
        "username": data.get("username")
    }

    messages = []
    for field, value in updates.items():
        if value:
            setattr(user, field, value)
            messages.append(f"✅ {field.capitalize()} do usuário {id_user} atualizado com sucesso")

    if messages:
        db.session.commit()
        return jsonify({
            "status": "success",
            "updates": messages
        })
    
    return jsonify({
        "status": "error",
        "message": "Nenhum dado válido fornecido para atualização"
    }), 400


@app.route("/user/<int:id_user>", methods=["DELETE"])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if user:
        return jsonify({"message": f"Usuário {id_user} deletado com sucesso"})

    return jsonify({"message": "Usuario não encontrado"}), 404


@app.route("/hello-world", methods=["GET"])
def hello_world():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)

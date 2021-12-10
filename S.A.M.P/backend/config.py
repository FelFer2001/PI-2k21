from datetime import timezone
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request, flash, redirect
from flask_cors import CORS
import os
UPLOAD_FOLDER = './img/perfil/'
app = Flask(__name__)
CORS(app)
caminho = os.path.dirname(os.path.abspath(__file__))
arquivobd = os.path.join(caminho, "pessoa.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + arquivobd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'testesdeupload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
db = SQLAlchemy(app)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)

if __name__ == '__main__':
    db_path = os.path.abspath('database.db')
    print("DB Path:", db_path)

    with app.app_context():
        db.drop_all()  # <--- DROP ALL TABLES
        print("✔ Dropped all tables")
        db.create_all()
        print("All models:", db.metadata.tables.keys())
        print("✔ Tables created")

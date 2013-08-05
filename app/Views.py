__author__ = 'inqui'
from app import app, db
from flask import jsonify, request
from Models import User


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/v1/users', methods=['POST'])
def add_user():
    user = User(name=request.json['name'],
                email=request.json['email'],
                phone=request.json['phone'],
                thumbnail_url=request.json['thumbnail_url'],
                reg_id=request.json['reg_id'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'user': user.serialize})

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    return jsonify(users=[u.serialize for u in User.query.all()])
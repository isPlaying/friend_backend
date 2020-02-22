from flask import Blueprint
from flask import request
from dao import db

friend = Blueprint('friend', __name__)


@friend.route('', methods=['GET'])
def get_friend():
    name = request.args.get('name')
    if name is not None:
        return db.get_friend(name)
    else:
        return db.get_friend_list()


@friend.route('', methods=['POST'])
def post_friend():
    params = request.get_json()
    return db.post_friend(params)


@friend.route('/<int:friend_id>', methods=['PUT'])
def put_friend(friend_id):
    params = request.get_json()
    return db.put_friend(friend_id, params)


@friend.route('/<int:friend_id>', methods=['DELETE'])
def delete_friend(friend_id):
    friend_id = friend_id
    return db.del_friend(friend_id)

from flask_restful import Resource, reqparse

from models.user import UserModel


class UserRegistry(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True)
    parser.add_argument('password', type=str, required=True)

    def post(self):
        data = UserRegistry.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User with that username already exists'}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created sucessfully"}, 201

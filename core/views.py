from framework.request import Request
from framework.status import status_200
from framework.views import BaseView, Response, ListApiView
from framework import status
from Database.tables import User


class HelloView(BaseView):

    def get(self, request) -> Response:
        hello = request.query_params.get('hello', None)

        if hello == '1':
            data = {
                "message": "Salom hammaga 1"
            }
        elif hello == '2':
            data = {
                "message": "Salom hammaga 2"
            }
        else:
            data = {
                "message": "Salom hammaga"
            }

        return Response(data=data, status=status.status_200)

class DataView(BaseView):

    def get(self, request) -> Response:
        user_id = request.query_params.get('user', None)
        if user_id is not None:
            user = User.get_user_by_id(user_id)
            if user:
                data = {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "created_at": str(user.created_at)
                }

                return Response(data=data, status=status.status_200)

            else:
                data = {
                    "msg": "User not found"
                }

                return Response(data=data, status=status.status_404)
        else:
            users = User.get_users()
            if users:
                response_data = {}
                count = len(users)
                response_data.update(
                    {
                        'count': count
                    }
                )
                users_data = []
                for user in users:
                    data = {
                        "id": user.id,
                        "username": user.username,
                        "email": user.email,
                        "created_at": str(user.created_at)
                    }

                    users_data.append(data)

                response_data.update(
                    {
                        "users_data": users_data
                    }
                )

                return Response(data=response_data, status=status_200)
            else:
                data = {
                    "msg": "User not found"
                }

                return Response(data=data, status=status.status_404)

class UsersListView(ListApiView):
    queryset = User.get_users()
    fields = ['id', 'email', 'username', 'created_at']


class CreateUserView(BaseView):
    def post(self, request: Request) -> Response:
        data = request.body
        username = data.get('username', None)
        email = data.get("email", None)
        password = data.get("password", None)

        if username is None:
            return Response(data={
                "msg": "username bo'sh bo'lishi mumkin emas"
            },
                status=status.status_400
            )

        if email is None:
            return Response(data={
                "msg": "email bo'sh bo'lishi mumkin emas"
            },
                status=status.status_400
            )

        new_user = User.create_user(username=username, password=password, email=email)

        if new_user:
            return Response(
                data={
                    "msg": "user muvafaqiyatli yaratildi"
                },
                status=status.status_201
            )

        else:
            return Response(
                data={
                    "msg": "Nimadir xato ketti"
                },
                status=status.status_400
            )



from framework.routes import Router
from .views import DataView, HelloView, UsersListView, CreateUserView

Router.add_route('/hello/', HelloView.as_view())
Router.add_route('/users/', DataView.as_view())
Router.add_route('/users-list/', UsersListView.as_view())
Router.add_route('/users/create/', CreateUserView.as_view())

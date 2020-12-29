from flask import Flask
from flask_restful import Api

# Import the class in todo.py with get/put endpoints
# from resources.todo import todo
from resources import todo
Todo = todo.Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, "/todo/<int:id>")

if __name__ == '__main__':
    app.run()
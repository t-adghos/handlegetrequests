import pyodbc,decimal
from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)


@app.route('/<string:task_id>', methods=['GET'])
def get_task(task_id):
    print task_id


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Incorrect query'}), 404)





if __name__ == '__main__':
    app.run(debug = True)

import pyodbc,decimal
from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)


@app.route('/todo/api/v1.0/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    try:
        server = "t-adghos.database.windows.net"
        database = "PWA"
        username = "aditya"
        password = "Coco808802"
        driver = '{ODBC Driver 13 for SQL Server}'
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        cursor.execute(task_id)
        columns = [column[0] for column in cursor.description]
        results = cursor.fetchall()
        key = []
        for item in columns:
            key.append(str(item))
        ls = []
        for row in results:
            dict = {}
            for a,b in zip(row,columns):
                if isinstance(a,unicode):
                    dict[str(b)] = str(a)
                elif isinstance(a,decimal.Decimal):
                    dict[str(b)] = round(a,10)
                else:
                    dict[str(b)] = a
            ls.append(dict)
        return jsonify(ls)
    except:
        abort(404)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Incorrect query'}), 404)





if __name__ == '__main__':
    app.run(debug = True)

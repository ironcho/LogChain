from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)

rulelist = [
    {
        'id': 1,
        'title': u'Buy',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/rulelist/', methods=['GET'])
def get_rules():
    return jsonify({'rulelist': rulelist})


@app.route('/rules/', methods=['POST'])
def create_rule():
    if not request.json or not 'title' in request.json:
        abort(400)
    rule = {
        'id': rulelist[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    rulelist.append(rule)
    return jsonify({'rule': task}), 201


@app.route("/")
def hello():
    return "LogChain's REST API node!"


if __name__ == "__main__":
    app.run()

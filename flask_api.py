from flask import Flask, jsonify, request
app = Flask(__name__)

languages = [{"name": "Python"}, {"name": "JavaScript"}, {"name": "Java"}]


@app.route("/", methods=['GET'])
def test():
    return jsonify({"message": "Test"})


@app.route("/lang", methods=['GET'])
def returnAll():
    return jsonify({"languages": languages})


@app.route("/lang/<string:name>", methods=['GET'])
def returnOne(name):
    try:
        langs = [language for language in languages if language["name"] == name]
        return jsonify({"language": langs[0]})
    except:
        return jsonify({"language": "Invalid Request"})


@app.route("/lang", methods=["POST"])
def addOne():
    try:
        language = {"name": request.json['name']}
        if languages.__contains__(language) and request.json['opt'] != "rem":
            return jsonify({'languages': languages}, {"succsess": "False", "info": "aready exists"})

        if request.json['opt'] == "add":
            languages.append(language)
            return jsonify({'languages': languages}, {"succsess": "True", "info": ""})

        elif request.json['opt'] == "rem":
            languages.remove(language)
            return jsonify({'languages': languages}, {"succsess": "True", "info": ""})

        else:
            return jsonify({'languages': languages}, {"succsess": "False", "info": "Invalid arguments"})
    except:
        return jsonify({'languages': languages}, {"succsess": "False", "info": "Invalid arguments"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)

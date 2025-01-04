from flask import Flask, request, jsonify

from aggregate.aggreate_function import generate_feature

app = Flask(__name__.split('.')[0])

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 * num2
    return jsonify({'result': result})

@app.route('/classify', methods=['POST'])
def invoke_aggregate():
    data = request.get_json()
    file_dir = data['file']
    result = generate_feature(file_dir)
    return jsonify({'result': int(result)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
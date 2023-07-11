from flask import Flask, jsonify,render_template
import json

app = Flask(__name__)

# Load the data from orders.json
with open('orders.json', 'r') as file:
    orders_data = json.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello', methods=['GET'])
def hello():
    return {'message': 'Hello, World!'}

@app.route('/api/entire')
def fulldisplay():
    return jsonify(orders_data)

@app.route('/api/<int:order_id>', methods=['GET'])
def displayOrderID(order_id):
    order = None
    for item in orders_data:
        if item.get('orderID') == order_id:
            order = item
            break
    if order:
        return jsonify(order)
    else:
        return jsonify({'error': 'Order not found'})

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

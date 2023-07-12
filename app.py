from flask import Flask, jsonify,render_template,request
import json
import numpy as np
import pandas as pd
df=pd.read_csv('static/orders.csv')
ord_id=list(np.unique(df.orderID.values))

app=Flask(__name__)


@app.route('/', methods=['GET'])
def displayOrderID():
    res = None
    order_id = request.args.get('orderID')
    
    if order_id is not None:
        order_id = int(order_id)
        if order_id in ord_id:
            q = df[df['orderID'] == order_id]
            return q.to_json(orient='records')
        else:
            res = "Order ID not found."
    else:
        res = "Order ID parameter not provided."
    
    return res

if __name__ in '__main__':
    app.run(debug=True)

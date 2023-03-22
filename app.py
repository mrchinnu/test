from flask import Flask, jsonify,render_template,request
import pickle
import numpy as np

model=pickle.load(open('model.pkl','rb'))
print("model is loaded")
app=Flask(__name__)
@app.route('/',methods=['GET'])
def index():
    m1=int(request.args['m1'])
    m2=int(request.args['m2'])
    m3=int(request.args['m3'])
    m4=int(request.args['m4'])
    m5=int(request.args['m5'])
    m6=int(request.args['m6'])
    m7=int(request.args['m7'])
    m8=int(request.args['m8'])
    m9=int(request.args['m9'])
    m0=int(request.args['m0'])
    pred = model.predict(np.array([m1,m2,m3,m4,m5,m6,m7,m8,m9,m0]).reshape(1,10))
    if 30>m1>1 and 30>m2>1 and 30>m3>1 and 30>m4>1 and 30>m5>1 and 30>m6>1 and 30>m7>1 and 30>m8>1  and 30>m9>1 and 30>m0>1:
        return jsonify(str(pred))
    else:
        return "enter valid values"
if __name__ == "__main__":
    app.run(debug=True)
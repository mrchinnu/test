from flask import Flask,render_template,request
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
    print(m1,m2,m3,m4,m5,m6)
    pred = model.predict(np.array([m1,m2,m3,m4,m5,m6]).reshape(1,6))
    return jsonify(predection=str(pred))
if __name__ == "__main__":
    app.run(debug=True)
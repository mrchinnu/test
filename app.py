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
    m11=int(request.args['m11'])
    m12=int(request.args['m12'])
    m13=int(request.args['m13'])
    m14=int(request.args['m14'])
    m15=int(request.args['m15'])
    m16=int(request.args['m16'])
    m17=int(request.args['m17'])
    m18=int(request.args['m18'])
    m19=int(request.args['m19'])
    m20=int(request.args['m20'])
    m21=int(request.args['m21'])
    m22=int(request.args['m22'])
    m23=int(request.args['m23'])
    m24=int(request.args['m24'])
    m25=int(request.args['m25'])
    m26=int(request.args['m26'])
    m27=int(request.args['m27'])
    m28=int(request.args['m28'])
    m29=int(request.args['m29'])
    m30=int(request.args['m30'])
    m31=int(request.args['m31'])
    m32=int(request.args['m32'])
    pred = model.predict(np.array([m1,m2,m3,m4,m5,m6,m7,m8,m9,m0,m11,m12,m13,m14,m15,m16,m17,m18,m19,m20,m21,m22,m23,m24,m25,m26,m27,m28,m29,m30,m31,m32]).reshape(1,32))
    pred=np.round(pred);
    if pred>=0 and pred<=3:
        return jsonify("GRADE F:FAIL")
    elif pred>=4 and pred<=7:
        return jsonify("GRADE D:")
    elif pred>=7 and pred<=11:
        return jsonify("GRADE C:AVERAGE")
    elif pred>=12 and pred<=16:
        return jsonify("GRADE B:GOOD")
    elif pred>=17 and pred<=20:
        return jsonify("GRADE A:EXCELLENT")
    else:
        return jsonify("WRONG INPUT")
if __name__ == "__main__":
    app.run(debug=True)
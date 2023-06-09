from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route("/sum",methods=['POST'])
def sum():
    try:
        data=request.get_json()
        if "number1" not in data or "number2" not in data :
            raise ValueError("Debe traer 2 datos")
        
        number1=data["number1"]
        number2=data["number2"]
        if not isinstance(number1,(int,float)) or not isinstance(number2,(int,float)) :
            raise TypeError("los datos deben ser numeros")
        return jsonify ({"result":number1+number2})
    except ValueError as ve:
        return jsonify({"error":str(ve)}),400
    except TypeError as te:
        return jsonify({"error":str(te)}),400
    except Exception as e:
        return jsonify({"error":str(e)}),500
   
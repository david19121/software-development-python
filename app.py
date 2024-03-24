from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "welcome to my page"


@app.route("/me")
def come():
    return "welcome back"



@app.route("/details")
def details():
    a="david oguma"
    return "my name is: " + a



@app.route("/skull")
def skull():
    a=10
    b=20
    z=a+b
    return "my result was: " + str(z) 



@app.route("/aboutus")
def aboutus():
    email="davogums@gmail.com"
    phone="07062800092"
    return "our company details are: " + email + "," + phone



@app.route("/result")
def result():
    q=40
    o=45
    t=q+o
    w=t*50
    return str(w)


@app.route(“/success”)

def getcandidate():
    return jsonify(
    {
        "id": 1,
        "name": “ayeni”,
        "type": “devops Engr”
    },
    {
        "id": 2,
        "name": “bisi komolafe,
        "type": “”infrastructure
    },
    {
        "id": 3,
        "name": “ojo” Taiwo,
        "type": “aws Architect
    },
    {
        "id": 4,
        "name": “clement “philips,
        "type": “system Engr”
    },


    

    














if __name__=='__main__':
    app.run(host="127.0.0.1") 
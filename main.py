from flask import Flask, request
#from caesar import rotate_string
import caesar
import cgi
app = Flask(__name__)
app.config['DEBUG'] = True
 
form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rotate" method="post">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0" /><br>
                <input type="text" name"textarea"/><br>
            </label>
            <input type="submit" value="encrypt"/>
        </form>
    </body>
</html>
"""




@app.route("/")
def index():
    return form 

@app.route("/rotate", methods=['POST'])
def rotate():
    rotate= request.form['rot']
    return cgi.escape(rotate)

@app.route("/encrypt", methods=['POST'])
def encrypt():
    textarea = request.form['textarea']
    text = textarea
    rot = int(self.request.get['rotate_by'])
    rotate(text, rot)
    rotate_string(text, rot)
    self.response.write['encrypted']
    return rotate_string()
 
app.run()

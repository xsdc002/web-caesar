from flask import Flask, request
from caesar import rotate_string

import cgi
app = Flask(__name__)
app.config['DEBUG'] = True
 
form="""
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST">
            <label>
                Rotate by:
                <input type="text" name="rot" value="0" /><br>
                <textarea name="textarea">{0}</textarea><br>
            </label>
            <input type="submit" value="Submit Query"/>
        </form>
    </body>
</html>
"""




@app.route("/")
def index():
    return form.format("") 

#@app.route("/rotate", methods=['POST'])
#def rotate():
#    rotate= request.form['rot']
#    return cgi.escape(rotate)



@app.route("/", methods=['POST'])
def encrypt():
    textarea = request.form['textarea']
    rot = request.form['rot']
    rot = int(rot)
    #rot = int(self.request.get['rotate_by'])
    #text = textarea
    #rotate(text, rot)
    #rotate_string(textarea, rot)
    #self.response.write['encrypted']
    return form.format(rotate_string(textarea, rot))
 
app.run()

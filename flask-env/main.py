from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config["DEBBUG"] = True

empty=""

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background=color: #eee;
                padding 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label>Rotate by:
                    <input type="text" name="rot" value="0" />
                </label>
            </div>    
            <textarea type="text" name="text">
                {0}
            </textarea>
            <br>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""




@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    rot = int(rot)
    text = request.form["text"]
    encrypted = rotate_string(text, rot)
    content = form.format(encrypted)
    
    return content

@app.route("/")
def index():
    return form.format(empty)

app.run()
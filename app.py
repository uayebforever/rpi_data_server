import json
import subprocess

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route("/data")
def data():
    data = [(1, 2),
            (2, 2.5),
            (3, 2)]
    output = []
    for point in data:
        output.append({"x": point[0], "y": point[1]})
    return json.dumps(output)


@app.route("/temp")
def temp():
    data = str(subprocess.check_output(["tail", "-n1", "../temp_data.csv"]))
    timestamp, greenhouse_temp, porch_temp = data.split(",")[:3]

    return json.dumps(
        {"greenhouse": greenhouse_temp,
         "porch": porch_temp})


if __name__ == '__main__':
    app.run()

from os import environ, remove
from uuid import uuid4
from flask import *

from os_scheduler_visualizer import render


app = Flask(__name__)
app.secret_key = environ['FLASK_SECRET']

scheduler_log = 'scheduler_log'


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', name=scheduler_log)


@app.route('/visualize', methods=['POST'])
def visualize():
    log_file_name = uuid4().hex
    image_file_name = uuid4().hex + '.png'
    request.files[scheduler_log].save(log_file_name)
    render(log_file_name, image_file_name)
    remove(log_file_name)
    @after_this_request
    def remove_file(response):
        remove(image_file_name)
        return response
    return send_file(image_file_name)


if __name__ == '__main__':
    app.run()

# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template
from flask.globals import request

import jsonschema
from jsonschema import validate

# Read emoji from txt file to dict on start
# you need just copy and paste emoji from site https://emojipedia.org/nature/
# and paste in text file
#
# Not good solution but it's works

path_to_emoji_file = "emoji_lib.txt"

with open(path_to_emoji_file) as file:
    emoji_source = dict(x.lower().rstrip().split(None, 1) for x in file)

emoji = {v: k for k, v in emoji_source.items()}
set_with_keys = set(key.lower() for key in emoji)


app = Flask(__name__)

# CONST MESSAGES
CURL_404_ERROR_MESSAGE = '''Error 404 – Not Found.\n\nThe requested URL not found on this server. \n
Please try to run command in terminal as in example below:
curl -XPOST -d'{{"animal":"cow", "sound":"moooo", "count": 3}}' {host_url}'''

CURL_400_ERROR_MESSAGE = '''Error 400 - Bad Request.\n\n
Please try to run command in terminal as in example below:
curl -XPOST -d'{{"animal":"cow", "sound":"moooo", "count": 3}}' {host_url}'''

GREETING_MESSAGE = '''
  /\_/\  (
 ( ^.^ ) _)
   \"/  (
 ( | | )
(__d b__)
'''

# JSON schema for validating input data from POST request
# it's necessary because we can expect what incoming data may be not valid

animalsSchema = {
    "type": "object",
    "properties": {
        "animal": {"type": "string"},
        "sound": {"type": "string"},
        "count": {"type": "number"}
    },
    "required": ["animal", "sound", "count"]
}


def validate_json(json_data):
    try:
        validate(instance=json_data, schema=animalsSchema)
    except jsonschema.exceptions.ValidationError:
        return False
    return True


@app.route('/healthz', methods=['GET'])
def healthz():
    return "{\"status\": \"ok\"}"


@app.route("/", methods=['GET', 'POST'])
def index():
    app.logger.info("Host %s", request.host_url)
    app.logger.info("User-agent: %s", request.user_agent.string)
    if request.method == 'POST':
        request_data = request.get_json(force=True, silent=True)
        app.logger.info('index(): %s\n', request_data)

        is_valid = validate_json(request_data)
        if is_valid:
            app.logger.info("Given JSON data is Valid")
            return generate_response(request_data)
        else:
            app.logger.info("Given JSON data is InValid")
            return handle_bad_request("Given JSON data is InValid")
            # TODO Change str to err
    if "curl" in request.user_agent.string:
        return GREETING_MESSAGE + "\n"
    return render_template('main.html'), 200


@app.errorhandler(404)
def page_not_found(e):
    app.logger.info("Host %s", request.host_url)
    if "curl" in request.user_agent.string:
        error_message = e + "\n" + CURL_404_ERROR_MESSAGE.format(host_url=request.host_url)
        return error_message, 404
    else:
        return render_template('404.html'), 404


@app.errorhandler(400)
def handle_bad_request(e):
    app.logger.info("Host %s", request.host_url)
    if "curl" in request.user_agent.string:
        error_message = e + "\n" + CURL_400_ERROR_MESSAGE.format(host_url=request.host_url)
        return error_message, 400
    return 'bad request', 400


@app.errorhandler(500)
def page_not_found():
    return 'Internal Server error', 500

# TODO: Add error message like 404 error - template


def generate_response(request_data):
    app.logger.info("generate_response(): %s", request_data)

    animal = str(request_data['animal'])
    sound = str(request_data['sound'])
    count = int(request_data['count'])

    # Check if emoji from request exists
    # if yes then return emoji if no return as it is
    if animal.lower() in emoji:
        app.logger.info(emoji[animal])
        animal = emoji[animal]

    app.logger.info(
        "generate_response(): animal is %s, sound is %s, count is %s", animal, sound, count)

    res = ""
    for i in range(count):
        res += animal + " says " + sound + "\n"
    res += "Made with ❤️ by Maxim Chepukov\n"
    return res


if __name__ == '__main__':
    # Start flask application
    app.run(host='0.0.0.0', debug=True, port=5000)

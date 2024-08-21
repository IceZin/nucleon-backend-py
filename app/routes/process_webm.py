from flask import make_response, request
from . import routes
from matplotlib import pyplot as plt
from random import randint


@routes.route('/process-webm', methods=['POST'], endpoint='process_webm')
def process_webm():
    body = request.get_json()

    audio_data = body["data"]

    print(audio_data)

    with open(f"app/audios/{randint(0, 99999)}.wav", "wb") as f:
        f.write(bytes(audio_data))

    plt.plot(audio_data)
    plt.show()

    response = make_response('')
    return response
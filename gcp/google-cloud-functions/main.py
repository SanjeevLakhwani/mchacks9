from numpy import array as arr
from json import load

from tensorflow.keras import Model
from tensorflow.keras.models import load_model
from tensorflow import keras
from tensorflow.keras import layers

from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from google.cloud import storage


def get_file(filename):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('mchacks9')
    blob = bucket.blob("checkpoints/"+filename)

    blob.download_to_filename('/tmp/'+filename)


json_path = '/tmp/token.json'
weights_path = '/tmp/weights.ckpt'
max_length = 20

tokenizer = ""

model = keras.Sequential([
    layers.Embedding(800, 64),
    layers.Bidirectional(layers.LSTM(64)),
    layers.Dense(64, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])



def isProductive(title):
    proc = pad_sequences(tokenizer.texts_to_sequences(arr([title])),
                         maxlen=max_length, truncating="post")

    predic = model(arr(proc))
    predic = predic.numpy()[0][0]

    return predic


def hello_world(request):
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Max-Age': '3600'
        }

        return ('', 204, headers)


    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    get_file("token.json")
    get_file("checkpoint")
    get_file("weights.ckpt.data-00000-of-00001")
    get_file("weights.ckpt.index")

    model.load_weights(weights_path)

    

    with open(json_path) as json_file:
        global tokenizer
        tokenizer = tokenizer_from_json(load((json_file)))

    if(model.layers[0].input_dim==tokenizer.num_words+1):
        print("Match")
    else:
        print("Wrong")

    request_json = request.get_json()
    print("reqest json", request_json)
    print("request", request)
    print("request args", request.args)
    print("nail polish stuff ", isProductive("A nail polish clickbait comedy title"))
    try: 
        if 'title' in request_json:
            title = request_json["title"]
            return (str(isProductive(title)), 200, headers)
    except:
        pass
    
    try: 
        title = request.args.get("title")
        return (str(isProductive(title)), 200, headers)
    except:
        pass

    return ('nothing was provided', 200, headers)
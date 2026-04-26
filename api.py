#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
from prediction import predict_popularity

app = Flask(__name__)

api = Api(
    app,
    version='1.0',
    title='Spotify Popularity Prediction API',
    description='Spotify Popularity Prediction API')

ns = api.namespace('predict',
     description='Spotify Popularity Predictor')

parser = api.parser()
parser.add_argument('duration_ms',      type=float, required=True, help='Duration in ms',          location='args')
parser.add_argument('explicit',         type=int,   required=True, help='Explicit content (0/1)',  location='args')
parser.add_argument('danceability',     type=float, required=True, help='Danceability (0-1)',       location='args')
parser.add_argument('energy',           type=float, required=True, help='Energy (0-1)',             location='args')
parser.add_argument('key',              type=int,   required=True, help='Key (0-11)',               location='args')
parser.add_argument('loudness',         type=float, required=True, help='Loudness in dB',          location='args')
parser.add_argument('mode',             type=int,   required=True, help='Mode (0=minor, 1=major)', location='args')
parser.add_argument('speechiness',      type=float, required=True, help='Speechiness (0-1)',        location='args')
parser.add_argument('acousticness',     type=float, required=True, help='Acousticness (0-1)',       location='args')
parser.add_argument('instrumentalness', type=float, required=True, help='Instrumentalness (0-1)',   location='args')
parser.add_argument('liveness',         type=float, required=True, help='Liveness (0-1)',           location='args')
parser.add_argument('valence',          type=float, required=True, help='Valence (0-1)',            location='args')
parser.add_argument('tempo',            type=float, required=True, help='Tempo in BPM',            location='args')
parser.add_argument('time_signature',   type=int,   required=True, help='Time signature (1-5)',    location='args')
parser.add_argument('track_genre',      type=str,   required=True, help='Genre (e.g. pop, rock)',  location='args')

resource_fields = api.model('Resource', {
    'result': fields.Float,
})

@ns.route('/')
class SpotifyApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        return {"result": predict_popularity(args)}, 200

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
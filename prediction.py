#!/usr/bin/python
import pandas as pd
import joblib
import sys
import os

def predict_popularity(params):
    clf = joblib.load(os.path.dirname(__file__) + '/spotify.pkl')

    row = {
        "duration_ms":       float(params.get("duration_ms")),
        "explicit":          int(params.get("explicit")),
        "danceability":      float(params.get("danceability")),
        "energy":            float(params.get("energy")),
        "key":               int(params.get("key")),
        "loudness":          float(params.get("loudness")),
        "mode":              int(params.get("mode")),
        "speechiness":       float(params.get("speechiness")),
        "acousticness":      float(params.get("acousticness")),
        "instrumentalness":  float(params.get("instrumentalness")),
        "liveness":          float(params.get("liveness")),
        "valence":           float(params.get("valence")),
        "tempo":             float(params.get("tempo")),
        "time_signature":    int(params.get("time_signature")),
        "track_genre":       params.get("track_genre"),
    }

    df = pd.get_dummies(pd.DataFrame([row]), columns=["track_genre"])
    df = df.reindex(columns=clf.feature_names_in_, fill_value=0)

    return round(float(clf.predict(df)[0]), 2)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print('Please add parameters')
    else:
        print('Predicted popularity: ', predict_popularity(sys.argv[1]))
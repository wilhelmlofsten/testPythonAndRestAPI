from ast import arg
from flask import Flask
from flask_restful import Resource, Api, reqparse, abort
from pkg_resources import require
import json

app = Flask("VideoAPI")
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('title', required=True)
parser.add_argument('uploadDate', type=int, required=False)

with open('videos.json', 'r') as f:
    videos = json.load(f)

def write_changes_to_files(): #metod för att sortera filerna genom datum
    global videos
    videos = {k: v for k, v in sorted(videos.items(), key=lambda video: video[1]['uploadDate'])}
    with open('videos.json', 'w') as f:
        json.dump(videos, f)


class Video(Resource):

    def get(self, video_id):
        if video_id == "all":
            return videos
        if video_id not in videos:
            abort(404, message=f"Video {video_id} not found")
        return videos[video_id]
    
    def put(self, video_id):
        args = parser.parse_args()
        new_video = {'title': args['title'], 'uploadDate': args['uploadDate']}
        videos[video_id] = new_video
        write_changes_to_files()
        return {video_id: videos[video_id]}, 201
    
    def delete(self, video_id):
        if video_id not in videos:
            abort(404, message=f"Video {video_id} not found")
        del videos[video_id]
        write_changes_to_files()
        return "", 204

class VideoSchedule(Resource):

    def get(self):
        return videos


    def post(self):
        args = parser.parse_args()
        new_video = {'title': args['title'], 'uploadDate': args['uploadDate']}
        video_id = max(int(v.lstrip('video')) for v in videos.keys()) + 1
        video_id = f"video{video_id}"
        videos[video_id] = new_video
        write_changes_to_files()
        return videos[video_id], 201


api.add_resource(Video, '/videos/<video_id>')
api.add_resource(VideoSchedule, '/videos')

if __name__ == '__main__':
    app.run()
    #app.run(debug=True)
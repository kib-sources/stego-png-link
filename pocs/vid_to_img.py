import ffmpeg
import random

def get_random_frame(input_video, output_image):
    # Get the video's duration in seconds
    probe = ffmpeg.probe(input_video)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    duration = float(video_stream['duration'])

    # Generate a random timestamp within the video's duration
    timestamp = str(int(random.uniform(0, duration)))

    # Extract the frame at the randomly generated timestamp
    (
        ffmpeg
        .input(input_video)
        .filter("fps", fps=1, round="up")
        .filter("select", "gte(t,{})".format(timestamp))
        .output(output_image,vframes=1)
        .run()
    )


input_video = "1.mp4" 
output_image = "image.jpg"

get_random_frame(input_video, output_image)


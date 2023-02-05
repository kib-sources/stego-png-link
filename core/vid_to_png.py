import ffmpeg
import random

def get_random_frame(input_video, output_image):
    probe = ffmpeg.probe(input_video)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    duration = float(video_stream['duration'])

    timestamp = str(int(random.uniform(0, duration)))

    (
        ffmpeg
        .input(input_video)
        .filter("fps", fps=1, round="up")
        .filter("select", "gte(t,{})".format(timestamp))
        .output(output_image, vframes=1)
        .run(quiet=True, overwrite_output=True)
    )

input_video = "1.mp4"
output_image = "image.png"

if __name__ == '__main__':
    get_random_frame(input_video, output_image)
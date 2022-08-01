import requests
import os
import ffmpeg
from datetime import datetime


def generate_gif(url):
    """
    Save video
    Convert one to gif format
    Delete video
    """
    saved_video_name = get_and_save_video(url)
    convert_to_gif(saved_video_name)
    delete_video_file(saved_video_name)


def get_and_save_video(file_url):
    """
    Receive a video url
    Save video in current dir
    Return a name of the saved video
    """
    # check wether it is correct url
    try:
        res = requests.get(file_url)
    except:
        res = None
        print('[ERROR] Wrong url, use another one.')
    # if url correct continue
    if res != None:
        if res.headers['Content-Type'] == 'video/mp4':
            cur_date = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
            video_name = f'TikTok_video_{cur_date}'

            with open(f'{video_name}.mp4', 'wb') as file:
                file.write(res.content)
                print('[INFO] Temporary video file was saved successfully.')

            return video_name
        else:
            print('[ERROR] Incorrect url for current purpose.')


def convert_to_gif(filename):
    """
    Receive filename,
    Get file from current dir,
    Set the output frame rate,
    Save file as gif.
    """
    try:
        stream = ffmpeg.input(f'{filename}.mp4')
        stream = ffmpeg.filter(stream, 'fps',
                               fps=3)  # the less fps, the lower file size
        stream = ffmpeg.output(stream, f'{filename}.gif')
        ffmpeg.run(stream)
        print('[INFO] Gif was created successfully.')
    except Exception as e:
        print(f'[ERROR] Problem with ffmpeg\n{e}')


def delete_video_file(filename):
    """Delete video file"""
    try:
        os.remove(f'{filename}.mp4')
        print('[INFO] Temporary video file was deleted successfully.')
    except FileNotFoundError as e:
        print(f'[ERROR] File not found.\n{e}')


def main(url):
    generate_gif(url)


if __name__ == '__main__':
    main(input("Put your TikTok's video url:\n"))
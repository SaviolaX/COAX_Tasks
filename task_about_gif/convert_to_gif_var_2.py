from datetime import datetime
from moviepy.editor import VideoFileClip

def convert_to_gif(url):
    """
    Get video clip's url
    Convert one to a gif file with 5 fps
    """
    try:
        videoClip = VideoFileClip(url)
        cur_date = datetime.now().strftime('%d_%m_%Y_%H_%M_%S')
        video_name = f'TikTok_video_{cur_date}'
        videoClip.write_gif(f"var_2_{video_name}.gif", fps=5)
        print('[INFO] Gif file was created successfully.')
    except:
        print('[ERROR] Incorrect url.')
    
def main(url):
    convert_to_gif(url)
    
if __name__ == '__main__':
    # main('https://v16-webapp.tiktok.com/7d5598aa1bc18f5f7a970f2f038c4f24/62e86d3e/video/tos/maliva/tos-maliva-ve-0068c799-us/925d16f3f7f64f54b6a679d6dcdd3ce1/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=2572&bt=1286&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZtzKKwe2N8L0yl7Gb&mime_type=video_mp4&qs=0&rc=OTRnOjY4O2U1M2k1Mzg3aEBpMzx5aGY6Zm93PDMzZzczNEAtNGNjXjIzXjMxYTJgYF5iYSNnbmNtcjQwNTFgLS1kMS9zcw%3D%3D&l=202208011817570101902180902252AAD2')
    main(input("Put your TikTok's video url:\n"))
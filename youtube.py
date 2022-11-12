import youtube_dl


class Youtube:
    def __init__(self):
        pass

    def get_audio_link(self, url):
        ydl_opts = {
            'outtmpl': 'audio/current',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info["url"]

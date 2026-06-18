import os
from moviepy.editor import VideoFileClip

def extract_vocals(video_path):
    # آؤٹ پٹ فائل کا نام
    output_audio = video_path.replace(".mp4", "_vocals.mp3")
    
    # ویڈیو لوڈ کریں
    video = VideoFileClip(video_path)
    
    # آڈیو نکالیں
    audio = video.audio
    
    # یہاں میوزک ریموول کا لاجک ہونا چاہیے 
    # (فی الحال یہ صرف آڈیو نکال رہا ہے، میوزک ہٹانے کے لیے Spleeter یا Librosa استعمال ہوتا ہے)
    audio.write_audiofile(output_audio)
    
    return output_audio

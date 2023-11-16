import subprocess
from moviepy.editor import VideoFileClip

#Function that gets the motion flow of a video
input_file = "BBB.mp4"
output_file = "MVBBB.mp4"

# Construct the FFmpeg command
ffmpeg_cmd = [
    "ffmpeg",
    "-flags2", "+export_mvs",
    "-i", input_file,
    "-vf", "codecview=mv=pf+bf+bb",
    output_file
]

# Run the FFmpeg command
subprocess.run(ffmpeg_cmd)

###############################################EX3##############################################################

#Counts the number of tracks in the mp4
def count_tracks(mp4_file):
    try:
        video_clip = VideoFileClip(mp4_file)

        # Counting audio tracks
        if video_clip.audio:
            num_audio_tracks = len(video_clip.audio.reader.infos)
        else:
            num_audio_tracks = 0

        # Counting video tracks
        num_video_tracks = len(video_clip.reader.infos)

        print(f"The MP4 container contains {num_audio_tracks} audio track(s) and {num_video_tracks} video track(s).")
    except Exception as e:
        print(f"Error: {e}")


# Example usage
mp4_file_path = "BBB.mp4"
count_tracks(mp4_file_path)

###############################EX6########################################
import subprocess
import os

def extract_yuv_histogram(input_video, output_histogram):
    # Run ffmpeg command to extract YUV histogram
    subprocess.run(['ffmpeg', '-i', input_video, '-vf', 'split=4[a][b][c][d],[b]histogram[bb],[c]histogram[cc],[d]histogram[dd]', '-b:v', '4M', '-map', '[bb]', '-map', '[cc]', '-map', '[dd]', '-y', output_histogram])

def create_video_with_histogram(input_video, histogram, output_video):
    # Run ffmpeg command to overlay the histogram on the video
    subprocess.run(['ffmpeg', '-i', input_video, '-i', histogram, '-filter_complex', 'overlay=W-w-10:H-h-10', '-y', output_video])

if __name__ == "__main__":
    input_video = "BBB.mp4"
    output_histogram = "/home/manu/Documents/VideoCodification"
    output_video = "BBB-histogram.mp4"

    # Extract YUV histogram
    extract_yuv_histogram(input_video, output_histogram)

    # Create video with overlaid histogram
    create_video_with_histogram(input_video, output_histogram, output_video)

    print(f"Video with histogram saved at: {output_video}")
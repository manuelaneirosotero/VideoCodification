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

##################################################EX2###############################################
# exercise 2

def create_bbb_container(self):
    # Output file paths
    output_video_file = 'bbb_50s.mp4'
    output_mono_audio_file = 'bbb_mono.mp3'
    output_stereo_low_bitrate_audio_file = 'bbb_stereo_low_bitrate.mp3'
    output_aac_audio_file = 'bbb_aac.aac'

    # FFmpeg command to cut video to 50 seconds
    cut_video_cmd = [
        'ffmpeg',
        '-i', self.input_file,
        '-t', '50',
        '-c', 'copy',
        output_video_file
    ]

    #FFmpeg command to export audio as MP3 mono track
    export_mono_audio_cmd = [
        'ffmpeg',
        '-i', output_video_file,
        '-vn',
        '-ac', '1',
        '-q:a', '2',
        output_mono_audio_file
    ]

    # FFmpeg command to export audio in MP3 stereo with lower bitrate
    export_stereo_low_bitrate_audio_cmd = [
        'ffmpeg',
        '-i', output_video_file,
        '-vn',
        '-q:a', '5',
        '-ac', '2',
        output_stereo_low_bitrate_audio_file
    ]

    # FFmpeg command to export audio in AAC codec
    export_aac_audio_cmd = [
        'ffmpeg',
        '-i', output_video_file,
        '-vn',
        '-c:a', 'aac',
        output_aac_audio_file
    ]

    # FFmpeg command to package everything in a .mp4
    package_cmd = [
        'ffmpeg',
        '-i', output_video_file,
        '-i', output_mono_audio_file,
        '-i', output_stereo_low_bitrate_audio_file,
        '-i', output_aac_audio_file,
        '-map', '0:v',
        '-map', '1:a',
        '-map', '2:a',
        '-map', '3:a',
        '-c', 'copy',
        self.output_file
    ]

    # Run FFmpeg commands
    subprocess.run(cut_video_cmd)
    subprocess.run(export_mono_audio_cmd)
    subprocess.run(export_stereo_low_bitrate_audio_cmd)
    subprocess.run(export_aac_audio_cmd)
    subprocess.run(package_cmd)

##################################################EX3###############################################
def get_track_count(self):
    # FFprobe command to get information about input file
    ffprobe_cmd = [
        'ffprobe',
        '-v', 'error',
        '-select_streams', 'a:video',
        '-count_frames', '-show_entries',
        'stream=nb_read_frames',
        '-of', 'default=nokey=1:noprint_wrappers=1',
        input_video
    ]

    # Run FFprobe command and capture the output
    result = subprocess.run(ffprobe_cmd, capture_output=True, text=True)
    track_count = len(result.stdout.strip().split('\n'))
    return track_count


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
    output_file = 'final_output.mp4'

    # Extract YUV histogram
    extract_yuv_histogram(input_video, output_histogram)

    # Create video with overlaid histogram
    create_video_with_histogram(input_video, output_histogram, output_video)

    print(f"Video with histogram saved at: {output_video}")
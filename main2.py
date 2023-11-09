import os
import subprocess
from moviepy.editor import VideoFileClip
import cv2

def convert_to_mpeg(input_video, output_mpeg):
    try:
        video_clip = VideoFileClip(input_video)
        video_clip.write_videofile(output_mpeg, codec="mpeg2video")
        return True
    except Exception as e:
        print(f"Error converting to MPEG: {e}")
        return False

def get_video_info(input_video):
    try:
        cmd = f'ffmpeg -i {input_video}'
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        return result
    except subprocess.CalledProcessError as e:
        return f"Error getting video info: {e.output}"

def modify_resolution(input_video, output_video, width, height):
    try:
        cmd = f'ffmpeg -i {input_video} -vf "scale={width}:{height}" {output_video}'
        subprocess.run(cmd, shell=True, check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error modifying resolution: {e}")
        return False

def get_video_info(video_path):
    # Open the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video file is opened successfully
    if not cap.isOpened():
        print("Error: Could not open the video file.")
        return

    # Get video properties
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = cap.get(cv2.CAP_PROP_FPS)
    duration_seconds = frame_count / frame_rate

    print("Video Information:")
    print(f"Frames: {frame_count}")
    print(f"Frame Width: {frame_width}")
    print(f"Frame Height: {frame_height}")
    print(f"Frame Rate: {frame_rate} FPS")
    print(f"Duration: {duration_seconds:.2f} seconds")

    # Release the video capture object
    cap.release()


if __name__ == "__main__":
    input_video = "BBB.mp4"  # Replace with your input video file
    output_mpeg = "BBB.mpeg"  # Replace with your desired output MPEG file
    output_video = "BBB-resized.mp4"  # Replace with your desired output resized video file
    new_width = 480  # New width
    new_height = 320  # New height
    video_path = "BBB.mp4"  # Replace with the path to your video file
    get_video_info(video_path)

    if convert_to_mpeg(input_video, output_mpeg):
        print("Video converted to MPEG successfully.")
    else:
        print("Video conversion failed.")

    video_info = get_video_info(output_mpeg)
    print("Video Information:")
    print(video_info)

    if modify_resolution(input_video, output_video, new_width, new_height):
        print(f"Video resolution modified to {new_width}x{new_height}.")
    else:
        print("Resolution modification failed.")


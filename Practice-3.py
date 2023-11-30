import subprocess

def convert_video(input_file, output_file, resolution):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'scale={resolution}',
        '-c:a', 'copy',
        output_file
    ]
    subprocess.run(command)


def convert_video_codec(input_file, output_file, resolution, codec):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'scale={resolution}',
        '-c:a', 'copy',
        '-c:v', codec,
        output_file
    ]
    subprocess.run(command)

def compare_codecs(input_file, output_file, resolution, codec1, codec2, codec1_label, codec2_label):
    command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'[0:v]scale={resolution},setpts=PTS-STARTPTS[left];[0:v]scale={resolution},setpts=PTS-STARTPTS[right];[left][right]hstack[top];[0:v]scale=640x480[bottom]',
        '-c:a', 'copy',
        '-map', '[top]',
        '-c:v', codec1,
        f'{output_file}_{codec1_label}.mp4',
        '-map', '[bottom]',
        '-c:v', codec2,
        f'{output_file}_{codec2_label}.mp4',
    ]
    subprocess.run(command)


def main():
    input_video = 'BBB.mp4'
    resolution = '640x480'
    # Convert to 720p
    convert_video(input_video, 'output_720p.mp4', '1280x720')

    # Convert to 480p
    convert_video(input_video, 'output_480p.mp4', '854x480')

    # Convert to 360x240
    convert_video(input_video, 'output_360x240.mp4', '360x240')

    # Convert to 160x120
    convert_video(input_video, 'output_160x120.mp4', '160x120')

    # Convert to 720p using different codecs
    convert_video_codec('output_720p.mp4', 'output_720p_vp8.webm', '1280x720', 'libvpx')
    convert_video_codec('output_720p.mp4', 'output_720p_vp9.webm', '1280x720', 'libvpx-vp9')
    convert_video_codec('output_720p.mp4', 'output_720p_h265.mp4', '1280x720', 'libx265')
    convert_video_codec('output_720p.mp4', 'output_720p_av1.mp4', '1280x720', 'libaom-av1')

    # Convert to 480p using different codecs
    convert_video_codec('output_480p.mp4', 'output_480p_vp8.webm', '854x480', 'libvpx')
    convert_video_codec('output_480p.mp4', 'output_480p_vp9.webm', '854x480', 'libvpx-vp9')
    convert_video_codec('output_480p.mp4', 'output_480p_h265.mp4', '854x480', 'libx265')
    convert_video_codec('output_480p.mp4', 'output_480p_av1.mp4', '854x480', 'libaom-av1')

    # Convert to 360x240 using different codecs
    convert_video_codec('output_360x240.mp4', 'output_360x240_vp8.webm', '360x240', 'libvpx')
    convert_video_codec('output_360x240.mp4', 'output_360x240_vp9.webm', '360x240', 'libvpx-vp9')
    convert_video_codec('output_360x240.mp4', 'output_360x240_h265.mp4', '360x240', 'libx265')
    convert_video_codec('output_360x240.mp4', 'output_360x240_av1.mp4', '360x240', 'libaom-av1')

    # Convert to 160x120 using different codecs
    convert_video_codec('output_160x120.mp4', 'output_160x120_vp8.webm', '160x120', 'libvpx')
    convert_video_codec('output_160x120.mp4', 'output_160x120_vp9.webm', '160x120', 'libvpx-vp9')
    convert_video_codec('output_160x120.mp4', 'output_160x120_h265.mp4', '160x120', 'libx265')
    convert_video_codec('output_160x120.mp4', 'output_160x120_av1.mp4', '160x120', 'libaom-av1')

    # Compare VP8 and VP9
    compare_codecs(input_video, 'output_comparison', resolution, 'libvpx', 'libvpx-vp9', 'vp8', 'vp9')

if __name__ == "__main__":
    main()
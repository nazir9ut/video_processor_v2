import subprocess
import os





def first_pass(ffmpeg_path, src_path):
    cmd = "ffmpeg  -pattern_type glob -i '" + os.path.join(src_path, '*.jpg') + "' -y -c:v libvpx-vp9 -pass 1 -b:v 1000K" \
          " -threads 8 -speed 4  -tile-columns 6 -frame-parallel 1 -auto-alt-ref 1 -lag-in-frames 25  -an  " \
          "-f webm /dev/null"



    subprocess.check_output(cmd, shell=True)






def second_pass(ffmpeg_path, src_path, dst_file):
    cmd = "ffmpeg -pattern_type glob -i '" + os.path.join(src_path, '*.jpg') + "' -y -c:v libvpx-vp9 -pass 2 -b:v 1000K " \
           "-threads 8 -speed 1  -tile-columns 6 -frame-parallel 1 -auto-alt-ref 1 -lag-in-frames 25  -c:a libopus " \
           "-b:a 64k  -f webm " + dst_file



    subprocess.check_output(cmd, shell=True)











def first_and_second_pass(ffmpeg_path, src_file, dst_file):

    try:
        first_pass(ffmpeg_path, src_file)

        second_pass(ffmpeg_path, src_file, dst_file)

    except subprocess.CalledProcessError:
        print("CalledProcessError: cant encode video")
        result = False

    else:
        print("Video encoded successfully")
        result = True


    return result







#
#
#
#
# def first_and_second_pass_bad(ffmpeg_path, src_file, dst_file):
#     try:
#         first_pass(ffmpeg_path, src_file)
#         second_pass(ffmpeg_path, src_file, dst_file)
#     except subprocess.CalledProcessError:
#         result = False
#     else:
#         result = True
#
#     return result
#


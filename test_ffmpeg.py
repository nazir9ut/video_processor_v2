import helper_ffmpeg


ffmpeg_path = '/home/zhuma/bin/ffmpeg'

src_path = '/var/cache/zoneminder/events/Monitor-1/15/08/13/17/51/09'

helper_ffmpeg.first_pass(ffmpeg_path, src_path)


dst_file = '/home/naz/Desktop/Monitor-1/15/08/13/17/51/09/1234.webm'

helper_ffmpeg.second_pass(ffmpeg_path, src_path, dst_file)



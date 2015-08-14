from db import *

import os
import helper_ffmpeg
import helper_path




src_base_path = '/var/cache/zoneminder/events'
dst_base_path = '/home/naz/Desktop/vids'
ffmpeg_path = '/home/zhuma/bin/ffmpeg'



#
# remove all non motion events (like signal ...)
#
query =  Event.delete().where(Event.cause != 'Motion')
query.execute()  # Returns the number of rows deleted.




monitors = Monitor.select()
for monitor in monitors:

    events = Event.select().where(Event.monitor_id == monitor.id)
    count_events = events.count()

    for idx, event in enumerate(events):

        print('count_events')
        print(count_events)

        print('idx')
        print(idx)


        # stop on pre-last element
        if(idx == (count_events - 1)):
            break


        inner_path = os.path.join(monitor.name,
                                  helper_path.date_time_to_path(event.start_time))


        src_path = os.path.join(src_base_path,
                                inner_path)

        dst_path = os.path.join(dst_base_path,
                                inner_path)


        dst_file = os.path.join(dst_path,
                                str(event.id))


        if not os.path.exists(dst_path):
            os.makedirs(dst_path)



        success = helper_ffmpeg.first_and_second_pass(ffmpeg_path, src_path, dst_file)




        if success:
            with db.atomic() as txn:
                PrVideo.create(path_and_file=dst_file,
                               start_time=event.start_time,
                               length=event.length)

                event.delete_instance()
        else:
             with db.atomic() as txn:
                 PrLog.create(notes = str(event))

                 event.delete_instance()



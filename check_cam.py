import cv2
import pyrealsense2 as rs
import numpy as np

def save_frame_camera_cycle(delay=1, window_name='cam check'):
    config = rs.config()

    config.enable_stream(rs.stream.infrared, 1, 640, 480, rs.format.y8, 30)
    config.enable_stream(rs.stream.infrared, 2, 640, 480, rs.format.y8, 30)
    config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
    config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)

    pipeline = rs.pipeline()
    profile = pipeline.start(config)

    while True:
        frames = pipeline.wait_for_frames()
        
        ir_frame2 = frames.get_infrared_frame(2)
        ir_image2 = np.asanyarray(ir_frame2.get_data())
        
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())

        cv2.imshow(window_name, color_image)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cv2.destroyWindow(window_name)
    pipeline.stop()

save_frame_camera_cycle()

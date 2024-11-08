import cv2
import os

def extract_frames(video_path, output_folder, frame_rate=1):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)


    video = cv2.VideoCapture(video_path)


    video_fps = video.get(cv2.CAP_PROP_FPS)


    frame_skip = int(video_fps // frame_rate)


    frame_count = 0
    saved_frame_count = 0


    while True:
        success, frame = video.read()

        if not success:
            break


        if frame_count % frame_skip == 0:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1


        frame_count += 1


    video.release()
    print(f"Extraction terminée ! {saved_frame_count} frames extraites dans '{output_folder}'.")

video_path = 'data/videoTest.mp4'  #  chemin de ta vidéo
output_folder = "./frames"  #  dossier de sortie souhaité
extract_frames(video_path, output_folder, frame_rate=2)  # 1 = 1 image par sec ect..

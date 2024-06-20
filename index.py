import cv2
import os

def extract_frames(video_path, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Load the video
    cap = cv2.VideoCapture(video_path)

    # Check if the video opened successfully
    if not cap.isOpened():
        print(f"Error opening video file: {video_path}")
        return

    frame_count = 0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If frame reading was successful, ret will be True
        if not ret:
            break
        
        # Construct the filename
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")

        # Save the frame as an image file
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    # Release the video capture object
    cap.release()
    print(f"Extracted {frame_count} frames to {output_folder}")

# Example usage
video_path = 'path/to/your/video.mp4'
output_folder = 'path/to/output/folder'
extract_frames(video_path, output_folder)
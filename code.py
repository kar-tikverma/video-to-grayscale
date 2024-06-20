import cv2

# Load the video file
input_video_path = 'video-to-grayscale/input_video.mp4'
cap = cv2.VideoCapture(input_video_path)

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
else:
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(f"FPS: {fps}, Frame Count: {frame_count}, Width: {width}, Height: {height}")

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video_path = 'video-to-grayscale/gray_output.mp4'
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height), isColor=False)

    # Process frames
    frame_num = 0
    while cap.isOpened() and frame_num < frame_count:
        ret, frame = cap.read()
        if not ret:
            print(f"End of video file reached at frame {frame_num}.")
            break
        
        # Convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Write the frame to the output video
        out.write(gray_frame)
        
        frame_num += 1

    # Release resources
    cap.release()
    out.release()

    print(f"Processed {frame_num} frames.")

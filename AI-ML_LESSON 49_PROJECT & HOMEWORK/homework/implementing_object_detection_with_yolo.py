import numpy as np

# Dummy data for object detection homework
def detect_objects_homework(image):
    # Dummy implementation for object detection homework
    objects = ['person', 'car', 'dog', 'cat']
    # Simulate object detection results with confidence scores
    detected_objects = []
    for obj in objects:
        # Randomly generate bounding box coordinates
        xmin = np.random.randint(0, image.shape[1] - 50)
        ymin = np.random.randint(0, image.shape[0] - 50)
        xmax = xmin + np.random.randint(20, 50)
        ymax = ymin + np.random.randint(20, 50)
        # Randomly generate confidence score between 0.5 and 1.0
        confidence_score = np.random.uniform(0.5, 1.0)
        # Append object label, bounding box coordinates, and confidence score
        detected_objects.append({'label': obj, 'bbox': (xmin, ymin, xmax, ymax), 'confidence': confidence_score})
    return detected_objects

# Dummy image data for homework
image_data_homework = np.random.randint(0, 255, size=(480, 640, 3), dtype=np.uint8)

# Perform object detection for homework
detected_objects_homework = detect_objects_homework(image_data_homework)

# Display detected objects for homework
print("Detected Objects (Homework):")
for obj in detected_objects_homework:
    print(f"Label: {obj['label']}, Bounding Box: {obj['bbox']}, Confidence: {obj['confidence']:.2f}")

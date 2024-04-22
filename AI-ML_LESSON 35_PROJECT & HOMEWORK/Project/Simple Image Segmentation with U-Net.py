import numpy as np
import matplotlib.pyplot as plt
import cv2

# Step 1: Generate synthetic images and masks
def generate_data(num_samples, img_size):
    images = []
    masks = []
    for _ in range(num_samples):
        # Generate random shape (circle, square, or triangle)
        shape_type = np.random.choice(['circle', 'square', 'triangle'])
        
        # Generate random color
        color = tuple(np.random.randint(0, 256, (3,)).tolist())
        
        # Generate blank image and mask
        img = np.zeros((img_size, img_size, 3), dtype=np.uint8)
        mask = np.zeros((img_size, img_size), dtype=np.uint8)
        
        # Generate random position and size
        x, y = np.random.randint(10, img_size-10), np.random.randint(10, img_size-10)
        size = np.random.randint(10, 50)
        
        # Draw shape on image and mask
        if shape_type == 'circle':
            cv2.circle(img, (x, y), size, color, -1)
            cv2.circle(mask, (x, y), size, 255, -1)
        elif shape_type == 'square':
            cv2.rectangle(img, (x-size, y-size), (x+size, y+size), color, -1)
            cv2.rectangle(mask, (x-size, y-size), (x+size, y+size), 255, -1)
        elif shape_type == 'triangle':
            points = np.array([[x, y-size], [x-size, y+size], [x+size, y+size]], np.int32)
            cv2.fillPoly(img, [points], color)
            cv2.fillPoly(mask, [points], 255)
        
        images.append(img)
        masks.append(mask)
    
    return images, masks

# Step 2: Visualize synthetic data
def visualize_data(images, masks):
    num_samples = len(images)
    plt.figure(figsize=(12, 4*num_samples))
    for i in range(num_samples):
        plt.subplot(num_samples, 2, i*2+1)
        plt.imshow(images[i])
        plt.title('Image')
        plt.axis('off')
        
        plt.subplot(num_samples, 2, i*2+2)
        plt.imshow(masks[i], cmap='gray')
        plt.title('Mask')
        plt.axis('off')
    plt.show()

# Generate and visualize synthetic data
num_samples = 5
img_size = 128
images, masks = generate_data(num_samples, img_size)
visualize_data(images, masks)

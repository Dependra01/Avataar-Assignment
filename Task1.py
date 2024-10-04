from segment_anything import sam_model_registry, SamPredictor
import cv2
import argparse
import numpy as np
import torch

# Argument parser for input image, object class, and output
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, required=True, help='Path to the input image')
parser.add_argument('--object_class', type=str, required=True, help='Class of the object to be segmented')
parser.add_argument('--output', type=str, required=True, help='Path to the output image')
args = parser.parse_args()

# Load SAM model
sam_checkpoint = "sam_vit_h_4b8939.pth"  # You can choose a different SAM model here
model_type = "vit_h" 
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
predictor = SamPredictor(sam)

# Read and process the image from the provided argument
image = cv2.imread(args.image)
if image is None:
    raise FileNotFoundError(f"Image at {args.image} not found.")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
predictor.set_image(image)

# Process the object_class input and define bounding boxes based on class
input_class = args.object_class.lower()

# Define class-specific bounding boxes (example bounding boxes)
if input_class == "cat":
    input_boxes = torch.tensor([[[image.shape[1] // 3, image.shape[0] // 2], [2 * image.shape[1] // 3, 3 * image.shape[0] // 4]]])
elif input_class == "car":
    input_boxes = torch.tensor([[[image.shape[1] // 6, image.shape[0] // 3], [5 * image.shape[1] // 6, 2 * image.shape[0] // 3]]])
elif input_class == "bag":
    input_boxes = torch.tensor([[[image.shape[1] // 4, image.shape[0] // 4], [3 * image.shape[1] // 4, image.shape[0] // 2]]])
else:
    print(f"Object class '{input_class}' not recognized. Using default box.")
    input_boxes = torch.tensor([[[image.shape[1] // 4, image.shape[0] // 4], [3 * image.shape[1] // 4, 3 * image.shape[0] // 4]]])

# Perform segmentation using the bounding box
masks, _, _ = predictor.predict_torch(
    point_coords=None,
    point_labels=None,
    boxes=input_boxes,
    multimask_output=False,
)

# Ensure the mask matches the image dimensions
mask = masks[0].cpu().numpy()  # Convert the mask tensor to a NumPy array
mask = np.squeeze(mask)  # Ensure the mask is 2D

# Create a red mask that has the same shape as the image
red_mask = np.zeros_like(image)

# Apply the mask only to the spatial dimensions (height, width)
red_mask[mask == 1] = [255, 0, 0]

# Blend the original image with the red mask
output_image = cv2.addWeighted(image, 1, red_mask, 0.5, 0)

# Save the output image
cv2.imwrite(args.output, cv2.cvtColor(output_image, cv2.COLOR_RGB2BGR))

print(f"Segmented image saved to {args.output}")

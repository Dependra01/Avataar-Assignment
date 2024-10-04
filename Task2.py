from segment_anything import sam_model_registry, SamPredictor
import cv2
import argparse
import numpy as np
import torch

# Argument parser for input image, object class, output, and position shifts
parser = argparse.ArgumentParser()
parser.add_argument('--image', type=str, required=True, help='Path to the input image')
parser.add_argument('--object_class', type=str, required=True, help='Class of the object to be segmented')
parser.add_argument('--x', type=int, required=True, help='Number of pixels to shift in the x direction')
parser.add_argument('--y', type=int, required=True, help='Number of pixels to shift in the y direction')
parser.add_argument('--output', type=str, required=True, help='Path to the output image')
args = parser.parse_args()

# Load SAM model
sam_checkpoint = "sam_vit_h_4b8939.pth"
model_type = "vit_h"
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
predictor = SamPredictor(sam)

# Read and process the image from the provided argument
image = cv2.imread(args.image)
if image is None:
    raise FileNotFoundError(f"Image at {args.image} not found.")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
predictor.set_image(image)

# Process the object_class input (for simplicity, we define bounding boxes)
input_class = args.object_class.lower()

if input_class == "shelf":
    input_boxes = torch.tensor([[[image.shape[1] // 3, image.shape[0] // 2], [2 * image.shape[1] // 3, 3 * image.shape[0] // 4]]])
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

mask = masks[0].cpu().numpy()  # Convert the mask tensor to a NumPy array
mask = np.squeeze(mask)  # Ensure the mask is 2D

# Extract the object from the image
object_area = np.zeros_like(image)
object_area[mask == 1] = image[mask == 1]

# Create a blank background where the object used to be
image[mask == 1] = [255, 255, 255]

# Shift the object based on the x and y offsets
M = np.float32([[1, 0, args.x], [0, 1, -args.y]])
shifted_object = cv2.warpAffine(object_area, M, (image.shape[1], image.shape[0]))

# Add the shifted object back into the image
final_image = np.where(shifted_object > 0, shifted_object, image)

# Save the final image
cv2.imwrite(args.output, cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))

print(f"Shifted object saved to {args.output}")

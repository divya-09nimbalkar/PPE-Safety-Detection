import cv2
import torch
import torchvision.transforms as T
from torchvision.models.detection import fasterrcnn_resnet50_fpn

# Load pretrained model
model = fasterrcnn_resnet50_fpn(pretrained=True)
model.eval()

# Transformation
transform = T.Compose([T.ToTensor()])

def detect_ppe(image_path):
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    tensor = transform(img_rgb)
    with torch.no_grad():
        predictions = model([tensor])

    # Draw bounding boxes
    for box, score, label in zip(predictions[0]['boxes'], predictions[0]['scores'], predictions[0]['labels']):
        if score > 0.7:  # confidence threshold
            x1, y1, x2, y2 = box.int().tolist()
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(img, f"Label {label}", (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

    cv2.imshow("PPE Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_ppe("data/raw/sample.jpg")

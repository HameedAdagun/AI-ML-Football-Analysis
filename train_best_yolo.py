from ultralytics import YOLO
import os

current_dir = os.getcwd()

model = YOLO('models/best.pt')

results = model.predict('input_videos/08fd33_4.mp4', save=True, project=current_dir, name='runs')

print(results[0])
print('================================================')
for box in results[0].boxes:
    print(box)
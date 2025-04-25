## AI/ML Football Analysis

I built a YOLO model. The mp4 file inside the input_vidoes folder is the video I used to to run the model (done frame by frame). The avi file inside the runs folder is the output with the players and the football being detected.  Below is a still image from the .avi file. 
![Screenshot 2025-04-23 100737](https://github.com/user-attachments/assets/4d79f697-88ce-4be9-8062-97ac3f478e74)
<br>
I realised that the model was tracking the football the best. Some frames it would ignore the football. I decided to train a YOLO model using a dataset that is already annotated. I downloaded the dataset using roboflow. I then ran the new model. The players, referee and football are all being detected much better now. The output is in the runs2 folder.
<br>
![Screenshot 2025-04-25 113632](https://github.com/user-attachments/assets/715ceece-f6cc-4272-8968-349ac94a1786)

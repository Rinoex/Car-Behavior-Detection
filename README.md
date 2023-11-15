# Car-Behavior-Detection
2022_NUS_ML_Advanced model

## Proposal

Give more information about the deep learning aspect of this advance model, 

e.g. what kind of data? 

what is the DL model? 

What kind of preprocessing of inputs? 

What kind of result form the DL model? 

Any post-processing of outputs from model?



- Data: extract a picture every five frames from the dynamic video file captured by the camera for analysis

- DL model concept:
  - **PoseNet**: It trains a convolutional neural network to regress the 6-DOF camera pose from a single RGB image in an end-to-end manner with no need of additional engineering or graph optimisation.
  - The algorithm takes 5ms per frame to compute. 
  - It uses an efficient 23 layer deep convnet, demonstrating that convnets can be used to solve complicated out of image plane regression problems. This was made possible by leveraging transfer learning from large scale classification data where point based SIFT registration fails. 
- Model construct details:
  - **PoseNet** is a slightly modified version of **GoogLeNet** with 23layers (counting only the layers with trainable parameters).
    <u>modified GoogLeNet as follows:</u>
  - Replace all three softmax classifiers with affine regressors. The softmax layers were removed and each final fully connected layer was modified to output a pose vector of 7-dimensions representing position and orientation.
  - Insert another fully connected layer before the final regressor of feature size 2048. This was to form a localization feature vector which may then be explored for generalisation.
  - At test time we also normalize the quaternion orientation vector to unit length.
- Pretrained: Scaling up the input is equivalent to cropping the input before downsampling to 256 pixels on one side. This increases the spatial resolution of the input pixels.
- **Output**: Returns the anchor points of key parts of the human body


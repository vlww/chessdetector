# ChessDetector

This project can currently detect chess pieces in an image with low confidence using the DetectNet object detection model. With a larger dataset and variety of training data, it can become more confident and accurate. The goal for this project is for it to be able to recognize chess pieces and their positions on a chessboard in an image, and output a FEN, which is a one-line ASCII notation that describes where the pieces are. This is impactful because it would allow physical chess positions to be converted to an online setup, where they can be easily shared and analyzed by a chess engine.

![Detection of chess pieces](https://gcdnb.pbrd.co/images/9jyABzFCrhY9.png?o=1)

## The Algorithm

This program uses DetectNet, which is a convolutional neural network that is designed to detect and localize objects in images or videos. Convolutional neural networks are made up of multiple convolutional layers with a set of filters that break down the image into smaller parts and extract different aspects of the image. With more layers, the neural network can capture more complex patterns. This allows DetectNet to accurately detect objects in real-time.

## Running this project

Make sure you have connected your Nano to a monitor through headed mode, and that your webcam, keyboard, and mouse are all connected. Run the following commands in Terminal:
1. Make sure git and cmake is installed
```
sudo apt install git all
sudo apt install cmake
```
2. Clone jetson-inference and move into the jetson-inference directory
```
git clone https://github.com/dusty-nv/jetson-inference
cd jetson-inference
```
3. Clone this project
```
git clone https://github.com/vlww/chessdetector
```
4. Run the Docker container and mount this directory
```
docker/run.sh --volume ~/jetson-inference/chessdetector:/jetson-inference/chessdetector
```
5. Move into the chessdetector directory and run this script
```
cd chessdetector
python3 my-detect.py
```
After a while, a new window will open with the live camera feed. The program will detect chess pieces in the frame and classify them.

[ChessDetector Demo](https://www.youtube.com/watch?v=v7MKulEIaqI)

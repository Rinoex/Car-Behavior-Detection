import cv2
import time
from pymongo import MongoClient
import datetime
from flask import Flask, render_template, Response, request
import requests
import json
import base64

def request_img(frame):
    size = [frame.shape[1], frame.shape[0]]
    img_bytes = frame.tobytes()
    img_b64 = base64.b64encode(img_bytes).decode('utf-8')
    now = datetime.datetime.now()
    body = {"images": img_b64, "size": size}
    # Server: 101.35.252.209
    # local : 127.0.0.1
    res = requests.post("http://101.35.252.209:5000/detect", headers=headers, data=json.dumps(body))
    fin = datetime.datetime.now()
    print(res.text, "is the result, consume:", (fin-now).microseconds)

def capture_stream(cap):
    cv2.namedWindow(window_name)  # camera's name
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(2)
        if c & 0xFF == ord("n"):
            request_img(frame)
        if c & 0xFF == ord('q'):
            break
def capture_stream2(cap):
    cv2.namedWindow(window_name)  # camera's name
    while cap.isOpened():
        ok, frame = cap.read()
        if not ok:
            break
        cv2.imshow(window_name, frame)
        c = cv2.waitKey(1)
        request_img(frame)
        if c & 0xFF == ord('q'):
            break
def run2():  # 逐帧流
    cap = cv2.VideoCapture(0)
    capture_stream(cap)
    cap.release()
    cv2.destroyWindow(window_name)
def run1():  # 视频流
    cap = cv2.VideoCapture(0)
    capture_stream2(cap)
    cap.release()
    cv2.destroyWindow(window_name)
window_name = "camera"
headers = {"Content-type":"application/json"}
run1()
import tensorflow as tf
import numpy as np
from matplotlib import pyplot as plt
import cv2


interpreter = tf.lite.Interpreter(model_path='lite-model_movenet_singlepose_lightning_3.tflite')
interpreter.allocate_tensors()
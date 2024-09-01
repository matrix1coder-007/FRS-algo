{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# USAGE\n",
    "# python recognize_faces_image.py --encodings encodings.pickle --image examples/example_01.png \n",
    "\n",
    "# import the necessary packages\n",
    "import face_recognition_models\n",
    "import argparse\n",
    "import pickle\n",
    "import cv2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "usage: ipykernel_launcher.py [-h] -e ENCODINGS -i IMAGE [-d DETECTION_METHOD]\n",
      "ipykernel_launcher.py: error: the following arguments are required: -e/--encodings, -i/--image\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "2",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 2\n"
     ]
    }
   ],
   "source": [
    "# construct the argument parser and parse the arguments\n",
    "ap = argparse.ArgumentParser()\n",
    "ap.add_argument(\"-e\", \"--encodings\", required=True,\n",
    "\thelp=\"path to serialized db of facial encodings\")\n",
    "ap.add_argument(\"-i\", \"--image\", required=True,\n",
    "\thelp=\"path to input image\")\n",
    "ap.add_argument(\"-d\", \"--detection-method\", type=str, default=\"cnn\",\n",
    "\thelp=\"face detection model to use: either `hog` or `cnn`\")\n",
    "args = vars(ap.parse_args())\n",
    "\n",
    "# load the known faces and embeddings\n",
    "print(\"[INFO] loading encodings...\")\n",
    "data = pickle.loads(open(args[\"encodings\"], \"rb\").read())\n",
    "\n",
    "# load the input image and convert it from BGR to RGB\n",
    "image = cv2.imread(args[\"image\"])\n",
    "rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)\n",
    "\n",
    "# detect the (x, y)-coordinates of the bounding boxes corresponding\n",
    "# to each face in the input image, then compute the facial embeddings\n",
    "# for each face\n",
    "print(\"[INFO] recognizing faces...\")\n",
    "boxes = face_recognition_models.face_locations(rgb,\n",
    "\tmodel=args[\"detection_method\"])\n",
    "encodings = face_recognition_models.face_encodings(rgb, boxes)\n",
    "\n",
    "# initialize the list of names for each face detected\n",
    "names = []\n",
    "\n",
    "# loop over the facial embeddings\n",
    "for encoding in encodings:\n",
    "\t# attempt to match each face in the input image to our known\n",
    "\t# encodings\n",
    "\tmatches = face_recognition_models.compare_faces(data[\"encodings\"],\n",
    "\t\tencoding)\n",
    "\tname = \"Unknown\"\n",
    "\n",
    "\t# check to see if we have found a match\n",
    "\tif True in matches:\n",
    "\t\t# find the indexes of all matched faces then initialize a\n",
    "\t\t# dictionary to count the total number of times each face\n",
    "\t\t# was matched\n",
    "\t\tmatchedIdxs = [i for (i, b) in enumerate(matches) if b]\n",
    "\t\tcounts = {}\n",
    "\n",
    "\t\t# loop over the matched indexes and maintain a count for\n",
    "\t\t# each recognized face face\n",
    "\t\tfor i in matchedIdxs:\n",
    "\t\t\tname = data[\"names\"][i]\n",
    "\t\t\tcounts[name] = counts.get(name, 0) + 1\n",
    "\n",
    "\t\t# determine the recognized face with the largest number of\n",
    "\t\t# votes (note: in the event of an unlikely tie Python will\n",
    "\t\t# select first entry in the dictionary)\n",
    "\t\tname = max(counts, key=counts.get)\n",
    "\t\n",
    "\t# update the list of names\n",
    "\tnames.append(name)\n",
    "\n",
    "# loop over the recognized faces\n",
    "for ((top, right, bottom, left), name) in zip(boxes, names):\n",
    "\t# draw the predicted face name on the image\n",
    "\tcv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)\n",
    "\ty = top - 15 if top - 15 > 15 else top + 15\n",
    "\tcv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,\n",
    "\t\t0.75, (0, 255, 0), 2)\n",
    "\n",
    "# show the output image\n",
    "cv2.imshow(\"Image\", image)\n",
    "cv2.waitKey(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'face_recognition'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m~\\Desktop\\Parity-InfoTech\\03-face_recognition\\face-recognition-opencv\\face-recognition-opencv\\recognize_faces_image.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m# import the necessary packages\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mface_recognition\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0margparse\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'face_recognition'"
     ]
    }
   ],
   "source": [
    "%run -i \"test.py\" --encodings encodings.pickle --image examples/example_01.png"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

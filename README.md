# Ascii-Art-Generator
## Project Description
In this project we'll be seeing how we can form an ascii art version of an image and a video using ASCII-a very common encoding format. 
## How to run the project
* you can choose Download Zip option in the dropdown of 'code' just above the files or can use git clone command to download the contents of the project.
```
$ git clone https://github.com/devanshmishra10/Ascii-Art-Generator
```
* Once you have the folder and the files in your system open the sketch.py and video.py files in your editor and run the python file one by one.
```
> python sketch.py
```
```
> python video.py
```
> Note : above command maybe different according to the version of python installed in your system so check it accordingly like using python3 command instead of python.
* The video.py file supports Windows OS only in order to show the asciified video so make sure you run this file in Windows only to not get any error. 
* You can change the input image and video files by adding your files in the 'data' folder and changing the name of the file in the code file accordingly.
## Description of my tasks
Here in this project these two are the tasks which I'm performing :
* Taking any image as an input and forming a pencil sketched version of the image but only with ascii characters embedded in it.
* Taking any video and displaying its asciified version on a screen.
## The internal working of the project
* Each individual color is represented by numbers in the interval of 0 to 255. In the same manner images are composed of pixels each having its value between 0 to 255, which can be denoted by ASCII characters.
* In this project firstly the image is converted to grayscale (B/W) then into an inverted image using OpenCV library
Now we use character mapping to convert the grey area into ASCII charcters based on the luminosity of each pixel which forms the ascii form of the pencil sketch version of the input image.
* In the video part of the project, the video is being broken down into different frames and each frame is then being converted into its ascii art form using character mapping and then displayed all together as a whole in the end.
## My learnings from the project
* I got to learn about how are the images being stored in a desktop. 
* Learnt about the character mapping and how ASCII characters differ from in each other in luminosity like,to cover darker regions in the image '&' is used while for lighter regions '.' is used.
* Learnt about the way to even asciify a video.
## Resources
* [AScii Art](https://en.wikipedia.org/wiki/ASCII_art#Types_and_styles)
* [Drawing an Ascii sketch](https://blog.waffles.space/2017/03/01/ascii-sketch/#fnref:2)
* [How images are stored in a computer](https://alekya3.medium.com/how-images-are-stored-in-a-computer-f364d11b4e93)


https://user-images.githubusercontent.com/86547969/174853115-e8533a35-bd49-4f96-9a61-b1fc1cfeef01.mp4


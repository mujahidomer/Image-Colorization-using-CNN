# Image Colorization using Convolutional Neural Network (CNN)
The colorization of grayscale images automatically is very keen topic of research within the different communities of machine learning and computers. Beyond taking consideration from an artificial intelligence perspective, such concept has broad practical applications ranging from video re-establishment to enhancement of image for better accountably. Here approach with learning dataset taken for this. For this designed a **convolutional neural network (CNN)** which takes a black and white image as an input and give a colorized image as output. This colorizing process of black and white images does assigning of 3D (RGB) pixel weights to input which range along only 1D (brightness or intensity). There are various colors which may have same brightness value but can be different in intensity. Due to these redundancy, a significant role is played by human interaction in colorization process.

![](CNN%20IMG/deepL.jpg)

The CNN makes use of back-propagation. The training of dataset comprises of feed forward, loss function, learning parameters and back pass. In this way with the help of batch the whole dataset is trained. Image enhancement is also a wide topic where various enhancement techniques like brightness enhancement, sharpness, contrast enhancement, histogram equalization. So these techniques can be used to get the enhanced image of colored image

### Learning Based Colorization
Before CNN approach *Bugeau and Ta* gave a method which was patch based image colorization which have input of square patches around each pixels. *Cheng et al.* gave a method of colorization of image automatically based on three layer deep neural network. **CNN** based approach was suggested by *Ryan Dahl*. He used it as a feature extractor of an image with the help of pre-trained model. In machine learning, a large set of guideline to solve the issue should be avoided, rather than this a model should provide to system with which it can evaluate examples and instructions should be there to make change in the model whenever it gives a wrong result.

### Back-Propogation
The training makes use of back propagation neural network. It consists of **18 hidden layers** along with *Adam optimizer *which has a *learning rate of 104*. **Rectified Linear Unit (ReLU)** activation function is used to extract the features in the input images to train the convolution layers and the data is stored in checkpoint models. The difference between the actual input image and the output of the CNN layers is marked and then the error is back propagated.

----

#### Enhancement Techniques 
                
1. Histogram Equalization
2. Brightness
3. Contrast
4. Sharpness
5. RGB
6. Powerlog
7. HDR
8. Inverse
                
![](CNN%20IMG/lvl0%20dfd.jpg) 

![](CNN%20IMG/lvl1%20dfd.jpg)  

![](CNN%20IMG/lvl2%20dfd.jpg)  

##### This project was done as the MAJOR PROJECT in the 4 year undergraduate B.Tech course of Information Technology in 8th Semester

import streamlit as st
import streamlit.components.v1 as components

PAGE_HEADER_TEXT="""
# Project Methodology
The project was divided into six tasks which were completed sequentially, one after the other, in order to finish the project.
The tasks were:

 **1. Data Collection**

 **2. Data preprocessing**

 **3. Feature Extraction**

 **4. Model Training**

 **5. Model Validation and Testing**

 **6. Model Deployment**

"""

PAGE_CONTENT_TEXT="""
# Data Collection

Deepfakes have been widely used for malicious purposes such as in the pornography industry. Therefore, there is a need to counteract the illicit use of this powerful technology. The goal of this project is to develop a machine learning model capable of detecting Deepfake vs Real images with high accuracy. The team should be able to accurately detect whether an input image is real or deepfake. Most of the publicly available datasets for Deepfake detection are videos (image sequences). However, the project initially aims at detecting deepFakes in face images and later, it can be extended for videos. Several works on Deepfake detection are present in the literature, but unfortunately most of them lack robustness and generalization: they do not work in real-case scenarios. Therefore, our team decided to use the dataset developed by 'Deepfake Detection and Reconstruction Challenge' held by 21st International Conference on Image Analysis and Processing (ICIAP) Conference. This dataset is more challenging than usual detection approaches, having Deepfake images generated by different state-of-the-art architectures.

## Dataset description

Two datasets of real face images were used for the employed experimental phase: CelebA and FFHQ. Different Deepfake images were generated considering StarGAN, GDWCT, AttGAN, StyleGAN and StyleGAN2 architectures. In particular, CelebA images were manipulated using pre-trained models on StarGAN, GDWCT and AttGAN. Images of StyleGAN and StyleGAN2 were created starting from FFHQ dataset.

A detailed description of the obtained images is given below:
| **Dataset** | **# Images** | **Resolution** | **Description** | 
|--|--|--|--|
| CelebA | 5000 | 178 × 218 | a large-scale face attributes dataset with > 200K celebrity images | 
 | FFHQ | 5000 | 1024 × 1024 | human faces with variations in terms of age, ethnicity and image background | 
 | StarGAN | 1000 | 256 × 256 | CelebA images were manipulated | 
 | GDWCT | 1000 | 216 × 216 | CelebA images were manipulated | 
 | AttGAN | 1000 | 256 × 256 | CelebA images were manipulated | 
 | StyleGAN | 1000 | 1024 × 1024 | Images generated using FFHQ as the input dataset | 
 | StyleGAN2 | 1000 | 1024 × 1024 | Images generated using FFHQ as the input dataset | 

**![](https://lh5.googleusercontent.com/PEu92UV3IBCDfSk1goKbFZhUTTjWepVb6M5UeYPYYXmXgeDxV4fdl2T0UfEMUB3KRdyrw_yz3IKQMrZLndxm4FVgOoNWQRMrt_oQbDEGuuDaQQfBEMRwDqaa2NlZcI3I6G_QLhrfBFo)**

# Data Preprocessing

The team went through a lot of research papers to take inspiration from their work, adopt their augmentation techniques and also try to resolve the limitations of their models. One of the major limitations of these models was that they lacked generalizability. Even the state of the art deepfake detection models lacked generalizability, that is, when these models were tested on deepfakes generated by GANs other than the ones they were trained on, their accuracy often dropped by a huge extent. To solve this problem, we adopted a number of augmentation techniques to make our model robust to deepfakes generated by unseen GANs.

The pre-processing steps taken were:
1.  Resizing images to (160, 160)
2.  Random blackout of facial features such as eyes, nose or mouth 
3.  Random rotation, horizontal or vertical flip   
4.  JPEG compression   
5.  Gaussian blurring, noise addition   
6.  Changing the brightness, saturation, hue and contrast    
7.  Shear shift, zooming, height and width shift
    
We decided to work with (160,160) sized images because many online platforms downsize the images to reduce memory consumption, hence our model is compatible with smaller and low quality images that further increases its robustness.

Proper care was taken to not augment images to an extent such that it degrades the quality of our dataset.

The original dataset had 10K real images and 5K deepfake images. To maintain the balance between the classes, we decided to augment 30K real images and 30K deepfake images. Dataset was split according to the following ratio - 80% for train, 10% for validation and 10% for the test set. Due care was given to balance each of these datasets, hence out of 24K train images, we had 12K real and 12K deepfake images. Similar approach was used for both validation and test set. We decided to work in two teams, one team would augment the images with albumentations library and the other team would work with keras library. Within each team, the work was further divided such that each person worked on utmost 2 folders and everyone used their own augmentation pipeline thereby increasing the variation in the augmented images. Each team generated a total of 60K images, thus at the end of pre-processing, we had a total of 120K images, divided as two separate sets with an aim to train our model on both the sets to improve its generalizability.

# Feature Extraction

In this Project we performed the Feature Extraction on the data pre-processed Images to extract the relevant features for training of the model. We applied many process and extraction kernels and filters like blur, gray-scale, contrast, etc.

We first read the documentations and research papers at hand to fully understand the kernels and the process of feature extraction. We then held weekly meetings to collaboratively and collectively move the task towards its completion. We distributed the work for everyone in the team so that uniformity is formed. Everyone in the team performed their own methodologies to extract the kernels and filters of the Images provided in the training dataset.

Then, the features were passed to the Model Training task to train the neural network.

# Model Training

In this Project after Feature Extraction, we performed the Model Training. We used many models and tested them on the preprocessed datasets. We used many advanced techniques of Model Training like Transfer Learning, Deep Neural Networks, Object Detection models, Image Segmentation models, etc.

The task was divided among the team members to train the model using a small amount of the training data. The models were thoroughly researched and then provided to the team and each member took one model as per their desire. We then held weekly meetings to discuss the model training advancements and if the model was giving good accuracy for the small fraction of the dataset then, the model was asked to be trained on the entire dataset.

The code, implementation and accuracy of every contributor is available on github of the project. The best model was chosen for testing and cross-validation among the many created models by the team. Around 17 models were chosen by the team, out of which 11 models were fully created and Implemented on the entire dataset. After the implementation of the chosen models, the best performing models were chosen to be passed on to the Model Testing Team.

## Fully Created Models

| ***Contributor Name*** | ***Model Name*** | ***Accuracy*** |
|-|-|-|
| Vishu Kalier | esrgan-tf2  | 83 % |
| Mussie Berhane | CNN AlexNet | 85% |
| Abdelrahman Youssry| EfficientNetB5 & ImageNet|  90% |
| Akash Kundu | MogaNetXtiny  | 85.8% |
| Qutaiba Ahmed Ansari | ResNet  | 92% |
| Reem Abdel-Salam | CNN MobilnetV3-ImageNet  | 89% |
| Parnika Damle | volo(VOLO_d2)-ImageNet   | 96.52% |
| Abdul Rahman | DenseNET-264  | 50% | 
| Reem Abdel-Salam | CNN ConvnextTiny-ImageNet  | 97% |
| Abdelrahman Rabah | VGG19_BN   | 80%  |
|  Abdelrahman Youssry| EfficientNetB7 & ImageNet| 92.5% |
| Abdelrahman Youssry| VGG16 & ImageNet|93.5% |


# Model Validation and Testing

After completion of the model training, we conducted validation and testing of the best-performing models to confirm the results and determine the best model for deployment. To evaluate the performance of our deepfake image detection model, we considered precision, recall and F1 score as the most appropriate evaluation metrics. Our primary goal was to reduce the number of false positives (deepfakes being classified as real), so we prioritized recall. However, precision was also important as it measured the model’s ability to accurately distinguish between real images and deepfakes. The F1 score which takes into account both precision and recall, provided a significant measure of the model’s effectiveness.

## Model Evaluation Matrix

| Model Name | Accuracy | Precision | Recall | F1 Score | Tested By |
|-|-|-|-|-|-|
|**ResNet50**|65%||||**Qutaiba Ansari**|
|Deepfake||0.71|0.86|0.78||
|Real||0.27|0.14|0.18||
|**EfficientNetB7**|73%||||**Abdelrahman Youssry**|
|Deepfake||0.83|0.77|0.80||
|Real||0.52|0.60|0.56||
|**EfficientNetB5**|76%||||**Abdelrahman Youssry**|
|Deepfake||0.81|0.86|0.84||
|Real||0.59|0.50|0.54||
|**VGG16**|77%||||**Abdelrahman Youssry**|
|Deepfake||0.81|0.90|0.85||
|Real||0.65|0.46|0.54||
|**ConvNextTiny**|81%||||**Reem Abdel-Salam**|
|Deepfake||0.80|0.99|0.88||
|Real||0.92|0.39|0.54||
|**VOLO-D2**|81%||||**Parnika Damle**|
|Deepfake||0.81|0.95|0.88||
|Real||0.79|0.45|0.57||
|**MobileNetV3**|81%||||**Reem Abdel-Salam**|
|Deepfake||0.92|0.81|0.86||
|Real||0.63|0.82|0.71||

<br>
### Final Model Evaluation Matrix

-   Based on the table above, MobileNetV3 was chosen to be deployed.
    
-   Although, Volo-D2, ConvNextTiny, and MobileNetV3 had almost similar accuracy (81%), the recall for both the deepfakes (0.81) and real images (0.82) is better compared to the other models which had great recall for the deepfake images but performed poorly infront of the real images.
    
-   Although, VOLO-D2 showed higher precision for real images, MobileNetV3 had significantly higher recall. As a result, MobileNetV3 was ultimately chosen over VOLO-D2.
    
-   The F1 Score for the real images (0.71) is better than all of the models present in the table.

### Confusion Matrix for MobileNetV3
In the given test dataset, there were 5000 deepfake images and 2000 real images. The model predicted 4048 deepfakes and 1632 real images correctly. I.e 5680 images out of 7000 images were correctly predicted by our final model.

**![](https://lh6.googleusercontent.com/fHnOQSI4p2fQvGJzDYS4V25a_znNT6QykkYZ8fhs3aMzBf1LbiKRPWhvd6A59kj6w8ihAt_so-uwzIJPFebuE38LBhZLBzq6qXWU9DEen_FZTj4g7IicystEau1NUir1PgEVCFAj818)**

"""

PAGE_DIAGRAM_TEXT=f"""
        <pre class="mermaid">
             graph LR
        A(Data Collection) --> B[Data Preprocessing]
        B --> C(Feature Extraction)
        C --> D
        B --> D(Model Training)
        D --> E(Model Validation and Testing)
        E --> F(Model Deployment)
        </pre>

        <script type="module">
            import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
            mermaid.initialize({{ startOnLoad: true }});
        </script>
        """

st.markdown(PAGE_HEADER_TEXT, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
components.html(PAGE_DIAGRAM_TEXT)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(PAGE_CONTENT_TEXT, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

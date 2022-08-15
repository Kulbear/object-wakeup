## NOTE: This page is still under construction.
## Now we provide a minimal demo only. More to come.

# Object Wake-up: 3D Object Rigging from a Single Image (ECCV 2022) 

## | [[Project Page]](https://kulbear.github.io/object-wakeup/) | [[Arxiv]](https://arxiv.org/pdf/2108.02708v3.pdf) | [[Supplementary]](#) | [[Data]](https://drive.google.com/drive/folders/1y360MpyGendcp7gFsjD1Gr8L0wpzFVLg?usp=sharing) |

![teaser_image](https://kulbear.github.io/object-wakeup/image/main_arch.png)
![teaser_image](https://github.com/Kulbear/object-wakeup/blob/gh-pages/image/visual.png?raw=true)
  
>> Given a single chair image, could we wake it up by reconstructing its 3D shape and skeleton, as well as animating its plausible articulations and motions, similar to that of human modeling? 

>> It is a new problem that not only goes beyond image-based object reconstruction but also involves articulated animation of generic objects in 3D, which could give rise to numerous downstream augmented and virtual reality applications.
  
## Environment Setup
    
```
conda env create -f environment.yaml
conda activate object-wakeup
python setup.py build_ext --inplace
```


## Dataset
  
**(Work in Progress)**

Now we have a release contains sample dataset as well as the source code of the tool we developed in UNREAL 4. It is not yet finished but it is ready to play with if you are interested in.

[[Data Download]](https://drive.google.com/drive/folders/1y360MpyGendcp7gFsjD1Gr8L0wpzFVLg?usp=sharing)

- `ShapeRR_Generation` contains the plug-in we developed in UE4.
- `Chair_Out` provides sample high-resolution rendering data for the Chairs category in ShapeNet.
- Other 3 categories presented in paper is still being processed and a full release is expected in the future.


## Demo
  
To run a demo on our method for 3D reconstruction, please download the sample demo image from [here](https://drive.google.com/drive/folders/1gQbQZcewn0PsTe80BZp3u1Xuw7iq1MYP?usp=sharing).


Put the sample image in folder `./demo_chair`.


Then you may want to download the pretrained model weights from [here](https://drive.google.com/drive/folders/1XPdBjsV21Vmc4s1GLpHW9Yhvaym20j9T?usp=sharing).

Put the checkpoint file in folder `./checkpoint`.

To generate sample meshes using a trained model, use

```
python demo.py demo.yaml
```
  
## Misc

Contact Ji Yang at jyang7@ualberta.ca for any questions or comments.

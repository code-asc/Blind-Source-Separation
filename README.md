# Blind Source Separation

The aim of the project is to separate the images where one image is projected onto the other. This project is for study purpose. 
 
**s1** and **s2** be two images such that  they are not gaussian.
**x1** and **x2** be two images which are linear combination of s1 and s2.

let **A** be the SVD matrix where **A** = **U** * **W** * **V**

Here **U**, **V** perform rotation and **W** for scaling.

**X** = **AS**


![Image of variations](https://raw.githubusercontent.com/code-asc/Blind-Source-Separation/master/img.png " ")

The top two images are the expected outputs **s1** and **s2**.

The middle two images are the inputs **x1** and **x2**.

The bottom two images are the actual outputs.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install cv2
pip install numpy
pip install matplotlib
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

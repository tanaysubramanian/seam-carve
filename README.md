# Seam Carve
In this project, I implemented the Seam Carve algorithm to find vertical seams in images to aid in resizing images without losing important data. This program can read in any image and shrink it by trimming the least important portions of the image. This project uses dynamic programming to produce an efficient solution to optimize such a resizing problem. The algorithm works by removing unimportant pixels from the image by finding the least important vertical seams. These trivial seams contain pixels with the lowest color difference from their neighbors, so they can be removed without significantly compromising the image, as shown in the below image results.

# Results
Example original input image:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/83c0dded-bae2-4877-acb1-779d69507ec9" alt="Image" width="568" height="350"> <br />

Program output of image with 1 trivial vertical seam highlighted:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/7f840fd2-f3b8-4910-8802-4639b247dad1" alt="Image" width="568" height="350"> <br />

Program output of shrunk image with 1 vertical seam removed:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/83c0dded-bae2-4877-acb1-779d69507ec9" alt="Image" width="568" height="350"> <br />

Program output of image with 5 trivial vertical seams highlighted:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/4ce2ee2a-ac87-43ef-a00b-187f363183f2" alt="Image" width="568" height="350"> <br />

Program output of shrunk image with 5 vertical seams removed:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/b45443fc-9a4e-4fbf-a129-dc696d551e5e" alt="Image" width="568" height="350"> <br />

Program output of image with 10 trivial vertical seams highlighted:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/11fe6c49-772a-4739-9e44-7236249a0e5e" alt="Image" width="568" height="350"> <br />

Program output of shrunk image with 10 vertical seams removed:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/c707f2dd-be38-4ca0-b6c5-9b5c5f5ed7a2" alt="Image" width="568" height="350"> <br />

Program output of image with 50 trivial vertical seams highlighted:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/8a9519ac-deb8-4264-9acf-cd4037bcd1e4" alt="Image" width="568" height="350"> <br />

Program output of shrunk image with 50 vertical seams removed:

<img src="https://github.com/tanaysubramanian/seamcarve/assets/139258609/fd9791ac-1177-43f4-aae9-ec149d5673dc" alt="Image" width="568" height="350"> <br />

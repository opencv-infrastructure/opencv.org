---
layout: page
title: OpenCL
type: page
parent: Platforms
---
### Intro

Open Computing Language (OpenCL) is an open standard for writing code that runs across heterogeneous platforms including CPUs, GPUs, DSPs and etc. In particular OpenCL provides applications with an access to GPUs for non-graphical computing (GPGPU) that in some cases results in significant speed-up. In Computer Vision many algorithms can run on a GPU much more effectively than on a CPU: e.g. image processing, matrix arithmetic, computational photography, object detection etc.

### History

Acceleration of OpenCV with OpenCL started 2011 by [AMD](http://amd.com). As the result the OpenCV-2.4.3 release [included](http://code.opencv.org/projects/opencv/wiki/ChangeLog#243) the new `ocl` module containing OpenCL implementations of some existing OpenCV algorithms. That is, when OpenCL runtime and a compatible device are available on a client machine, user may call `cv::ocl::resize()` instead of `cv::resize()` to use the accelerated code. During 3 years more and more functions and classes have been added to the `ocl` module; but it has been a separate API alongside with the primary CPU-oriented API in OpenCV-2.x.

In OpenCV-3.x the architecture concept has been changed to the so-called Transparent API (T-API). In the new architecture a separate OpenCL-accelerated `cv::ocl::resize()` is removed from external API and becomes a branch in a regular `cv::resize()`. This branch is called automatically when it's possible and makes sense from the performance point of view. The T-API implementation was sponsored by [AMD](http://amd.com) and [Intel](http://intel.com) companies.

### Numbers

Some performance numbers are shown on the picture below:

![]({{ site.baseurl }}{% link assets/pages/OpenCV_OpenCL_perf-e1421322901763.jpg %}){: class="center" alt="Bar chart: OpenCL performance in OpenCV 3.0 (iGPU and dGPU vs CPU): MOG - 2x - 6x, warpPerspective - 2x - 7x, ..., matchTemplate - 5x - 30x, Sobel - 10x - 32x"}

### Code sample

Regular CPU code

{% highlight C++ %}
// initialization
VideoCapture vcap(...);
CascadeClassifier fd("haar_ff.xml");
Mat frame, frameGray;
vector<rect> faces;
for(;;){
  // processing loop
  vcap >> frame;
  cvtColor(frame, frameGray, BGR2GRAY);
  equalizeHist(frameGray, frameGray);
  fd.detectMultiScale(frameGray, faces, ...);
  // draw rectangles …
  // show image …
}
{% endhighlight %}

OpenCL-aware code OpenCV-2.x

{% highlight C++ %}
// initialization
VideoCapture vcap(...);
ocl::OclCascadeClassifier fd("haar_ff.xml");
ocl::oclMat frame, frameGray;
Mat frameCpu;
vector<rect> faces;
for(;;){
  // processing loop
  vcap >> frameCpu;
  frame = frameCpu;
  ocl::cvtColor(frame, frameGray, BGR2GRAY);
  ocl::equalizeHist(frameGray, frameGray);
  fd.detectMultiScale(frameGray, faces, ...);
  // draw rectangles …
  // show image …
}
{% endhighlight %}

OpenCL-aware code OpenCV-3.x

{% highlight C++ %}
// initialization
VideoCapture vcap(...);
CascadeClassifier fd("haar_ff.xml");
UMat frame, frameGray;
vector<rect> faces;
for(;;){
  // processing loop
  vcap >> frame;
  cvtColor(frame, frameGray, BGR2GRAY);
  equalizeHist(frameGray, frameGray);
  fd.detectMultiScale(frameGray, faces, ...);
  // draw rectangles …
  // show image …
}
{% endhighlight %}

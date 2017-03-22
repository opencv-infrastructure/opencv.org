---
layout: page
title: Platforms
type: page
---
OpenCV was designed to be cross-platform. So, the library was written in C and this makes OpenCV portable to almost any commercial system, from PowerPC Macs to robotic dogs. Since version 2.0, OpenCV includes its traditional C interface as well as the new C++ one. For the most part, new OpenCV algorithms are now developed in C++. Also wrappers for languages such as Python and Java have been developed to encourage adoption by a wider audience. OpenCV runs on both desktop (Windows, Linux, Android, MacOS, FreeBSD, OpenBSD) and mobile (Android, Maemo, iOS).

### CUDA

In 2010 a new module that provides GPU acceleration was added to OpenCV. The 'gpu' module covers a significant part of the library’s functionality and is still in active development. It is implemented using CUDA and therefore benefits from the CUDA ecosystem, including libraries such as NPP (NVIDIA Performance Primitives). With the addition of CUDA acceleration to OpenCV, developers can run more accurate and sophisticated OpenCV algorithms in real-time on higher-resolution images while consuming less power.

[Read more ...]({{ site.baseurl }}{% link platforms/cuda.md %})

### Android

Since 2010 OpenCV was ported to the Android environment, it allows to use the full power of the library in mobile applications development.

[Introduction]({{ site.baseurl }}{% link platforms/android/index.md %})

[Android Best Practices]({{ site.baseurl }}{% link platforms/android/android-best-practices.html %})

[OpenCV4Android Samples]({{ site.baseurl }}{% link platforms/android/opencv4android-samples.html %})

[OpenCV4Android Usage Model]({{ site.baseurl }}{% link platforms/android/opencv4android-usage-models.html %})

### iOS

In 2012 OpenCV development team actively worked on adding extended support for iOS. Full integration is available since version 2.4.2 (2012).

### OpenCL

In 2011 a new module providing [OpenCL™](http://www.khronos.org/opencl/) accelerations of OpenCV algorithms was added to the library. This enabled OpenCV-based code taking advantage of heterogeneous hardware, in particular utilize potential of discrete and integrated GPUs.
Since version 2.4.6 (2013) the [official OpenCV WinMegaPack]({{ site.link_sf }}/files/opencv-win/) includes the _ocl_ module.

In the _2.4_ branch OpenCL-accelerated versions of functions and classes were located in a separate _ocl_ module and in a separate namespace (`cv::ocl`), and often had different names (e.g. `cv::resize()` vs `cv::ocl::resize()` and `cv::CascadeClassifier` vs `cv::ocl::OclCascadeClassifier`) that required a separate code branch in user application code.
Since OpenCV 3.0 (_master_ branch as of 2013) the OpenCL accelerated branches transparently added to the original API functions and are used automatically when possible/sensible.

[Read more ...]({{ site.baseurl }}{% link platforms/opencl.md %})

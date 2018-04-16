---
layout: page
title: Links
type: page
---
### Publications

*   [Real-time computer vision with OpenCV](https://research.nvidia.com/publication/realtime-computer-vision-opencv) ([pdf](http://research.nvidia.com/sites/default/files/publications/OpenCV_CACM_p61-pulli.pdf))
    Kari Pulli (NVIDIA), Anatoly Baksheev, Kirill Kornyakov, Victor Eruhimov
    in Communications of the ACM, June 2012
*   [The OpenCV Library](http://www.drdobbs.com/open-source/the-opencv-library/184404319)
    Gary Bradski
    in Dr. Dobbs Journal, 2000

**Following links have been gathered with the community help. More can be found on this page: [Q&A forum: Informative websites related to OpenCV]({{ site.link_forum }}/question/69691/informative-websites-related-to-opencv/)**

### Tutorials/Lessons

*   [Learn OpenCV (C++, Python)](http://www.learnopencv.com/)
*   [PyImageSearch (Python)](http://www.pyimagesearch.com/)
*   [Code for the book "Mastering OpenCV with Practical Computer Vision Projects" (C++)](https://github.com/MasteringOpenCV/code)
*   [Learn OpenCV by Examples (C++)](http://opencvexamples.blogspot.com/p/table-of-contents.html)
*   [OpenCV Java Tutorials (Java)](http://opencv-java-tutorials.readthedocs.org/en/latest/)
*   [OpenCV Tutorial (C++)](http://opencv-srf.blogspot.com/)
*   [Tutorials AI Shack (C++)](http://aishack.in/tutorials/)
*   [Tutorials (C++, Qt, Android)](http://amin-ahmadi.com/category/tutorials/opencv-tutorials/)
*   [Advanced OpenCV 3 (Video)](https://www.packtpub.com/application-development/advanced-opencv-3-video)
*   [Building Advanced OpenCV3 Projects with Python (Video)](https://www.packtpub.com/application-development/building-advanced-opencv3-  projects-python-video)
*   [Learn OpenCV with Mapt](https://www.packtpub.com/mapt/search_results?query=OpenCV&ss_cck_field_available=Available,Early%20Access)

### Articles/Pages

*   [Intel INDE - OpenCV](https://software.intel.com/en-us/opencv)
*   [MATLAB - OpenCV](http://www.mathworks.com/discovery/matlab-opencv.html)
*   [Microsoft Open Technologies - OpenCV](https://msopentech.com/blog/tag/opencv/)
*   [NVIDIA - OpenCV](https://developer.nvidia.com/opencv)
*   [Some C++ good practices from the OpenCV source code](http://www.codergears.com/Blog/?p=535)
*   [Using OpenCV's Test Framework](http://quentin.bonnard.eu/blog/2013/10/16/Using-OpenCV_s_test_framework_with_CMake/)

### Blogs

*   [MARE's Computer Vision Study](http://study.marearts.com/)
*   [bytefish.de](http://bytefish.de/tag/opencv/)
*   [Eric Yuan's Blog](http://eric-yuan.me/category/opencv/)
*   [Hanzra Tech](http://hanzratech.in/categories/opencv/)
*   [More Than Technical](http://www.morethantechnical.com/?s=opencv)
*   [Philipp Hasper](http://www.hasper.info/tag/opencv/)

### Other languages

*   [Japanese](http://opencv.jp/)
*   [Tutorials (C++, Spanish)](http://acodigo.blogspot.com.es/p/tutorial-opencv.html)
*   [Tutorials (Python, Spanish)](http://www.aprendiendoando.com/opencv)

### Interesting computer vision algorithms and frameworks

#### OBJECT TRACKING

*   _[Real-time compressive tracking](http://www4.comp.polyu.edu.hk/~cslzhang/CT/CT.htm)_ implementation uses OpenCV.

    Zhang, Kaihua, Lei Zhang, and Ming-Hsuan Yang. "Real-time compressive tracking." European Conference on Computer Vision. Springer Berlin Heidelberg, 2012.

*   _Accurate scale estimation for robust visual tracking_ is implemented in [DLIB library](http://dlib.net/).

    Danelljan, Martin, et al. "Accurate scale estimation for robust visual tracking." British Machine Vision Conference, Nottingham, September 1-5, 2014. BMVA Press, 2014.

#### FACE PRE-PROCESSING

*   _[Tan&Triggs preprocessing](https://github.com/bytefish/opencv/blob/master/misc/tan_triggs.cpp)_, a efficient image pre-processing normalization algorithm to deal with difficult lighting conditions.

    Tan, Xiaoyang, and Bill Triggs. "Enhanced local texture feature sets for face recognition under difficult lighting conditions." IEEE transactions on image processing 19.6 (2010): 1635-1650.

*   _Real-time face pose estimation_ is implemented in [DLIB library](http://dlib.net/). A demo snippet can be found [here](https://gist.github.com/berak/b23262a9cb08a9d0a6d3#file-dlib-landmarks-example).

    Kazemi, Vahid, and Josephine Sullivan. "One millisecond face alignment with an ensemble of regression trees." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2014.

*   _[Face landmarks detector for face alignment](https://github.com/delphifirst/FaceX/)_. A demo snippet can be found [here](https://gist.github.com/berak/79aeb39b59222917c558#file-facex-example).

    Cao, Xudong, et al. "Face alignment by explicit shape regression." International Journal of Computer Vision 107.2 (2014): 177-190.

*   _[Eye localization: Average of Synthetic Exact Filters](https://github.com/laoyang/ASEF)_.

    Bolme, David S., Bruce A. Draper, and J. Ross Beveridge. "Average of synthetic exact filters." Computer Vision and Pattern Recognition, 2009. CVPR 2009. IEEE Conference on. IEEE, 2009.

*   _[Eye localization: Accurate eye centre localisation by means of gradient](https://github.com/trishume/eyeLike)_.

    Timm, Fabian, and Erhardt Barth. "Accurate Eye Centre Localisation by Means of Gradients." VISAPP 11 (2011): 125-130.

*   _[Eye pupil localization (tracking)](https://github.com/chrisjryan/eye-tracker)_. A demo video can be found [here](https://www.youtube.com/watch?v=7J30yNHlXlQ).

    Markuš, Nenad, et al. "Eye pupil localization with an ensemble of randomized trees." Pattern recognition 47.2 (2014): 578-587.

#### FACE DETECTION

*   _[PICO face detector](https://github.com/nenadmarkus/pico)_. MIT license.

    Markuš, Nenad, et al. "Object detection with pixel intensity comparisons organized in decision trees." arXiv preprint arXiv:1305.4537 (2013).

#### FACE RECOGNITION

*   _[FaceNet: A Unified Embedding for Face Recognition and Clustering](https://github.com/cmusatyalab/openface)_.  Torch allows the network to be executed on a CPU or with CUDA on GPU. Apache 2.0 license. It uses OpenCV for many processing steps.

    Schroff, Florian, Dmitry Kalenichenko, and James Philbin. "Facenet: A unified embedding for face recognition and clustering." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2015.

#### FRAMEWORKS

*   _[CAFFE deep learning library](http://caffe.berkeleyvision.org/)_. An example of combining CAFFE and OpenCV can be found [here](http://answers.opencv.org/question/72321/how-can-caffe-be-interfaced-using-opencv/).

    Jia, Yangqing, et al. "Caffe: Convolutional architecture for fast feature embedding." Proceedings of the 22nd ACM international conference on Multimedia. ACM, 2014.

*   _[Machine learning framework mlpack](http://mlpack.org/)_, a scalable C++ machine learning library.

    Curtin, Ryan R., et al. "MLPACK: A scalable C++ machine learning library." Journal of Machine Learning Research 14.Mar (2013): 801-805.

*   _[Machine learning framework LIBSVM](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)_.

    Chang, Chih-Chung, and Chih-Jen Lin. "LIBSVM: a library for support vector machines." ACM Transactions on Intelligent Systems and Technology (TIST) 2.3 (2011): 27.

*   _[Framework for face processing and recognition](http://openbiometrics.org/)_, and more biometric analysis.

    Klontz, Joshua C., et al. "Open source biometric recognition." Biometrics: Theory, Applications and Systems (BTAS), 2013 IEEE Sixth International Conference on. IEEE, 2013.

*   _[DLIB](http://dlib.net/)_, a general purpose cross-platform C++ library designed using contract programming and modern C++ techniques. Boost Software License. OpenCV image objects can be converted into a form usable by dlib routines by using `cv_image`. You can also convert from a dlib matrix or image to an OpenCV Mat using `dlib::toMat()`.

*   _[Human action recognition](https://github.com/DAIGroup/BagOfKeyPoses)_. Apache 2.0 license.

    Chaaraoui, Alexandros Andre, Pau Climent-Pérez, and Francisco Flórez-Revuelta. "Silhouette-based human action recognition using sequences of key poses." Pattern Recognition Letters 34.15 (2013): 1799-1807.

#### TEXTURE DESCRIPTORS

*   _[LBP Modification: High Dimensional LBP](https://github.com/bcsiriuschen/High-Dimensional-LBP)_, is an implementation of high dimensional lbp feature for face recognition.

    Chen, Dong, et al. "Blessing of dimensionality: High-dimensional feature and its efficient compression for face verification." Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition. 2013.

*   _[Local Quantized Patterns LQP](https://github.com/franklan/LQP)_ is based on OpenCV when dealing with the pixel information.

    ul Hussain, Sibt, and Bill Triggs. "Visual recognition using local quantized patterns." Computer Vision–ECCV 2012. Springer Berlin Heidelberg, 2012. 716-729.

    Hussain, Sibt Ul, Thibault Napoléon, and Fréderic Jurie. "Face recognition using local quantized patterns." British machive vision conference. 2012.

#### BACKGROUND SUBTRACTION

*   _[Background Subtraction Library BGSLib](https://github.com/andrewssobral/bgslibrary)_.

    Sobral, Andrews. "BGSLibrary: An opencv c++ background subtraction library." IX Workshop de Visao Computacional (WVC’2013). Vol. 7. 2013.

*   _[Vehicle Detection, Tracking and Counting](https://www.behance.net/gallery/Vehicle-Detection-Tracking-and-Counting/4057777)_ uses OpenCV HAAR cascades in combination with OpenCV background subtraction.

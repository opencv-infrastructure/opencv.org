---
layout: page
title: Android
type: page
parent: Platforms
---
Want a Quick Start link? Use this tutorial: ["OpenCV for Android SDK"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/O4A_SDK.html "OpenCV for Android SDK").


### What you should know

There are two major types of OpenCV4Android beginners, first group is new to Android, and the second - to OpenCV. We'll try to provide some advice for both:

1.  If you're an experienced OpenCV adept and you want to start with Android, you should remember, that Android is not desktop OS, you should prepare yourself for mobile development. We're not aiming to teach you all about Android, so in case you're not really familiar with the platform, you may consider consulting the official [website](http://developer.android.com) for developers, or some short introduction like [this one](http://developer.nvidia.com/sites/default/files/akamai/mobile/docs/android_lifecycle_app_note.pdf). At the same time, we've prepared a special ["Introduction into Android Development"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/android_dev_intro.html) tutorial and a set of samples helping you to become familiar with Android specifics. What's important, is that you can reuse your C++ desktop code. It's even recommended to develop and debug your algorithms in familiar environment, using your PC and favourite IDE. Of course you have to keep efficiency in mind, but please avoid premature optimization. OpenCV was designed to be high-performance, so measure your actual performance before you start to worry. Keep in mind, that majority of modern mobile devices is surprisingly powerful.
2. If you're a confident Android developer, but you need some information on OpenCV, please have a look at the [documentation]({{ site.link_docs }}/) and use the user-support resources if needed: [forum]({{ site.link_forum }}/) and issue [tracker]({{ site.link_gh }}/opencv/issues). And do not forget to look into [tutorials]({{ site.link_docs }}/2.4/doc/tutorials/tutorials.html), they will help you to quickly understand what you can easily accomplish with OpenCV. Computer Vision field has a long history, but some problems are still unsolved. If you're not sure if OpenCV could help you with your task, just ask your question at our forum, people there like to solve quirky problems.

### How to start

OpenCv4Android is available as a SDK with a set of samples and Javadoc documentation for OpenCV Java API. It also contains prebuilt apk-files, which you can run on your device instantly. There are three OpenCV tutorials aimed to help you start:

1.  ["Introduction into Android Development"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/android_dev_intro.html) would be useful for the absolute beginner, because it shows you how to setup Android development environment.
2.  Detailed instructions on SDK are available in the ["OpenCV for Android SDK"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/O4A_SDK.html "OpenCV for Android SDK") tutorial. You'll see a couple of sample applications, which you can use as a basis for your own developments.
3.  ["Android development with OpenCV"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/dev_with_OCV_on_Android.html) shows you how to add OpenCV functionality into your Android application. For those who want to reuse their C++ code, we've created a special section: ["Native/C++"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/dev_with_OCV_on_Android.html#native-c). We propose this way for the professional developers, since native development is a bit harder, but gives you larger opportunities. [Face detection sample]({{ site.baseurl }}{% link platforms/android/opencv4android-samples.html %}) shows an example of wrapping a C++ class to the Java.

If you need additional information on OpenCV usage models, you can check this [page]({{ site.baseurl }}{% link platforms/android/opencv4android-usage-models.html %}).


### Online resources

#### User Communities:

- OpenCV Q&A forum: [{{ site.link_forum }}]({{ site.link_forum }}/). Use it as a major resource for Computer Vision and OpenCV consultancy.
- Read-only OpenCV4Android group: [https://groups.google.com/group/android-opencv](https://groups.google.com/group/android-opencv). This group was replaced by the Q&A forum from above, but its archive is still available.

#### OpenCV4Android documentation:

- Tutorials: ["Introduction into Android Development"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/android_dev_intro.html), ["OpenCV for Android SDK"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/O4A_SDK.html "OpenCV for Android SDK"), ["Android development with OpenCV"]({{ site.link_docs }}/2.4/doc/tutorials/introduction/android_binary_package/dev_with_OCV_on_Android.html).
- Documentation on "OpenCV Manager": please check these [slides]({{ site.link_dl }}/present/ECCV2012%20-%20OpenCV4Android.pdf).
- Javadoc html-files are included into the distribution and available [online]({{ site.link_docs }}/java/2.4.11/).
- [Android Samples]({{ site.baseurl }}{% link platforms/android/opencv4android-samples.html %})
- [Android Best Practices]({{ site.baseurl }}{% link platforms/android/android-best-practices.html %})

#### Information on OpenCV:

- Official documentation for the latest public release: [{{ site.link_docs }}]({{ site.link_docs }}).
- Daily documentation build: [{{ site.link_docs }}/master/]({{ site.link_docs }}/master/).
- And please pay special attention to the [tutorials]({{ site.link_docs }}/2.4/doc/tutorials/tutorials.html) and [C++ cheatsheet]({{ site.link_docs }}/2.4/opencv_cheatsheet.pdf)!

#### 3rd-party samples and tutorials:

- [Open Source Google Glass](https://github.com/jaredsburrows/OpenQuartz) samples by Jared Burrows and Andre Compagno
- [Eyes detection and tracking on Android](http://romanhosek.cz/android-eye-detection-and-tracking-with-opencv/) sample by Roman Hošek (the "face-detection" sample extension)


### Providing feedback

1.  You know, we love [contributions]({{ site.baseurl }}{% link about.md %}#Contribute), especially pull requests on the [GitHub]({{ site.link_gh }}/opencv/pulls)!
2.  If you think you've found a new bug, let's double-check it:

1.  Please check that you use the [latest version]({{ site.baseurl }}{% link releases.html %}) of OpenCV4Android.
2.  Please check the open ["Android issues"]({{ site.link_gh }}/opencv/issues?q=is%3Aopen+is%3Aissue+label%3A%22category%3A+android%22) on the tracker.
3.  Ask OpenCV [community]({{ site.link_forum }}) about your problem.
4.  If you're still suspecting that you're probably the first human who met such problem, let's file a bug! Instructions are [here]({{ site.link_wiki }}/OpenCV4Android).


### Contacts

- Use OpenCV [Q&A forum]({{ site.link_forum }}) for most of your questions. And please help others, this is good for your karma!
- Email: android at opencv dot org. Again, please use the group first of all, we do not provide private consultancy!
- Twitter: [https://twitter.com/OpenCV4Android](http://twitter.com/OpenCV4Android).

This repository contains sources for the http://opencv.org site. It uses [Jekyll](http://jekyllrb.com/) to generate actual site from the sources.

Quick local check can be done using [Docker](https://www.docker.com/) container. The _docker-compose_ tool can be used to build a container and run generator in it with a single command.
In Ubuntu it can be installed with the `sudo apt install docker-compose`.

##### Static serve:
- go to site folder
- run `docker-compose up`
- open _http://localhost:4000_ in browser

##### Build:
- go to site folder
- run `docker-compose run jekyll-server jekyll build`
- find results in the __site_ directory

##### How to add a book:
- add cover JPEG image resized to fit 210x260 box to the _assets/books_ folder
- add an entry to the __data/books.yml_ (in [YAML](https://en.wikipedia.org/wiki/YAML) format) with the following fields:
  - **date** - publishing date, should be in form 'YYYY-MM-DD', it will be used to sort all books from newest to oldest
  - **description** - short text with the book description
  - **image** - name of the book cover file
  - **link** - URL of the book page
  - **title** - book title, will be used as a link text
  - **type** - can be:
    - _english_ - books about using the OpenCV
    - _video_ - video courses
    - _other_ - non-English books
    - _mention_ - books which only mention the OpenCV in some parts

##### How to add a link to the [Links](http://opencv.org/links.html) page
- edit the _links.md_ file (uses [Markdown](https://en.wikipedia.org/wiki/Markdown) syntax)

GRIST
=====

This is grist, so far an experiment in indexing GR OOT projects. You should
probably ignore it for now.

Dependencies / Technologies
--------------------------

The goal is to automate creation of a bunch of static content that helps
explore what people are doing in GR and what kinds of blocks are out there.
Since it's a website it uses HTML/CSS/JS and a touch of jQuery. Otherwise
content is generated with

* jekyll
* flup (a python CGI application)
* block info comes from parsing a tagfile generated with exuberant ctags

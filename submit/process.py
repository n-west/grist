#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from cgi import escape
import sys, os
from flup.server.fcgi import WSGIServer
import urlparse

def app(environ, start_response):
    qs = urlparse.parse_qs(environ['QUERY_STRING'])
    process_form(qs)
    start_response('303 See other', [('Content-Type', 'text/html')])
    print "Location: http://104.131.79.130"
    print

    print 'Content-Type: text/html'
    print 'Location: %s' % redirectURL
    print # HTTP says you have to have a blank line between headers and content
    print '<html>'
    print '  <head>'
    print '    <meta http-equiv="refresh" content="0;url=%s" />' % redirectURL
    print '    <title>You are going to be redirected</title>'
    print '  </head>' 
    print '  <body>'
    print '    Redirecting... <a href="%s">Click here if you are not redirected</a>' % redirectURL
    print '  </body>'
    print '</html>'


    #yield '<h1>Module description</h1>'
    #yield '<table>'
    #for k, v in sorted(qs.items()):
    #     yield '<tr><th>%s</th><td>%s</td></tr>' % (escape(k), escape(v[0]))
    #yield '</table>'
    #yield '<p>'
    #yield '</p>'

def process_form(qs):
    f = open("/srv/grist/_grmodules/"+qs['name'][0] + '.md', "w")
    f.write("---\n")
    f.write("title: %s\n" % escape(qs['name'][0]) )
    f.write("author: %s\n" % escape(qs['module_maintainer'][0]) )
    f.write("description: %s\n" % escape(qs['module_summary'][0]) )
    f.write("type: %s\n" % escape(qs['module_type'][0]) )
    f.write("repo: %s\n" % escape(qs['module_repo_url'][0]) )
    f.write("mirror: http://vanilla.ceat.okstate.edu/cgit/cgit.cgi/%s\n" % escape(qs['name'][0]) )
    f.write("layout: gr_module\n" )
    f.write("---\n")
    f.write("\n%s\n" % qs['module_description'][0])

WSGIServer(app).run()

"""
override class for base.page

"""
from base.render import html
from base.lib import *
from base.Page import Page as basePage

import os, string


class Page(basePage):

  def get_navbar_links(self):
    "override the base version..."
    links=[]
    for uid in (4031,2134,3819):
      p=self.get(uid)
      links.append(
        (p.name,p.url(),p.name)
        )
    links.append(("subscribe","http://feedburner.google.com/fb/a/mailverify?uri=deepian","get email alerts for new posts"))
    links.append(("deepian on twitter","http://twitter.com/deepian","@deepian"))
    return links

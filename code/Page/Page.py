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
    links=[("home","/","latest posts")]
    home=self.get(1)
    for uid in (4031,3819,4405,3506,2134):
      p=self.get(uid)
      links.append(
        (p.name,p.url(),p.name)
        )
    links.append(("favourites",home.url("favourites"),"deepian's favourite posts"))
    links.append(("BapDada's teachings","http://bapdada.deepian.uk","the teachings of Avyakt BapDada"))
#    links.append(("subscribe","http://feedburner.google.com/fb/a/mailverify?uri=deepian","get email alerts for new posts"))
    links.append(("deepian on twitter","http://twitter.com/deepian","@deepian"))
#    links.append(("help","/7","evoke help"))
    return links

  def favourites(self,req):
    "top rated pages, in date order"
    lim=page(req,50)
    req.pages=self.list(kind="page",stage="posted",rating=2,orderby="`when` desc",limit=lim)
    req.title="favourites"
    req.prep="from"
    req.page='favourites' # for paging
    return self.listing(req)


################# publishing (test) ####################

  def save_flat_page(self,content):
    "publish to flat page in site/data folder- just like an image or file"
    # set filename
    self.code="%s.html" % self.uid
    # save the flat file  
    self.save_file(content)
  save_flat_page.permit="no way"

  def publish_page(self,req):
    "publish this page, if it is posted and of kind 'page'"
    if self.kind=="page" and self.stage=="posted":
      self.save_flat_page(self.view(req))
      req.message="page published at <a href={0}>{0}</a>".format(self.file_url())
  publish_page.permit="no way"

  def publish(self,req):
    " publish this page and its branch of descendent pages to flat files"
    # temporarily force guest view
    req.user=self.User.fetch_user("guest")
    req.permits={}
    # publish the page ( branch, recursively - O/S )
    self.publish_page(req)
    # restore admin view
    req.user=self.User.fetch_user("admin")
    return self.view(req)
  publish_page.permit="admin page"

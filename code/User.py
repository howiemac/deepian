"""
override class for base.user

"""

from base.User import User as baseUser

class User(baseUser):

  @classmethod
  def welcome(self,req):
    "override for default page to give latest 'deepians blog' article"
    if req.return_to:
      return req.redirect(req.return_to)
    try:
      where='rating>=0 and parent!=2134 and lineage like ".1.4031.%"'
      res=self.Page.list(kind='page',where=where,stage='posted', orderby="`when` desc",limit="0,1")
      page=res[0]
    except:
      page=None
    if page:
      return req.redirect(page.url())
    return baseUser.welcome(self,req)





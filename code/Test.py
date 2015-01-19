""" 
"""

from base.render import template 

class Test(object):

  @template
  def test(cls,req):
    a=cls.Account.get(4)
    a.contact=2
    req.message="Config is %s " % (cls.Config.__dict__,)
    a.flush()
  test.permit="edit user"
  test=classmethod(test)    

 



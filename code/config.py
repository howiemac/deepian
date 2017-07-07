"""
config file for app single-app server

"""

sitename='deepian'
meta_description="go beyond"
meta_keywords="spiritual,spirituality,soul,enlightenment"

#permits={} #basis of permit system

guests=True #do guests have access by default?
ratings="admin"
attribution="minimal" #attribution=False
chronological=False
default_class="Page"
registration_method="admin" # "admin" : admin has to register each user                                                                    
                              # "approve" : online self registration with approval by admin 

#default_page=4031 #home page is deepian blog
default_page=1 #home page is root

urlpath=""  # no /evoke in url

pagetabs=True

#publishing
folder="~/www/"

from base.data.schema import *

#class Test(Schema):
#  pass

  


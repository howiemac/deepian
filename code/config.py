"""
config file for app single-app server

"""

sitename='deepian'
meta_description="go beyond"
meta_keywords="spiritual,spirituality,soul,enlightenment"

#permits={} #basis of permit system

default_class="Page" #lets us do page urls as domain/123 with no class specified
#flat_files=True # post pages as flat html files, and serve up page views to guest users as flat html files NOT YET IMPLEMENTED...

guests=True #do guests have access by default?
ratings="admin"
attribution="minimal" #attribution=False
chronological=False
registration_method="admin" # "admin" : admin has to register each user                                                                    
                              # "approve" : online self registration with approval by admin 

#default_page=4031 #home page is deepian blog
default_page=1 #home page is root

urlpath=""  # no /evoke in url

pagetabs=True

#publishing
folder="~/www/"

#from base.data.schema import *

#class Test(Schema):
#  pass

  


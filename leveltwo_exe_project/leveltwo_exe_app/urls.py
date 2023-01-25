from django.urls import path
from leveltwo_exe_app import views

# TEMPLATE TAGGING
#this going to allow template tagging,to tell django look under the 'given_as_value' 
# and find the url that matches.
app_name = 'leveltwo_exe_app'

# in the root url this url.py is refferd as the name of the app.
# so every url here will come after the name of the app.
# like this -- leveltwo_exe_app/relative/ or leveltwo_exe_app/other/.
# except first one named=users it's configured direct.

urlpatterns = [
  path('',views.users,name='users'),
  path('relative/',views.relative,name='relative'),
  path('other/',views.other,name='other'),
]


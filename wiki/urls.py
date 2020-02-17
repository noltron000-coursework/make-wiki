from django.urls import path
from wiki.views import PageList, PageDetail

'''
==CHALLENGES==
1. Refactor the URL named `wiki-list-page`.
	-> Point it to the root route (`/`).
	-> No warnings or errors after running:
		`python manage.py runserver`
	-> Test by visiting:
		`http://127.0.0.1:8000/`

2. Refactor the URL named `wiki-details-page`.
	-> Show the DetailsView(?) for any page that exists.
	-> Use the slug field in the Page(?) model to do this.
	-> DO NOT CHANGE the `name` argument.
	-> Test by visiting:
		`http://127.0.0.1:8000/w/{wiki-page-title}`
'''

# ==TODO==
# Check documentation on these things:
# -> '<str:slug>/' string
# -> 'as_view()' method
urlpatterns = [
	path('', PageList.as_view(), name='wiki-list-page'),
	path('<str:slug>/', PageDetail.as_view(), name='wiki-details-page'),
]

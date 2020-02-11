from wiki.models import Page

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class PageList(ListView):
	'''
	Renders a list of all Pages.

	== CHALLENGES ==
	- On GET, display a homepage that shows all Pages in your wiki.
	- Replace this CHALLENGE text with a descriptive docstring for PageList.
	- Replace pass below with the code to render a template named `list.html`.
	'''
	model = Page

	def get(self, request):
		'''
		Returns a list of wiki pages.
		'''
		pass

	"""
	== HINT ==
	def get(self, request):
		'''
		GET a list of Pages.
		'''
		pages = self.get_queryset().all()
		return render(request, 'list.html', {
			'pages': pages
		})
	"""

class PageDetailView(DetailView):
	'''
	Renders a specific page based on it's slug.
	
	== CHALLENGES ==
	- On GET, render a template named `page.html`.
	- Replace this docstring with a description of what thos accomplishes.

	== STRETCHES ==
	- Import the PageForm class from forms.py.
		- This ModelForm enables editing of an existing Page object in the database.
	- On GET, render an edit form below the page details.
	- On POST, check if the data in the form is valid.
		- If True, save the data, and redirect back to the DetailsView.
		- If False, display all the errors in the template, above the form fields.
	- Instead of hard-coding the path to redirect to, use the `reverse` function to return the path.
	- After successfully editing a Page, use Django Messages to "flash" the user a success message
		- Message Content: REPLACE_WITH_PAGE_TITLE has been successfully updated.
	'''
	model = Page

	def get(self, request, slug):
		'''
		Returns a specific of wiki page by slug.
		'''
		pass

	"""
	== HINT ==
	def get(self, request, slug):
		'''
		Returns a specific wiki page by slug.
		'''
		page = self.get_queryset().get(slug__iexact=slug)
		return render(request, 'page.html', {
			'page': page
		})
	"""

	def post(self, request, slug):
		'''
		Creates a new post!
		'''
		pass

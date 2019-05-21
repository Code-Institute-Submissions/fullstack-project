from django.shortcuts import render, get_object_or_404, redirect, reverse,HttpResponse
from .models import Bug, BugComment
from django.contrib.auth.decorators import login_required
# from .forms import BugForm, BugCommentForm
# Create your views here.
@login_required()
def all_bugs(request):
    all_bugs = Bug.objects.all()
    return render(request, "bugs.html", {'all_bugs':all_bugs} )

@login_required()
def upvote_bug(request, id):
    """
    A view that upvotes the selected bug
    """
    bug = Bug.objects.get(pk=id)
    bug.upvotes += 1
    bug.save()
    return redirect(all_bugs)

from django.shortcuts import render, get_object_or_404, redirect, reverse,HttpResponse
from .models import Bug, BugComment
from django.contrib.auth.decorators import login_required
from .forms import BugForm, BugCommentForm
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

@login_required()
def add_bug(request):
    if request.method == "POST":
        submitted_form = BugForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(all_bugs)
        else:
            return(request,"add_bug.html",{
                'form':submitted_form
            })
    else:
        toadd_form = BugForm()
        return render(request,"add_bug.html",{
            'form' : toadd_form
        })

@login_required()
def edit_bug(request, id):
    edit_item = get_object_or_404(Bug, pk=id)
    if request.method == "POST":
        submitted_form = BugForm(request.POST, instance=edit_item)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(all_bugs)
    else:
        form = BugForm(instance=edit_item)
        return render(request, 'edit_bug.html',{
            'item_form':form
        })

@login_required()
def delete_bug(request, id):
    delete_item = get_object_or_404(Bug, pk=id)
    if request.method == "POST":
        delete_item.delete()
        return redirect(all_bugs)
    else:
        return render(request, 'confirm-delete.html',{
            't':delete_item
        })

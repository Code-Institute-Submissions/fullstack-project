from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Feature, FeatureComment
from django.contrib.auth.decorators import login_required
from .forms import FeatureForm, FeatureCommentForm

# Create your views here.
@login_required()
def all_features(request):
    all_features = Feature.objects.all()
    return render(request, "features.html", {'all_features':all_features} )

@login_required()
def upvote_feature(request, id):
    """
    A view that upvotes the selected bug
    """
    feature = Feature.objects.get(pk=id)
    feature.upvotes += 1
    feature.save()
    return redirect(all_features)

@login_required()
def add_feature(request):
    if request.method == "POST":
        submitted_form = FeatureForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            submitted_form.save()
            return redirect(all_features)
        else:
            return(request,"add_feature.html",{
                'form':submitted_form
            })
    else:
        toadd_form = FeatureForm()
        return render(request,"add_feature.html",{
            'form' : toadd_form
        })


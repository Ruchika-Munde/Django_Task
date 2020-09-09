from django.shortcuts import render,redirect,HttpResponseRedirect
from django.forms import inlineformset_factory
from .models import Language,Framework
def display_view(request):
    l=Language.objects.all()
    return render(request,'display.html',{'l':l})

def add_view(request,id):
    obj=Language.objects.get(pk=id)
    frameworkset = inlineformset_factory(Language, Framework, fields=('Fname',))

    # for max number of field**
    # frameworkset = inlineformset_factory(Language, Framework, fields=('Fname',),max_num=2)

    # for extra field**
    #frameworkset = inlineformset_factory(Language, Framework, fields=('Fname',), extra=5)

    # can_delete for delete checkbox**
    #frameworkset=inlineformset_factory(Language,Framework,fields=('Fname',),can_delete=False)
    if request.method=='POST':
        form=frameworkset(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/display/',id=obj.id)
    form=frameworkset(instance=obj)
    return render(request,'add.html',{'form':form,'obj':obj})
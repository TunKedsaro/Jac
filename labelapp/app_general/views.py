from django.shortcuts import render,redirect
from django.http import HttpResponse
from app_general.models import Person
from django.contrib import messages


# def index(request):
#     person = Person.objects.all()
#     return render(request,"index.html",{'data':person})



def index(request):
    filtername = ""
    if request.method == "POST":
        filtername = request.POST["filtername"]
        print(filtername)
        if filtername:
            person = Person.objects.filter(tag=filtername)
        else:
            person = Person.objects.all()
    else:
        person = Person.objects.all()
    tags = Person.objects.values_list('tag',flat=True).distinct()
    return render(request,"index.html",{'data':person,
                                        'tags':tags,
                                        'selected_tag':tags})


def about(request):
    return render(request,"about.html")


def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        tag = request.POST["tag"]
        person = Person.objects.create(
            name = name,
            tag = tag
        )
        person.save()
        messages.success(request,"Saved data !")
        return redirect("/")
    else:
        return render(request,"form.html")



def edit(request,person_id):
    if request.method == "POST":
        person = Person.objects.get(id=person_id)
        person.name = request.POST["name"]
        person.tag  = request.POST["tag"]
        person.save()
        messages.success(request,"Updated data!")
        return redirect("/")
    else:
        person = Person.objects.get(id=person_id)
        return render(request,"edit.html",{"person":person})
    

def delete(request,id_remove):
    print(f"I wanna remove {id_remove}")
    person = Person.objects.get(id=id_remove)
    person.delete()
    return redirect("/")
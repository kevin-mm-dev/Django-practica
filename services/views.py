from django.shortcuts import render
from services.models import Products


# Create your views here.
def index(request):
    response = Products.objects.all()
    return render(request, 'index.html', {'response' : response})

def listaGames(request):
    response = Products.objects.all()
    return render(request, 'listaGames.html', {'response' : response})

def venta(request):
    response = Products.objects.all()
    return render(request, 'venta.html', {'response' : response})

def createSubject(request):
    response = Products.objects.all()
    if request.method=="POST":
        product=Products.objects.create(
            name=request.POST["subject_name"],
            category=request.POST["cate"],
            ubication=request.POST["ubi"],
            lote=request.POST["lote"]
        )
        product.save()
        # return redirect('index')
        return render(request, 'index.html', {'response' : response})
    return render(request, 'create.html')
    # print(request,POST)
    # return render(request, 'create.html')

# def editSubject(request):
#     response = Products.objects.all()
#     product=Products.objects.(
#         name=request.POST["subject_name"],
#         category=request.POST["cate"],
#         ubication=request.POST["ubi"],
#         lote=request.POST["lote"]
#     )
#     product.save()
#     # return redirect('index')
#     return render(request, 'index.html', {'response' : response})
#     # return render(request, 'create.html')



    # if request.method=="POST":
    #     product=Products.objects.create(
    #         name=request.POST["subject_name"],
    #         category=request.POST["cate"],
    #         ubication=request.POST["ubi"],
    #         lote=request.POST["lote"]

    #     )
    #     product.save()
    #     # return redirect('index')
    #     return render(request, 'index.html', {'response' : response})
    # return render(request, 'create.html')
    # print(request,POST)
    # return render(request, 'create.html')

#pip freeze > requeriments.txt
#pip install -r requeriments.txt
from email.message import EmailMessage
from django.shortcuts import render, redirect
from .forms import FormularioCont
# Create your views here.

def cont(request):
    formulariocont=FormularioCont()
    if request.method=="POST":
        formulariocont=FormularioCont(data=request.POST)
        if formulariocont.is_valid():
            nom=request.POST.get("nom")
            ema=request.POST.get("ema")
            cont=request.POST.get("cont")

            ema=EmailMessage("Intercambio",
            "El usuario con nombre {} con la dirección {} escribe lo siguiente: {}".format(nom, ema, cont),
            "", ["alisonantonia75@gmail.com"], reply_to=[ema])
            
            try:
                ema.send()
                return redirect("/cont/?valido")
            except:
                return redirect("/cont/?novalido")
        
        
    return render(request, "cont/cont.html", {'formularioMi':formulariocont})
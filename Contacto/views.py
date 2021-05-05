from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

# Create your views here.
def contacto(request):
    if request.method == "POST":
        asunto = request.POST["name"]
        mensaje = request.POST["message"] + " / Email: " + request.POST["email"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["cesarlazarus123@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contacto/contactoexitoso.html")
    return render(request, "contacto/contacto.html")

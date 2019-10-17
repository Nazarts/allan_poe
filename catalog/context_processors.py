from .models import Categories

def menu(request):
    categories = Categories.objects.all()
    return {"categ":categories}
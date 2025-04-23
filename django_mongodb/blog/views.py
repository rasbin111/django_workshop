from django.shortcuts import render

from core.utils import get_db_handle

def db_check_view(request):
    dbname, client = get_db_handle(db_name="django_mongo", username="admin", password="adminadminadmin", host="localhost", port="27017")
    collection = dbname["medicinedetails"]

#Create two documents
    medicine_1 = {
        "medicine_id": "RR000123456",
        "common_name" : "Paracetamol",
        "scientific_name" : "",
        "available" : "Y",
        "category": "fever"
    }
    medicine_2 = {
        "medicine_id": "RR000342522",
        "common_name" : "Metformin",
        "scientific_name" : "",
        "available" : "Y",
        "category" : "type 2 diabetes"
    }

    collection.insert_many([medicine_1, medicine_2])
    context = {}
    
    medicines = collection.find()
    if medicines:
        context["medicines"] = list(medicines)

    return render(request, 'blog.html', context=context)
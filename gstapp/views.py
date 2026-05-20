from django.shortcuts import render

def gst(request):

    result = ""

    if request.method == 'POST':

        price = float(request.POST.get('price'))
        gst = float(request.POST.get('gst'))

        total = price + (price * gst / 100)

        print("Total Bill Amount =", total)

        result = "Total Bill Amount = ₹ " + str(total)

    return render(request, 'gst.html', {'result': result})
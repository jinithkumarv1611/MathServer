# Ex.04 Design a Website for Server Side Processing
## Date:20-05-2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```python
urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gstapp.urls')),
]

views.py
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

gst.html

<!DOCTYPE html>
<html>
<head>
    <title>GST Calculator</title>
</head>

<body>

<h1>GST Calculator</h1>

<form method="POST">

    {% csrf_token %}

    <label>Price:</label>
    <input type="number" name="price"><br><br>

    <label>GST Percentage:</label>
    <input type="number" name="gst"><br><br>

    <input type="submit" value="Calculate">

</form>

<h2>{{ result }}</h2>

</body>
</html>

DEVELOPED BY: JINITH KUMAR V
REGISTER NO: 212225040157
```



## OUTPUT - SERVER SIDE:
Screenshot 2026-05-20 204913.png

## OUTPUT - WEBPAGE:
Screenshot 2026-05-20 204950.png

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.

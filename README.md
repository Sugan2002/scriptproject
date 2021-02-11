# Mathematical Calculations using JavaScript
## AIM:
To design a website to calculate the area of a circle and volume of a cylinder using JavaScript.

## DESIGN STEPS:
### Step 1: 
Requirement collection.
### Step 2:
Creating the layout using HTML and CSS.
### Step 3:
Write JavaScript to perform calculations.
### Step 4:
Choose the appropriate style and color scheme.
### Step 5:
Validate the layout in various browsers.
### Step 6:
Validate the HTML code.
### Step 6:
Publish the website in the given URL.


## PROGRAM:
### addnumber.html
```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>Adding Two Numbers</title>
    <link rel="stylesheet" href="{% static 'css/maths.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
                ADD TWO NUMBERS
            </div>
            <div class="content">
                <form action="addnumber.html" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">A=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">B=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_add" id="button_add">Add</button>
                    </div>
                    <div  class="forminput">
                        <label for="value_c">C=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>                    
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/maths.js"></script>
</body>

</html>
```
### maths.js
```
addBtn = document.querySelector('#button_add');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c;

    c = parseFloat(txtA.value) + parseFloat(txtB.value);

    txtC.value = c;
});
```

### rectangle.html

```
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <title>AREA OF RECTANGLE</title>
    <link rel="stylesheet" href="{% static 'css/maths.css' %}">
</head>

<body>
    <div class="container">
        <div class="formview">
            <div class="banner">
               AREA OF RECTANGLE 
            </div>
            <div class="content">
                <form action="rectangle.html" method="GET">
                    {% csrf_token %}
                    <div class="forminput">
                        <label for="value_a">length=</label>
                        <input type="text" name="value_a" id="value_a">
                    </div>
                    <div  class="forminput">
                        <label for="value_b">width=</label>
                        <input type="text" name="value_b" id="value_b">
                    </div>                    
                    <div class="forminput">
                        <button type="button" name="button_calculate" id="button_calculate">calculate</button>
                    </div>
                    <div  class="forminput">
                        <label for="value_c">AREA=</label>
                        <input type="text" name="value_c" id="value_c" readonly>
                    </div>                    
                </form>
            </div>
        </div>
    </div>
    <script src="/static/js/mathsrectangle.js"></script>
</body>

</html>

```

### mathsrectangle.js

```
addBtn = document.querySelector('#button_calculate');

addBtn.addEventListener('click',function(e){

    txtA = document.querySelector('#value_a');
    txtB = document.querySelector('#value_b');
    txtC = document.querySelector('#value_c');

    let c;

    c = parseFloat(txtA.value) * parseFloat(txtB.value);

    txtC.value = c;
});
```

## OUTPUT:

![output](./static/img/o1.png)

![output](./static/img/o2.png)


## CODE VALIDATION REPORT:
![output](./static/img/v1.png)

![output](./static/img/v2.png)

## RESULT:
Thus a website is designed for the add two numbers and is hosted in the URL http://suganya.student.saveetha.in:8000/addnumber. HTML code is validated.

Thus a website is designed for the cluculate area of rectangle and is hosted in the URL http://suganya.student.saveetha.in:8000/rectangle. HTML code is validated.
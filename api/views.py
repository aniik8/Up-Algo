from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from CodeEditor.models import Passed
from main.models import Profile

# Create your views here.
PROBLEMS = [
    {
        "id": 1,
        "title": "Nth Fibonacci Sequence",
        "description": "<p>Write a program to compute nth number of a <a href=\"https://en.wikipedia.org/wiki/Fibonacci_number\">fibonacci number sequence</a>.</p><br>Starting Numbers: <code>nth_fib(1) = 0</code>, <code>nth_fib(2) = 1</code><br><br><p>Example Input & Output: </p><ul><li><code>nth_fib(2) = 1</code></li><li><code>nth_fib(6) = 5</code></li></ul><br><h4>Note:</h4><p>If you see a RecursionError, make sure you try again, the maximum number for input is 15.</p> <br><br><h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def nth_fib(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 2,
        "title": "Palindrome Checker",
        "description": "Return True if the string is a <a href='https://en.wikipedia.org/wiki/Palindrome'>palindromic string</a> (same as you read it backward as forward), given with following constraints: <ul><li>Only check  the alphanumeric part of a string,</li><li>This is case insensitive, means that RaCeCar is a palindromic string.</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"race CAR\") = True</code></li><li><code>palindrome(\"2_A3*3#A2\") = True</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "true"
    },
    {
        "id": 3,
        "title": "Reverse a number",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 4,
        "title": "Leap Year or Not",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 5,
        "title": "Find element in a sorted array",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 6,
        "title": "Second maximum element in an array",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 7,
        "title": "",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 8,
        "title": "factorial of a number.",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 3,
        "title": "Armstrong number",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 9,
        "title": "sum of Natural Numbers",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 10,
        "title": "Binary to Decimal to conversion",
        "description": "Return reverse of a number. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "false"
    }
]


def problems(request):
    pros = PROBLEMS.copy()
    for i in pros:
        try:
            Passed.objects.get(user_id=request.user.id, problem_id=i["id"])
            i["complete"] = "True"
        except Passed.DoesNotExist:
            i["complete"] = "False"
    return JsonResponse(pros, safe=False)


def paid(request):
    try:
        request.META["HTTP_REFERER"]
        Profile.objects.filter(user_id=request.user.id).update(paid="True")
        request.session["paid"] = "True"
        return JsonResponse(data={"message": "updated"})
    except:
        return JsonResponse(data={"message": "invalid"})
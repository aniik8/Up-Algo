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
        "description": "<p>Write a program to compute nth number of a <a href=\"https://en.wikipedia.org/wiki/Fibonacci_number\">fibonacci number sequence</a>.</p><br>Starting Numbers: <code>nth_fib(1) = 0</code>, <code>nth_fib(2) = 1</code><br><br><p>Example Input & Output: </p><ul><li><code>nth_fib(2) = 1</code></li><li><code>nth_fib(6) = 5</code></li></ul><br><h4>Note:</h4><p>If you see a RecursionError, make sure you try again, the maximum number for input is 15.</p> <br><br>\
            <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def nth_fib(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 2,
        "title": "Palindrome Checker",
        "description": "Return True if the string is a <a href='https://en.wikipedia.org/wiki/Palindrome'>palindromic string</a> (same as you read it backward as forward), given with following constraints: <ul><li>Only check  the alphanumeric part of a string,</li><li>This is case insensitive, means that RaCeCar is a palindromic string.</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"race CAR\") = True</code></li><li><code>palindrome(\"2_A3*3#A2\") = True</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.<br>\
        <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def palindrome(n):\n\tpass",
        "paid": "true"
    },
    {
        "id": 3,
        "title": "Reverse a number",
        "description": "Return reverse of a number. \
            <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>See documentation here</a> <br>(same as you read it backward as forward), given with following constraints <br><ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>reverse(\"1234\") = 4321</code></li><li><code>reverse(\"1010102\") = 2010101</code></li></ul>.<br>\
                <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def reverse(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 4,
        "title": "Leap Year or Not",
        "description": "Check whether a given year is leap year or not. <a href='https://simple.wikipedia.org/wiki/Reverse_of_a_number'>Know what is leap year here?</a>  given with following constraints: <ul><li>0 <= n <= 2022</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>leap_year(\"2000\") = true</code></li><li><code>leap_year(\"1900\") = false</code></li><li><code>leap_year(2004) = true</code></li></ul>.",
        "starter": "def leap_year(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 5,
        "title": "Find element in a sorted array",
        "description": "Given a sorted array. Find an element and return it's position. <a href='https://en.wikipedia.org/wiki/Sorted_array'>Know more here</a> Given with following constraints: <ul><li>10 <= array_length <= 1000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>findele(\"array = [1, 2, 3, 4]. ele = 3 \") = 2</code></li></ul>.",
        "starter": "def findele(n, element):\n\tpass",
        "paid": "false"
    },
    {
        "id": 6,
        "title": "Find if a number is odd or even.",
        "description": "Given a number, your task is to check if the given number is even or odd. <a href='https://en.wikipedia.org/wiki/Parity_(mathematics)'>See documentation here</a>Given with following constraints: <ul><li>1 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>parity(\"1234\") = true</code></li><li><code>parity(\"123\") = false</code></li></ul>.\
            <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def parity(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 7,
        "title": "Find sum of digit",
        "description": "Given a natural number, Find the sum of the digits of the number. <a href='https://en.wikipedia.org/wiki/Digital_sum'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 10000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>palindrome(\"1234\") = 4321</code></li><li><code>Reverse(\"1010102\") = 2010101</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.\
            <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def sum_digit(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 8,
        "title": "Factorial of a number.",
        "description": "Given a number, find the factorial of that number.\n (Either use iterative or recursive solution, Complexity should be O(n)) <a href='https://en.wikipedia.org/wiki/Factorial'>See documentation here</a> (same as you read it backward as forward), given with following constraints: <ul><li>10 <= num <= 100</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>facto(\"5\") = 120</code></li><li><code>Reverse(\"4\") = 24</code></li><li><code>palindrome(\"This is not palindrome string\") = False</code></li></ul>.\
            <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def facto(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 9,
        "title": "Armstrong number",
        "description": "Check if the given number is an Armstrong Number or not. <a href='https://en.wikipedia.org/wiki/Narcissistic_number'> <br/>Check Documentation here</a> Given with following constraints: <br/> <ul><li>10 <= num <= 10000</li></ul> <br><br> \
            <h4>Examples: </h4><ul><li><code>armstrong(\"153\") = true</code></li><li><code>armstrong(\"370\") = true</code></li><li><code>armstrong(23) = False</code></li></ul>.<br/>\
                <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def armstrong(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 10,
        "title": "Sum of Natural Numbers",
        "description": "Given a number 'n', return the sum of natural number till number n.<br/> <a href='https://en.wikipedia.org/wiki/Natural_number'>Natural Number</a> <br/> Given with following constraints: <ul><li>10 <= num <= 1000</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>sum(\"10\") = 55</code></li><li><code>sum(\"100\") = 5050</code></li><li><code>sum(\"83\") = 3486</code></li></ul>.<br>\
            <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def sum(n):\n\tpass",
        "paid": "false"
    },
    {
        "id": 11,
        "title": "Binary to Decimal to conversion",
        "description": "Given a Binary number, return the respective Decimal number of that binary number. <a href='https://en.wikipedia.org/wiki/Binary_number'>Know Binary Number</a> Given with following constraints: <ul><li>0000 <= num <= 11111111</li></ul> <br><br> <h4>Examples: </h4><ul><li><code>converter(\"1010\") = 10</code></li><li><code>converter(\"0110\") = 6</code></li><li><code>converter(\"1111\") = 28</code></li></ul>.\
            <br/> <h4>Video Walkthrough</h4><iframe width='500' height='315' src='https://www.youtube.com/embed/Hq13p2I5UbY' frameborder='0' allow='accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture' allowfullscreen></iframe>",
        "starter": "def converter(n):\n\tpass",
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
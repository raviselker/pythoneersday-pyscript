# PyScript Assignments
- **Date:** 2022-10-14
- **Author:** Ravi Selker (Ordina Pythoneers)
- **Event:** Pythoneersday of the Ordina Pythoneers

---

To help you get started with PyScript I created a couple of assignments you can do. These assignments are mere a place to get started, so if you at any point feel you want to deviate from the assignment or explore your own ideas, please do so! The goal of this pythoneersday is to experiment with PyScript so let's!

## Need help?

There are a couple of helpful websites with information on PyScript that could help you out if you're stuck:
* https://pyscript.net/ (the official website)
* https://docs.pyscript.net/latest/ (official 'documentation')
* https://realpython.com/pyscript-python-in-browser (an extensive introduction to PyScript)
* https://github.com/pyscript/pyscript/tree/main/examples (example PyScript projects)


## Basic example

To help you get started with the assignments, you can copy-paste the following code into an html file and check whether it works by opening the file using a web browser:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, World!</title>
    <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css" />
    <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
</head>
<body>
    <py-script>print("Hello, World!")</py-script>
</body>
</html>
```

## Assignment Solutions

There's no single way to do these assignments of course, but you can find my solutions in the `examples` directory on the [github page](https://github.com/raviselker/pythoneersday-pyscript).


## Assignment 0 - Getting started

PyScript allows you to easily run python code in the browser by adding the python code in between the `<py-script></py-script>` tags; you only need one (html) file to run your whole app! However, the disadvantage of this method is that IDEs are not very good (yet) at recognizing the python code within an html file. Wouldn't it be easier if you could just write your python code in a `.py` file like you (and your IDE) are used to and then load it into the html file? Luckily, that's possible with PyScript!

### Assignment

**Recreate the 'hello_world' example, but instead of writing the python code within the `py-script` tags, create a separate file and load this into the html file.**

Hints:
* Because browsers don't like it if you try to load local files into your HTML ([because of CORS errors](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/set_up_a_local_testing_server#the_problem_with_testing_local_files)), you'll need to run a local static server. Luckily, python makes it easy to set one up. Just run `python -m http.server` from within your project directory, and you can find your app on the [localhost](http://localhost:8000/)
* You can load the python file directly in the `<py-script>` tags, by using the `src` attribute. See, [the RealPython article](https://realpython.com/pyscript-python-in-browser/#dealing-with-python-code-formatting) for more information.

## Assignment 1 - Manipulating the DOM

Now that you can write your python code in a separate python file again, let's move on from the *hello-world* example and start manipulating some html elements. Up to this point, we've "printed" the values to the screen. Wouldn't it be nicer, if you have some control over where you add certain output and can directly manipulate the DOM from within your python code. [Well, you can](https://realpython.com/pyscript-python-in-browser/#pyscripts-adapter-for-javascript-proxy)!

### Assignment
**Create a clock that updates every second. Make the clock as fancy (or simple) as you like!**

Hints:
* It's best to first create an HTML container with a unique id in your html file, e.g., `<div id="clock"></div>` so that you can easily access (and manipulate) this element.

## Assignment 2 - Third party libraries

Using the standard python library in your browser is already pretty sweet, but it would be great if I'd could use some third-party libraries. [That's possible](https://realpython.com/pyscript-python-in-browser/#managing-python-dependencies-in-pyscript)!

### Assignment
**Create a figure using `matplotlib` and display this figure in the browser. Again, make it as fancy as you'd like.**

## Assignment 3 - Fetching data from an API

Fetching data from a REST API can be very useful. However, because you're constrained to the browser's security policies, fetching data from a REST API is not as straightforward as it usually is in python. Therefore, pyodide provides a conveniant wrapper function (`pyfetch`) that allows you to make asyncronous API calls and it's recommended that you use that (i.e., the requests library will not work).

For this assignment we will fetch a random dog image URL using the following API: https://dog.ceo/api/breeds/image/random

### Assignment
**Fetch the url of a random dog image using the following free REST API: GET https://dog.ceo/api/breeds/image/random. Show this image in the browser. Can you make the image update every 5 seconds? Or by pressing a button?**

Hints:
* You will need to create an `<img>` html element and manipulate the `src` attribute in order to show the picture of the dog. It's best to use [pyodide's javascript proxy](https://realpython.com/pyscript-python-in-browser/#pyodides-javascript-proxy) to select (and manipulate) the element.
* You can of course also decide to use a different REST API and show something completely different. See this [list of free APIs](https://github.com/public-apis/public-apis) for inspiration.

## Assignment 4 - Combining it all!

Now let's create a new app where we combina all the things we learned so far.

### Assignment
**Fetch data from a REST API (e.g., [currency data](https://currencyscoop.com/api-documentation)) continuously and display the change over time in a figure.**
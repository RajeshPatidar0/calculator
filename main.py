from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
    <style>
        body {
            font-family: Arial;
            text-align: center;
            margin-top: 50px;
        }
        input {
            padding: 10px;
            margin: 5px;
            width: 100px;
        }
        button {
            padding: 10px 15px;
            margin: 5px;
            cursor: pointer;
        }
        #result {
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

    <h1>Simple Calculator 🚀</h1>

    <input type="number" id="num1" placeholder="First number">
    <input type="number" id="num2" placeholder="Second number">
    <br>

    <button onclick="calculate('add')">Add</button>
    <button onclick="calculate('subtract')">Subtract</button>
    <button onclick="calculate('multiply')">Multiply</button>
    <button onclick="calculate('divide')">Divide</button>

    <div id="result"></div>

<script>
function calculate(operation) {
    let a = document.getElementById("num1").value;
    let b = document.getElementById("num2").value;

    fetch(`/${operation}?a=${a}&b=${b}`)
    .then(response => response.json())
    .then(data => {
        if (data.result !== undefined) {
            document.getElementById("result").innerHTML = "Result: " + data.result;
        } else {
            document.getElementById("result").innerHTML = "Error: " + data.error;
        }
    });
}
</script>

</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    return html_content


@app.get("/add")
def add(a: float, b: float):
    return {"result": a + b}


@app.get("/subtract")
def subtract(a: float, b: float):
    return {"result": a - b}


@app.get("/multiply")
def multiply(a: float, b: float):
    return {"result": a * b}


@app.get("/divide")
def divide(a: float, b: float):
    if b == 0:
        return {"error": "Division by zero not allowed"}
    return {"result": a / b}

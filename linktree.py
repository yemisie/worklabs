from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Linktree</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .link {
            display: block;
            margin: 10px 0;
            padding: 10px;
            background-color: #0073e6;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
        .link:hover {
            background-color: #005bb5;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>My Links</h1>
        <a href="https://www.linkedin.com/in/emmanuel-oluwayemisi/" class="link">Linkedin</a>
        <a href="https://web.facebook.com/emmanuel.oluwayemisi.5" class="link">fb</a>
        <a href="https://x.com/Emmtit" class="link">twitter</a>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(debug=True)
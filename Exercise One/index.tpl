<html>
    <head>
        <title>{{ data.title }}</title>
    </head>

    <body>
        <ul>
            {% for fact in data.facts %}
                <li>{{ fact.fact }}</li>
            {% endfor %}
        </ul>

    </body>
</html>
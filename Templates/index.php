<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>COVID-19 Data Vizualization</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static',filename='style.css')}}">
</head>
<body>

<div class="main_map">
  {{map|safe}}
</div>



<div>

    <form action="" target="result" method="get">
    <select name="Country">
    <option value="none">test</option>

    </select>
    <p><input type="submit" value="Submit"></p>
    </form>



</div>



</body>
</html>

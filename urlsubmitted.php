<html>
<body> <?php

// var_dump($_POST);

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['userUrl'])) {

    $url = $_POST["userUrl"]; 

    echo "Welcome ". $url ."!"; 
}?>
</body>
</html>
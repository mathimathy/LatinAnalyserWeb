<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <title>Text Analyser</title>
    </head>
    <body>
        <form action="" method="post">
            <textarea type="text" placeholder="Type your text..." id="text" name="text" style="width: 100%;"></textarea><br>
            <input type="submit" value="Submit" name="submit">
        </form>
        <?php header("Content-Type: text/html; charset=utf-8"); ?>
        <?php
            if(isset($_POST['submit'])) {
                $text = $_POST['text'];
                $result = shell_exec('python main.py "'.$text.'"');
                echo utf8_decode($result);
            }

        ?>
    </body>
</html>

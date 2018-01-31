<?php
$updir = '/var/www/html/uploads/';
$filename = $_FILES['upfile']['name'];
$command = 'python GCV_API.py ';

function br(){
echo nl2br("\n");//<br />tag send
}

//up file src
move_uploaded_file($_FILES['upfile']['tmp_name'],$updir.$filename);
?>
<?php
system($command.$updir.$filename,$opt);

if($opt==0){
readfile('result.txt');
}else{
print("文字が認識できませんでした");
}
?>

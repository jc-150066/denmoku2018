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
<h1>Complete</h1>
<HR>
<?php
system($command.$updir.$filename,$opt);
br();

if($opt==0){
readfile('result.txt');
}else{
print("文字が認識できませんでした");
}
br();
br();
br();
echo "<image src = ./uploads/".$filename.">";
?>

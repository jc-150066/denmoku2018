<?php
$updir = '/var/www/html/uploads/';
$filename = $_FILES['up_file']['name'];
$command = 'python GCV_API.py ';

function br(){
echo nl2br("\n");//<br />tag send
}

//up file src
move_uploaded_file($_FILES['up_file']['tmp_name'],$updir.$filename);
?>
<?php
// ファイルのパス
$filepath ='result.txt';

// リネーム後のファイル名
$filename ='result.txt';

// ファイルタイプを指定
header('Content-Type: application/force-download');

// ファイルサイズを取得し、ダウンロードの進捗を表示
header('Content-Length: '.filesize($filepath));

// ファイルのダウンロード、リネームを指示
header('Content-Disposition: attachment; filename="'.$filename.'"');

// ファイルを読み込みダウンロードを実行
readfile($filepath);

<?php

if (!($dblink = mysqli_connect('localhost', 'root', '') )){
    print("cannot connect to database");
    print('Aborting <br>');
    exit();
}

if(!mysqli_select_db( $dblink, 'test' )){
    print("Couldn't select a db");
    print("Aborting ------- <br>");
    exit();
}
$Query = "SELECT * FROM users";
if(!($dbresult=mysqli_query( $dblink, $Query))){
    print("COuldn't execute query");
    print("MYSQL ERROR:".mysql_errors()."<BR>\n");

}
print ("<TABLE>");
print("<th>");
print('<td> Users </td>');
print('<td> Account </td>');
print("</th>");
foreach($dbresult as $user){
    $result = "<tr>"."<td>".$user['email']."</td>"."<td>".$user['email']."</td>"."</tr>";
    print("$result");
}
print("</TABLE>");
?>
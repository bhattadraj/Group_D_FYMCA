<?php
    include("../auth_session.php");
?>

<!DOCTYPE html>
<html lang="en">
    <head>
        <link rel="shortcut icon" href="img/favicon.ico" type="image/x-icon">  
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width,initial-scale=1.0" />
        <link rel="stylesheet" href="style.css" />   
        
        <title>Home Page-Fun-Learn</title>
    
    </head>
    <body>
        <div class="header">
            <table>
                <th>
                    <img src="img/LOGO.png" width="50px" >
                </th>
                <th>
                    <h1 class="h1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        &nbsp;Fun Learn  </h1>
                </th>
                <th>
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                    Welcome, <?php echo $_SESSION['username']; ?>!  <a href="../logout.php"> <button>Logout</button></a>
                </th>
            </table>
        </div>
        
        <div class="container">
        
   	   <div class="panel active" style="background-image:url('img/StackArray.png');" >
           <a href = "../StackArray/StackArray.html"target="_blank">  <h3> Stack using Array Implementation </h3></a>
           </div>

           <div class="panel " style="background-image:url('img/StackLL.png');">
              <a href = "../StackLL/StackLL.html"target="_blank"><h3>Stack using Linked List Implementation</h3> </a>
           </div> 

           <div class="panel " style="background-image:url('img/QueueLL.png');">
            <a href = "../QueueLL/QueueLL.html"target="_blank">  <h3>Queue using Linked List Implementation</h3> </a>
           </div>
 
          <div class="panel " style="background-image:url('img/QueueArray.png');">
             <a href = "../QueueArray/QueueArray.html"target="_blank">  <h3>Queue using Array Implementation</h3> </a>
           </div> 
           
        </div>
        

        <div class="footer">
            <h4 class="h4">Copyright @ 2021 Fun Learn Designed by Raj, Utkarsh, Anuj, Suraj </h4> 
        </div>
        
        <script src="Script.js"></script>
    </body>
</html>


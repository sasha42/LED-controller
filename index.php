<?php
  //File to read
  $file = '/sys/devices/w1_bus_master1/28-0000062e0c90/w1_slave';

  //Read the file line by line
  $lines = file($file);

  //Get the temp from second line
  $temp = explode('=', $lines[1]);

  //Setup some nice formatting (i.e. 21,3)
  $temp = number_format($temp[1] / 1000, 1, '.', ' ');

  if ($_GET['white']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 99 99 99");
  }
  if ($_GET['red']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 99 0 0");
  }
  if ($_GET['green']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 0 99 0");
  }
  if ($_GET['blue']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 0 0 99");
  }
  if ($_GET['police']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/police.sh");
  }
  if ($_GET['off']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 0 0 0");
  }
  if ($_GET['white-on']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 0 0 0 99");
  }
  if ($_GET['white-off']) {
    # This code will run if ?run=true is set.
    exec("/home/pi/scripts/set.sh 0 0 0 0");
  }
  if ($_GET['relay---off--on']) {
    # This code will run if ?run=true is set.
    exec("gpio -g write 25 0");
  }
  if ($_GET['relay--off--off']) {
    # This code will run if ?run=true is set.
    exec("gpio -g write 25 1");
  }
  if ($_GET['relay2--off--on']) {
    # This code will run if ?run=true is set.
    exec("gpio -g write 10 0");
  }
  if ($_GET['relay2--off--off']) {
    # This code will run if ?run=true is set.
    exec("gpio -g write 10 1");
  }
?>
<!-- Yes, it's ugly, but STFU. This will be rewritten properly without PHP one day. -->

<!DOCTYPE html>
<html>
<head>
  <title>Fixme conrtol</title>
  <link rel="stylesheet" href="css/bootstrap.min.css">
  <!-- <link rel="stylesheet" href="css/bootstrap-theme.min.css"> -->
  <script src="js/bootstrap.min.js"></script>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <div class="container-fluid">
    <p>
      <h1>Control Interface</h1>
      <p>
      </div>
    </div>
      <div class="container-fluid col-md-6">
        <h2>RGB LEDs</h2>
        <div class="container-fluid well">
         <p>
           <a href="?red=true" type="button" class="btn btn-danger btn-lg btn-block">Red</button></a>
           <a href="?green=true" type="button" class="btn btn-success btn-lg btn-block">Green</button></a>
           <a href="?blue=true" type="button" class="btn btn-primary btn-lg btn-block">Blue</button></a>
           <div class="row">
             <div class="col-md-6"><a href="?white=true" type="button" class="btn btn-default btn-lg btn-block">On</button></a></div>
             <div class="col-md-6"><a href="?off=true" type="button" class="btn btn-default btn-lg btn-block">Off</button></a></div>
           </div>
         </p>
       </div>
     </div>
   </div>
 </div>
 <div class="container-fluid col-md-6">
  <h2>White LEDs</h2>
  <div class="container-fluid well well-sm">
   <p>
    <div class="col-md-6"><a href="?white-on=true" type="button" class="btn btn-default btn-lg btn-block">On</button></a></div>
    <div class="col-md-6"><a href="?white-off=true" type="button" class="btn btn-default btn-lg btn-block">Off</button></a></div>
  </p>
</div>
</div>
<div class="container-fluid col-md-6">
<h2>Server <small>rack temperature: <code><b><?php echo $temp ?></b></code></small></h2>
  <div class="container-fluid well well-sm">
<p>
  <div class="row">
    <div class="col-md-6"><a href="?meh=true" type="button" class="btn btn-default btn-lg btn-block">On</button></a></div>
    <div class="col-md-6"><a href="?meh2=true" type="button" class="btn btn-default btn-lg btn-block">Off</button></a></div>
  </div>
</p>
</div>
<br>
</body>


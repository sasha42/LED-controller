<?php
if ($_GET['relay2-on']) {
  # This code will run if ?run=true is set.
  exec("gpio -g write 11 0");
}
if ($_GET['relay2-off']) {
  # This code will run if ?run=true is set.
  exec("gpio -g write 11 1");
}

//File to read
$file = '/sys/devices/w1_bus_master1/28-0000062e0c90/w1_slave';

//Read the file line by line
$lines = file($file);

//Get the temp from second line
$temp = explode('=', $lines[1]);

//Setup some nice formatting (i.e. 21,3)
$temp = number_format($temp[1] / 1000, 1, '.', ' ');

//And echo that temp
//echo "The temperature is fucking " . $temp ;

?>
<html>
    <head>
        <title>Monitor</title>
	<meta http-equiv="refresh" content="5" >
    </head>
<body>
	<h1><center><font size="7"><b><?php echo $temp ?> &#8451;</b></font></center></h1>
        <center><a href="?relay2-on=true">On</a> / <a href="?relay2-off=true">Off</a></center>
</body>
</html>

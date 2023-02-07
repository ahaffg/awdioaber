// script for hero-image onload change adapted from http://
// jsbin.com/pozadujeca/edit?js,console,output and https://
// stackoverflow.com/questions/32288049/how-to-set-full-page-
// background-image-of-a-div-that-changes-on-page-load

window.onload=function(){  
  var thediv=document.getElementById("hero-image");  
  var imgarray = new Array ("media/abyss-headphones-diana.jpg", "media/AP80-PRO-X-Red-Copper-Edition.jpg", "media/audeze-lcdi4.jpg", "media/audeze-mm500.jpg", "media/auris-audio-ha-2sf.jpg", "media/auris-ha-2se.jpg", "media/campfire-audio-solaris-SE.jpg", "media/cayin-c9-2.jpg", "media/cayin-ha-300mk2.jpg", "media/cayin-n8.jpg", "media/chord-electronics-mojo-2.jpg", "media/dan-clark-audio-expanse.jpg" );  
  var spot =Math.floor(Math.random()* imgarray.length);  
 console.
log(spot); thediv.style.background="url("+imgarray[spot]+")";
}
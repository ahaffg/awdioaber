window.onload=function(){  
  var thediv=document.getElementById("hero-image");  
  var imgarray = new Array ("media/abyss-headphones-diana.jpg", "media/AP80-PRO-X-Red-Copper-Edition.jpg", "media/Aroma-Audio-Jewel.jpg" );  
  var spot =Math.floor(Math.random()* imgarray.length);  
 console.
log(spot); thediv.style.background="url("+imgarray[spot]+")";
}
// script for hero-image onload change adapted from http://
// jsbin.com/pozadujeca/edit?js,console,output and https://
// stackoverflow.com/questions/32288049/how-to-set-full-page-
// background-image-of-a-div-that-changes-on-page-load

window.onload=function(){  
  var thediv=document.getElementById("hero-image");  
  var imgarray = new Array ("media/abyss-headphones-diana.jpg", "media/AP80-PRO-X-Red-Copper-Edition.jpg", "media/AP80-PRO-X-Red-Copper-Edition.jpg", "media/audeze-mm500.jpg", "media/auris-audio-ha-2sf.jpg", "media/auris-ha-2se.jpg", "media/campfire-audio-solaris-SE.jpg", "media/cayin-c9-2.jpg", "media/cayin-ha-300mk2.jpg", "media/cayin-n8.jpg", "media/chord-electronics-mojo-2.jpg", "media/dan-clark-audio-expanse.jpg", "media/dCS-Bartok.jpg", "media/dekoni-audio-blue.jpg", "media/Denafrips-Ares-II.jpg", "earmen-angel.jpg", "media/earmen-ch-amp.jpg", "media/earmen-ch-amp.jpg", "media/empire-ears-odin.jpg", "media/feliks-audio-envy.jpg", "media/ferrum-erco.jpg", "media/fiio-m17.jpg", "media/final-d8000.jpg", "media/fir-audio-krypton.jpg", "media/formula-s-title.jpg", "media/gustard-x18.jpg", "media/hiby-r6-pro.jpg", "media/HiBy-R8.jpg", "media/hiby-rs8.jpg", "media/HIFIMAN-Sundara-Closed-Back.jpg", "media/hugo-title.jpg", "media/ibasso-dx240.jpg", "media/media/ibasso-dx300-max.jpg", "media/ifi-audio-GO-Bar.jpg", "media/media/ifi-audio-xdsd-gryphon.jpg", "media/ifi-audio-ZEN-Air.jpg", "media/IFI-AUDIO-ZEN-ONE.jpg", "media/iFi-Micro-iDSD-signature-series-2.jpg", "media/lime-ears-anima.jpg", "media/little-dot-VII.jpg", "media/lotoo-PAW-gold.jpg", "/workspace/awdioaber/media/luxury-and-precision-p6-pro.jpg", "/workspace/awdioaber/media/moondrop-void.jpg", "media/musician-audio-pegasus-r2r.jpg", "media/noble-audio-viking-ragnar.jpg", "media/noble-ausio-sultan.jpg", "media/sennheiser-ie600.jpg", "media/smsl-d-6.jpg", "media/topping-d10-balanced.jpg", "media/Violectric-DHA-V590.jpg", "media/vision-ears-ext.jpg", "media/Vision-Ears-Phonix.jpg", "media/xDuoo-MU-601.jpg", "media/zmf-headphones-atirum.jpg", "media/zmf-headphones-caldera.jpg" );  
  var spot =Math.floor(Math.random()* imgarray.length);  
 console.
log(spot); thediv.style.background="url("+imgarray[spot]+")";
};s

$('.carousel').carousel()
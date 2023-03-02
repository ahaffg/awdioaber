// script for hero-image onload change adapted from http://
// jsbin.com/pozadujeca/edit?js,console,output and https://
// stackoverflow.com/questions/32288049/how-to-set-full-page-
// background-image-of-a-div-that-changes-on-page-load

window.onload=function(){  
  var thediv=document.getElementById("hero-image");  
  var imgarray = new Array ("media/abyss-headphones-diana.jpg", "AP80-PRO-X-Red-Copper-Edition.jpg", "audeze-lcdi4.jpg", "audeze-mm500.jpg", "auris-audio-ha-2sf.jpg", "auris-ha-2se.jpg", "campfire-audio-solaris-SE.jpg", "cayin-c9-2.jpg", "cayin-ha-300mk2.jpg", "cayin-n8.jpg", "chord-electronics-mojo-2.jpg", "dan-clark-audio-expanse.jpg", "dCS-Bartok.jpg", "dekoni-audio-blue.jpg", "Denafrips-Ares-II.jpg", "earmen-angel.jpg", "earmen-ch-amp.jpg", "earmen-ch-amp.jpg", "empire-ears-odin.jpg", "feliks-audio-envy.jpg", "ferrum-erco.jpg", "fiio-m17.jpg", "final-d8000.jpg", "media/fir-audio-krypton.jpg", "formula-s-title.jpg", "gustard-x18.jpg", "hiby-r6-pro.jpg", "HiBy-R8.jpg", "hiby-rs8.jpg", "HIFIMAN-Sundara-Closed-Back.jpg", "hugo-title.jpg", "ibasso-dx240.jpg", "media/ibasso-dx300-max.jpg", "ifi-audio-GO-Bar.jpg", "media/ifi-audio-xdsd-gryphon.jpg", "ifi-audio-ZEN-Air.jpg", "IFI-AUDIO-ZEN-ONE.jpg", "iFi-Micro-iDSD-signature-series-2.jpg", "lime-ears-anima.jpg", "little-dot-VII.jpg", "lotoo-PAW-gold.jpg", "luxury-and-precision-p6-pro.jpg", "moondrop-void.jpg", "musician-audio-pegasus-r2r.jpg", "noble-audio-viking-ragnar.jpg", "noble-ausio-sultan.jpg", "sennheiser-ie600.jpg", "smsl-d-6.jpg", "topping-d10-balanced.jpg", "Violectric-DHA-V590.jpg", "vision-ears-ext.jpg", "Vision-Ears-Phonix.jpg", "xDuoo-MU-601.jpg", "zmf-headphones-atirum.jpg", "/workspace/awdioaber/media/zmf-headphones-caldera.jpg" );  
  var spot =Math.floor(Math.random()* imgarray.length);  
 console.
log(spot); thediv.style.background="url("+imgarray[spot]+")";
}
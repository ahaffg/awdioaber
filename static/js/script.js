function pic() {
    var bgm = ['abyss-headphones-diana', 'AP80-PRO-X-Red-Copper-Edition', 'Aroma-Audio-Jewel'];
 
    $('body').css({
        'background' : 'url('+ bgm[Math.floor(Math.random() * bgm.length)] + ') no-repeat',
    });
}
pic();
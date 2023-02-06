let shuffleImage = () => {
    if (easy === true) {
        let arrayOrder = getImages.slice(0, 12);
        arrayOrder.sort(() => Math.random() - 0.5);
        return arrayOrder;
    }
};       

let getImages = [{
    imgSrc: "./media/abyss-headphones-diana.jpg",
    name: "abyss-headphones-diana"
  }, {
    imgSrc: "./assets/images/sloth_1.png",
    name: "sloth_1"
  }, {
    imgSrc: "./assets/images/sloth_2.png",
    name: "sloth_2"
  }, {
    imgSrc: "./assets/images/sloth_2.png",
    name: "sloth_2"
  }, {
    imgSrc: "./assets/images/sloth_3.png",
    name: "sloth_3"
  }, {
    imgSrc: "./assets/images/sloth_3.png",
    name: "sloth_3"
  }, {
    imgSrc: "./assets/images/sloth_4.png",
    name: "sloth_4"
  }, {
    imgSrc: "./assets/images/sloth_4.png",
    name: "sloth_4"
  }, {
    imgSrc: "./assets/images/sloth_5.png",
    name: "sloth_5"
  }, {
    imgSrc: "./assets/images/sloth_5.png",
    name: "sloth_5"
  }, {
    imgSrc: "./assets/images/sloth_6.png",
    name: "sloth_6"
  }, {
    imgSrc: "./assets/images/sloth_6.png",
    name: "sloth_6"
  }, {
    imgSrc: "./assets/images/sloth_7.png",
    name: "sloth_7"
  }, {
    imgSrc: "./assets/images/sloth_7.png",
    name: "sloth_7"
  }, {
    imgSrc: "./assets/images/sloth_8.png",
    name: "sloth_8"
  }, {
    imgSrc: "./assets/images/sloth_8.png",
    name: "sloth_8"
  }, {
    imgSrc: "./assets/images/sloth_9.png",
    name: "sloth_9"
  }, {
    imgSrc: "./assets/images/sloth_9.png",
    name: "sloth_9"
  }, {
    imgSrc: "./assets/images/sloth_10.png",
    name: "sloth_10"
  }, {
    imgSrc: "./assets/images/sloth_10.png",
    name: "sloth_10"
  }, {
    imgSrc: "./assets/images/sloth_11.png",
    name: "sloth_11"
  }, {
    imgSrc: "./assets/images/sloth_11.png",
    name: "sloth_11"
  }, {
    imgSrc: "./assets/images/sloth_12.png",
    name: "sloth_12"
  }, {
    imgSrc: "./assets/images/sloth_12.png",
    name: "sloth_12"
  },
  ]
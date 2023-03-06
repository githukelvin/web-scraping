const popularFeeds = document.querySelector(".popular_feeds");

var xhr = new XMLHttpRequest();
xhr.open("GET", "jiji.json", true);

xhr.onload = function () {
  if (this.status == 200) {
    var jiji = JSON.parse(this.responseText);

    console.log(jiji[0])
    var output = "";
    for (var i in jiji) {
        const { price, image, Total_images, Title, anchor, location } = jiji[i];
      output += `
                <div class="pop">
                    <img src="${image}" alt="">
                    <div class="des">${Title}</div>
                    <h5 class="item_name">Address :${location}</h5>

                    <div>Price: ${price}</div>
                    <div class="des">${Total_images} images available</div>
                    <a class="not" href="${anchor}">view more</a>
                   
                </div>
            
            `;
    }
    popularFeeds.innerHTML = output;
  }
};
xhr.send();

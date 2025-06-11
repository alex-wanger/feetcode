fetch('../html/header.html')
  .then(res => res.text())
  .then(data => {
    document.getElementById('header-container').innerHTML = data;

    const links = document.querySelectorAll('.nav-links a, .auth-links a');
    const currentUrl = window.location.href;

    links.forEach(link => {
      if (link.href === currentUrl) {
        link.classList.add('active-link');
      }
    });
  });

fetch('../html/footer.html')
  .then(res => res.text())
  .then(data => {
    document.getElementById('footer-container').innerHTML = data;
  });
  

  const images = [
    { src: "../images/scatterplot.png", caption: "Scatter Plot" },
    { src: "../images/bargraph.png", caption: "Bar Graph" },
    { src: "../images/piechart.png", caption: "Pie Chart" }
  ];

  let currentIndex = 0;

  function updateCarousel() {
    const img = document.getElementById("carousel-img");
    const caption = document.getElementById("carousel-caption");

    img.src = images[currentIndex].src;
    img.alt = images[currentIndex].caption;
    caption.textContent = images[currentIndex].caption;
  }

  function nextImage() {
    currentIndex = (currentIndex + 1) % images.length;
    updateCarousel();
  }

  function prevImage() {
    currentIndex = (currentIndex - 1 + images.length) % images.length;
    updateCarousel();
  }

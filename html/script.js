fetch('../html/header.html')
  .then(res => res.text())
  .then(data => {
    document.getElementById('header-container').innerHTML = data;

    const links = document.querySelectorAll('.nav-links a');
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
  

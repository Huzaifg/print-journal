const viewer = document.querySelector('#photo-viewer');
const viewerImage = viewer.querySelector('img');
const viewerCaption = viewer.querySelector('p');
document.querySelectorAll('.print').forEach(entry => {
  const main = entry.querySelector('.main-photo');
  const mainImage = main.querySelector('img');
  const caption = entry.querySelector('.caption');
  entry.querySelectorAll('.thumbnail').forEach(button => {
    button.addEventListener('click', () => {
      mainImage.src = button.dataset.src;
      mainImage.alt = button.dataset.alt;
      caption.textContent = button.dataset.caption;
      entry.querySelectorAll('.thumbnail').forEach(item => item.setAttribute('aria-pressed', String(item === button)));
    });
  });
  main.addEventListener('click', () => {
    viewerImage.src = mainImage.src;
    viewerImage.alt = mainImage.alt;
    viewerCaption.textContent = caption.textContent;
    viewer.showModal();
  });
});
viewer.querySelector('.close-viewer').addEventListener('click', () => viewer.close());
viewer.addEventListener('click', event => {
  if (event.target === viewer) {
    const rect = viewer.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) viewer.close();
  }
});

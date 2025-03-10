document.addEventListener('DOMContentLoaded', () => {
  const container = document.querySelector('.table_container');
  const scrollAmount = (container.scrollWidth - container.clientWidth) / 2;
  container.scrollLeft = scrollAmount;
});
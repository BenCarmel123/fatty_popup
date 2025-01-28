document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const overlay = document.querySelector('.wrapper');

    overlay.style.display = 'none';

    function showDetails(event) {
        event.stopPropagation();
        const description = event.target.dataset.description;
        pop.textContent = description;
        overlay.style.display = 'flex';
        event.target.parentElement.open = false;
    }

    function closePop() {
        overlay.style.display = 'none';
        document.querySelectorAll('details').forEach(d => d.open = false);
    }

    arrow.forEach(summary => {
        summary.addEventListener('click', showDetails);
        summary.addEventListener('touchend', showDetails);
    });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });

    overlay.addEventListener('touchend', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });
});
document.addEventListener('DOMContentLoaded', () => {
    const summaries = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const overlay = document.querySelector('.wrapper');

    overlay.style.display = 'none';

    function showDetails(event) {
        event.preventDefault(); // Prevent default details toggle
        const description = event.target.dataset.description;
        pop.textContent = description;
        overlay.style.display = 'flex';
    }

    function closePop() {
        overlay.style.display = 'none';
        // Close all details elements
        document.querySelectorAll('details').forEach(detail => {
            detail.open = false;
        });
    }

    summaries.forEach(summary => {
        summary.parentElement.addEventListener('click', (e) => {
            e.preventDefault(); // Prevent details toggle
        });
        
        summary.addEventListener('click', showDetails);
        summary.addEventListener('touchstart', (e) => {
            e.preventDefault();
            showDetails(e);
        });
    });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });

    overlay.addEventListener('touchstart', (e) => {
        if (!detailsBlock.contains(e.target)) {
            e.preventDefault();
            closePop();
        }
    });
});
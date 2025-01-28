document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const overlay = document.querySelector('.wrapper');
    let isFirstLoad = true;

    overlay.style.display = 'none';

    function handleEvent(event) {
        if (!event.isTrusted || isFirstLoad) {
            isFirstLoad = false;
            return;
        }
        
        event.preventDefault();
        event.stopPropagation();
        
        const description = event.target.dataset.description;
        if (!description) return;
        
        pop.textContent = description;
        overlay.style.display = 'flex';
        event.target.parentElement.open = false;
    }

    function closePop() {
        overlay.style.display = 'none';
        document.querySelectorAll('details').forEach(d => d.open = false);
    }

    arrow.forEach(summary => {
        summary.addEventListener('click', handleEvent, {passive: false});
        summary.addEventListener('touchstart', handleEvent, {passive: false});
    });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });

    overlay.addEventListener('touchstart', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });
});
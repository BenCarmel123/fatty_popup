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
        document.body.style.overflow = 'hidden';
        event.target.parentElement.open = false;
    }

    function closePop() {
        overlay.style.display = 'none';
        document.body.style.overflow = '';
        document.querySelectorAll('details').forEach(d => d.open = false);
    }

    arrow.forEach(summary => {
        ['touchstart', 'click'].forEach(eventType => {
            summary.addEventListener(eventType, handleEvent, { passive: false });
        });
    });

    overlay.addEventListener('touchstart', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
            e.preventDefault();
        }
    });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });
});
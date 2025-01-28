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
        
        if (event.type === 'touchstart') {
            event.preventDefault();
            return;
        }
        
        const description = event.target.dataset.description;
        if (!description) return;
        
        pop.textContent = description;
        overlay.style.display = 'flex';
        document.body.setAttribute('style', 'position: fixed; width: 100%;');
        event.target.parentElement.open = false;
    }

    function closePop() {
        overlay.style.display = 'none';
        document.body.removeAttribute('style');
        document.querySelectorAll('details').forEach(d => d.open = false);
    }

    arrow.forEach(summary => {
        ['touchstart', 'touchend', 'click'].forEach(eventType => {
            summary.addEventListener(eventType, handleEvent);
        });
    });

    overlay.addEventListener('touchend', (e) => {
        if (!detailsBlock.contains(e.target)) closePop();
    });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) closePop();
    });
});
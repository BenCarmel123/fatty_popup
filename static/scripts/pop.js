document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const overlay = document.querySelector('.wrapper');
    let isFirstLoad = true;
    let touchStartY;

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
        document.documentElement.style.position = 'fixed';
        document.documentElement.style.width = '100%';
        event.target.parentElement.open = false;
    }

    function closePop() {
        overlay.style.display = 'none';
        document.documentElement.style.position = '';
        document.documentElement.style.width = '';
        document.querySelectorAll('details').forEach(d => d.open = false);
    }

    arrow.forEach(summary => {
        summary.addEventListener('touchend', handleEvent, { passive: false });
        summary.addEventListener('click', handleEvent, { passive: false });
    });

    overlay.addEventListener('touchmove', (e) => e.preventDefault(), { passive: false });
    
    overlay.addEventListener('touchend', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
            e.preventDefault();
        }
    }, { passive: false });

    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop();
        }
    });
});
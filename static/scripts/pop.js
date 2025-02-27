document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const resLinkContainer = document.querySelector('.event_link');
    const overlay = document.querySelector('.wrapper');

    overlay.style.display = 'none';

    function handleEvent(event) {
        if (!event.isTrusted) {
            return;
        }
        
        if (event.type === 'touchstart') {
            event.preventDefault();
            return;
        }
        
        const description = event.target.dataset.description;
        const resLink = event.target.dataset.reservation;
        
        if (!description) return;
        
        pop.textContent = description;
        
        if (resLink && resLink !== "None") {
            resLinkContainer.innerHTML = `<a href="${resLink}" target="_blank">להזמנת מקום</a>`;
            resLinkContainer.style.display = 'block';
        } else {
            resLinkContainer.style.display = 'none';
        }
        
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
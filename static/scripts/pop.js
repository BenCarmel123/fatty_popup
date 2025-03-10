document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.querySelector('.wrapper');
    overlay.style.display = 'none';
    const eventNames = document.querySelectorAll('summary p.event_name');
    const chefBlock = document.querySelector('.event_by')
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const resLinkContainer = document.querySelector('.event_link');
    const url = window.location.href;

    let scrollPosition = 0;

    function handleEvent(event) {
        if (!event.isTrusted) {
            return;
        }

        const targetElement = event.target;
        if (!targetElement.classList.contains('event_name')) {
            return;
        }

        if (event.type === 'touchend') {
            const rect = targetElement.getBoundingClientRect();
            
            const leftBoundary = rect.left + rect.width * 0.35;
            const rightBoundary = rect.left + rect.width * 0.65;
            const topBoundary = rect.top + rect.height * 0.35;
            const bottomBoundary = rect.top + rect.height * 0.65;
            
            const touchX = event.changedTouches[0].clientX;
            const touchY = event.changedTouches[0].clientY;
            
            if (touchX < leftBoundary || touchX > rightBoundary || 
                touchY < topBoundary || touchY > bottomBoundary) {
                event.preventDefault();
                event.stopPropagation();
                return;
            }
        }

        if (event.type === 'touchstart') {
            event.preventDefault();
            return;
        }

        scrollPosition = window.scrollY;

        const summaryElement = targetElement.closest('summary');
        const description = summaryElement.dataset.description;
        const resLink = summaryElement.dataset.reservation;
        const chef1 = summaryElement.dataset.chef1;
        const chef2 = summaryElement.dataset.chef2;
        const location = summaryElement.dataset.location;
        const host = summaryElement.dataset.host;

        pop.setAttribute('data-location', location);

        chefBlock.innerHTML = `<a href="https://www.instagram.com/${chef1}/" target="_blank" class="insta_link">@${chef1}</a>`;

        if (host) {
            chefBlock.innerHTML += ` | <a href="https://www.instagram.com/${host}/" target="_blank" class="insta_link">@${host}</a>`;
        }

        if (chef2) {
            chefBlock.innerHTML += ` | <a href="https://www.instagram.com/${chef2}/" target="_blank" class="insta_link">@${chef2}</a>`;
        }

        pop.textContent = description;

        if (resLink && resLink !== "None") {
            resLinkContainer.innerHTML = `<a href="${resLink}" target="_blank" class="insta_link" >להזמנת מקום</a>`;
            resLinkContainer.style.display = '';
        }
        else {
            resLinkContainer.style.display = 'none';
        }

        overlay.style.display = 'flex';
        document.body.style.position = 'fixed';
        document.body.style.top = `-${scrollPosition}px`;
        document.body.style.width = '100%';
        
        summaryElement.parentElement.open = false;
        
        event.stopPropagation();
    }

    function closePop() {
        overlay.style.display = 'none';
        document.body.removeAttribute('style');
        document.querySelectorAll('details').forEach(d => d.open = false);
        window.scrollTo({
            top: scrollPosition,
            behavior: 'instant'
        });
    }

    function shareWhatsApp() {
        const description = pop.textContent || '';
        window.open(`https://wa.me/?text=${encodeURIComponent(`${url}\n\n${description}`)}`, '_blank');
    }

    function openMaps() {
        const location = pop.getAttribute('data-location');
        window.open(`https://www.google.com/maps/search/${encodeURIComponent(location)}`, '_blank');
    }

    function copyToClipboard() {
        const description = pop.textContent || '';
        const shareText = `${url}\n\n${description}`;
        navigator.clipboard.writeText(shareText);
    }

    document.querySelectorAll('.share_container').forEach(container => {
        const whatsappButton = container.querySelector('.whatsapp');
        const linkButton = container.querySelector('.copy_link');
        const googleMaps = container.querySelector('.google_maps');

        if (whatsappButton) {
            whatsappButton.addEventListener('click', shareWhatsApp);
        }

        if (linkButton) {
            linkButton.addEventListener('click', copyToClipboard);
        }

        if (googleMaps) {
            googleMaps.addEventListener('click', openMaps);
        }
    });

    eventNames.forEach(eventName => {
        ['touchstart', 'touchend', 'click'].forEach(eventType => {
            eventName.addEventListener(eventType, handleEvent);
        });
    });

    document.querySelectorAll('summary').forEach(summary => {
        summary.addEventListener('click', function(e) {
            if (!e.target.classList.contains('event_name')) {
                e.preventDefault();
            }
        });
    });

    if (overlay && detailsBlock) {
        overlay.addEventListener('touchend', (e) => {
            if (!detailsBlock.contains(e.target)) closePop();
        });

        overlay.addEventListener('click', (e) => {
            if (!detailsBlock.contains(e.target)) closePop();
        });
    }
});
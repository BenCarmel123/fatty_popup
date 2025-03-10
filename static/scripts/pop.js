document.addEventListener('DOMContentLoaded', () => {
    const overlay = document.querySelector('.wrapper');
    overlay.style.display = 'none';
    const arrow = document.querySelectorAll('summary');
    const detailsBlock = document.querySelector('.event_details_container');
    const pop = document.querySelector('.event_details');
    const resLinkContainer = document.querySelector('.event_link');
    const url = window.location.href;

    let scrollPosition = 0;

    function handleEvent(event) {
        if (!event.isTrusted) {
            return;
        }

        if (event.type === 'touchstart') {
            event.preventDefault();
            return;
        }

        scrollPosition = window.scrollY;

        const description = event.target.dataset.description;
        const resLink = event.target.dataset.reservation;

        pop.textContent = description;

        if (resLink && resLink !== "None") {
            resLinkContainer.innerHTML = `<a href="${resLink}" target="_blank">להזמנת מקום</a>`;
            resLinkContainer.style.display = 'block';
        } else {
            resLinkContainer.style.display = 'none';
        }

        overlay.style.display = 'flex';
        document.body.style.position = 'fixed';
        document.body.style.top = `-${scrollPosition}px`;
        document.body.style.width = '100%';
        event.target.parentElement.open = false;
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

    function copyToClipboard() {
        const description = pop.textContent || '';
        const shareText = `${url}\n\n${description}`;
        navigator.clipboard.writeText(shareText);
    }

    document.querySelectorAll('.share_container').forEach(container => {
        const whatsappButton = container.querySelector('.whatsapp');
        const linkButton = container.querySelector('.copy_link');

        if (whatsappButton) {
            whatsappButton.addEventListener('click', shareWhatsApp);
        }

        if (linkButton) {
            linkButton.addEventListener('click', copyToClipboard);
        }
    });

    arrow.forEach(summary => {
        ['touchstart', 'touchend', 'click'].forEach(eventType => {
            summary.addEventListener(eventType, handleEvent);
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
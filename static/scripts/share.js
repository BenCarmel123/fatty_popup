document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.share_container').forEach(container => {
        const whatsapp = container.querySelector('.whatsapp');
        const facebook = container.querySelector('.facebook');
        const ig = container.querySelector('.instagram');
        const link = container.querySelector('.copy_link');

        const url = window.location.href;

        whatsapp.addEventListener('click', (event) => {
            const description = whatsapp.dataset.description || '';
            window.open(`https://wa.me/?text=${encodeURIComponent(`${url}\n\n${description}`)}`, '_blank');
        });

        facebook.addEventListener('click', (event) => {
            const description = facebook.dataset.description || '';
            window.open(`https://www.messenger.com/share?link=${encodeURIComponent(url)}&quote=${encodeURIComponent(description)}`, '_blank');
        });

        ig.addEventListener('click', (event) => {
            const description = ig.dataset.description || '';
            const shareText = `${url}\n\n${description}`;
            navigator.clipboard.writeText(shareText).then(() => {
                alert('Link and description copied to clipboard!');
            });
        });

        link.addEventListener('click', (event) => {
            const description = link.dataset.description || '';
            const shareText = `${url}\n\n${description}`;
            navigator.clipboard.writeText(shareText).then(() => {
                alert('Link and description copied to clipboard!');
            });
        });
    });
});
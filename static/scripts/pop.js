document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary'); // Select all summary elements
    const detailsBlock = document.querySelector('.event_details_container'); // Details container
    const pop = document.querySelector('.event_details'); // Description placeholder
    const overlay = document.querySelector('.wrapper'); // Wrapper as overlay

    // Initially hide the overlay and details container
    overlay.style.display = 'none';

    // Function to show the details popup
    function showDetails(event) {
        const description = event.target.dataset.description; // Get description
        pop.textContent = description; // Set description text
        overlay.style.display = 'flex'; // Show the overlay and popup
    }

    // Function to close the popup
    function closePop() {
        overlay.style.display = 'none'; // Hide the overlay and popup
    }

    // Add event listeners to each summary element
    arrow.forEach(summary => {
        summary.addEventListener('click', showDetails);
        summary.addEventListener('touchstart', showDetails); // Support for touch devices
    });

    // Add event listener to the overlay to close the popup
    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop(); // Close only if clicked outside the container
        }
    });

    overlay.addEventListener('touchstart', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop(); // Close only if touch is outside the container
        }
    });
});

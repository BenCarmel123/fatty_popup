document.addEventListener('DOMContentLoaded', () => {
    const arrow = document.querySelectorAll('summary'); // Select all summary elements
    const detailsBlock = document.querySelector('.event_details_container'); // Details container
    const pop = document.querySelector('.event_details'); // Description placeholder
    const overlay = document.querySelector('.wrapper'); // Wrapper as overlay

    // Initially hide the overlay and details container
    overlay.style.display = 'none';

    // Function to show the details popup
    function showDetails(clickEvent) {
        const description = clickEvent.target.dataset.description; // Get description
        pop.textContent = description; // Set description text
        overlay.style.display = 'flex'; // Show the overlay and popup
    }

    // Function to close the popup
    function closePop() {
        overlay.style.display = 'none'; // Hide the overlay and popup
    }

    // Add click listener to each summary element
    arrow.forEach(summary => {
        summary.addEventListener('click', showDetails);
    });

    // Add click listener to the overlay (to close the popup)
    overlay.addEventListener('click', (e) => {
        if (!detailsBlock.contains(e.target)) {
            closePop(); // Close only if clicked outside the container
        }
    });
});

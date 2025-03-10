document.addEventListener('DOMContentLoaded', () => {
    const cells = document.querySelectorAll(".dates");
    
    cells.forEach(cell => {
        cell.addEventListener('click', () => {
            let dateStr = cell.dataset.start;
            const endDateStr = cell.dataset.end;
            const eventName = cell.dataset.name || "Pop Up";
            const location = cell.dataset.location || "Tel Aviv";
            
            const now = new Date();
            const startDate = new Date(dateStr);
            
            if (startDate < now && endDateStr) {
                dateStr = endDateStr;
            }
            
            const date = new Date(dateStr);
            date.setHours(18, 0, 0, 0);
            
            const endDate = new Date(date);
            endDate.setHours(endDate.getHours() + 2);
            
            const startFormatted = date.toISOString().replace(/-|:|\.\d+/g, "");
            const endFormatted = endDate.toISOString().replace(/-|:|\.\d+/g, "");
            
            const calendarUrl = `https://calendar.google.com/calendar/render?action=TEMPLATE` + 
                `&text=${encodeURIComponent(eventName)}` + 
                `&dates=${startFormatted}/${endFormatted}` + 
                `&location=${encodeURIComponent(location)}`;
            
            window.open(calendarUrl);
        });
    });
 });
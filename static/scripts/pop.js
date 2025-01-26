document.addEventListener('DOMContentLoaded', () =>
{
   const arrow = document.querySelectorAll('summary');
   const detailsBlock = document.querySelector('.event_details_container');
   const pop = document.querySelector('.event_details');
   const close = document.getElementById('close_pop');
   detailsBlock.style.display = 'none';
   function showDetails(clickEvent)
   {
       const description = clickEvent.target.dataset.description;
       pop.textContent = description;
       detailsBlock.style.display = 'block';
   }
    function closePop()
    {
        detailsBlock.style.display = 'none';
    }
    for (let i = 0; i < arrow.length; i++)
    {
        arrow[i].addEventListener('click', showDetails);
    }
    close.addEventListener('click', closePop);
});




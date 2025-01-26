document.addEventListener('DOMContentLoaded', () =>
{
   const popUp = document.getElementById('pop_event_details');
    popUp.style.display = 'none';   
   const popButton = document.getElementById('event_details');
   popButton.addEventListener('hover', () =>
   {
       popUp.style.display = 'block';
   });
    popUp.addEventListener('hover', () =>
    {
         popUp.style.display = 'none';
    });

});
document.addEventListener('DOMContentLoaded', () =>
{
   const popUp = document.getElementsByClassName('pop_event_details');
    popUp.style.display = 'none';   
   const popButton = document.getElementsByClassName('event_details');
   popButton.addEventListener('click', () =>
   {
       popUp.style.display = 'block';
   });
    popUp.addEventListener('click', () =>
    {
         popUp.style.display = 'none';
    });

});
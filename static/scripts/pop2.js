document.addEventListener('DOMContentLoaded', () =>
    {
       const txt = "I'm in for ...";
       var i = 0;
       const speed=10;
       function typeHeader() {
        if (i<txt.length) {
            var currentChar= txt.charAt(i)
            document.getElementById("mood").innerHTML += currentChar;
            i++;
            let randomDelay = speed + Math.random() * 20;
            if (currentChar == ' ')
            {
                randomDelay *=1.3;
            }
            setTimeout(typeHeader,randomDelay);
        }
       }
       setTimeout(typeHeader, 200);
    });

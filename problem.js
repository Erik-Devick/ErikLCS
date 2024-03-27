function search_problem() { 
    let input = document.getElementById('searchbar').value 
    input=input.toLowerCase(); 
    let x = document.getElementsByClassName('problems'); 
      
    for (i = 0; i < x.length; i++) {  
        if (!x[i].innerHTML.toLowerCase().includes(input)) { 
            x[i].style.display="none"; 
        } 
        else { 
            x[i].style.display="list-item";                  
        } 
    } 
} 

function unhide (){
    style(document).ready
    var hid = ("div.exp")
         if (true) hid.css("visibility",hidden);
           hid({
           visibility:visible
           });
    }
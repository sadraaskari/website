function showDiv(d  , numOfDivs){
		alert(d);
		for(var i = 1 ; i<= numOfDivs ; i++){
			var divBlocked = document.getElementById("d" + i);
			if(divBlocked.style.display == "none"){
				/*nothing*/
			   }else{
                   divBlocked.style.display = "none";
               }
		}
		alert("fdkdfjdf");
		var divOnClicked = document.getElementById("d" + d);
		divOnClicked.style.display = "block";
		
	}
    function test(){
        alert("hello guys!!");
    }
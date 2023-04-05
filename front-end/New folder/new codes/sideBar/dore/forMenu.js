function showDiv(d){
		for(var i = 1 ; i<= 4 ; i++){
			var divBlocked = document.getElementById("d" + i);
			if(divBlocked.style.display == "none"){
				/*nothing*/
			   }else{
                   divBlocked.style.display = "none";
               }
		}
		var divOnClicked = document.getElementById("d" + d);
		divOnClicked.style.display = "block";
		
	}
    function test(){
        alert("hello guys!!");
    }
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
function trash(numOfRow){
	var divRow = document.getElementById("tr" + numOfRow);
	//divRow.style.display = "none";
	let t = confirm("آیا میخواهید ردیف شماره"+numOfRow+"را حذف کنید؟");
	if(t == true){
		divRow.style.display = "none";
	}
}
function add(numOfRow){
	var divRow = document.getElementById("tr" + numOfRow);
	//divRow.style.display = "none";
	
		   divRow.style.backgroundColor = "#1F65E0";
	divRow.style.color = "white";
	   
}
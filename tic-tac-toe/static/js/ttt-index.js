// Initialize some variables
var gameGrid = [[0,0,0],[0,0,0],[0,0,0]];
var highPriWin = [[0,"O","O"],["O",0,"O"],["O","O",0]];
var highPriBlock = [[0,"X","X"],["X",0,"X"],["X","X",0]];
var gameState = 0;
var gameAttempts = 0;

var xImg = "static/imgs/cross-sm.png";
var oImg = "static/imgs/circle-tick-sm.png";
var blankImg = "static/imgs/blank-dark.png";

//returns the gameGrid X index for given div
function xIndex(squareDiv) {
	var x = squareDiv.split("_");
	var i = parseInt(x[1]);
	return i;
}

//returns the gameGrid Y index for given div
function yIndex(squareDiv) {
	var x = squareDiv.split("_");
	var i = parseInt(x[2]);
	return i;
}

//creates 3 rows of 3 divs, names and applies classes
function createGame() {
	for (var i=0; i<3; i++) {
		var rowDiv = document.createElement("div");
		rowDiv.classList.add("row");
		
		for (var j=0; j<3; j++) {
			var gridDiv = document.createElement("div");
			gridDiv.id = "square_" + i +"_"+ j;
			gridDiv.classList.add("col-lg-4");
			gridDiv.classList.add("col-sm-4");
			gridDiv.classList.add("col-4");
			gridDiv.classList.add("blank");
			$('<img/>').attr('src',blankImg).addClass('img-responsive').appendTo(gridDiv);
			rowDiv.appendChild(gridDiv);
		}
		
		document.getElementById("gamezone").appendChild(rowDiv);
		if (i<2) {
			$("<br>").appendTo(document.getElementById("gamezone"));
		}
	}
}

//resets gameGrid and gameState, clears gamezone, and calls createGame
function resetGame(){
	gameGrid = [[0,0,0],[0,0,0],[0,0,0]];
	gameState = 0;
	document.getElementById("gamezone").innerHTML = '';
	createGame();
}

// increments game attempt counter, resets if given "reset" as argument
function countrIncrmt(condition){
  if (condition == "reset"){
		gameAttempts = 1;
	}	else {
		gameAttempts++;
	}
	var counters = document.getElementsByClassName("counter")
	for (var i=0; i<counters.length; i++){
		var count = counters[i];
		count.innerHTML = gameAttempts;
	}
}

//jQuery to create game on page load and capture clicks
$(document).ready(function(){
	createGame();	
	countrIncrmt();

	$(document).on("mousedown", ".blank", function(){
		if ($(this).hasClass("blank")){
			if (gameState == 0){
				this.classList.remove("blank");
				this.classList.add("X");
				$(this).children("img").attr('src',xImg);
				gameGrid[xIndex(this.id)][yIndex(this.id)] = "X";
				gameOver();
				if (gameState == 0) {
					computerTurn();
					gameOver();
				}
			}
		}
	})
	$("#drawModal").on('hide.bs.modal', function(){
			countrIncrmt();
	});
	$("#winModal").on('hide.bs.modal', function(){
		countrIncrmt("reset");
	});
	$("#loseModal").on('hide.bs.modal', function(){
		countrIncrmt();
	});

	$(".btn-reset").click(function(){
		resetGame();
	})

	$(".btn-reset-user").click(function(){
		countrIncrmt();
		resetGame();
	})
});
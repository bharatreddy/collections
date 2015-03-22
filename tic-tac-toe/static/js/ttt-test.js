// Initialize some variables
var gameGrid = [[0,0,0],[0,0,0],[0,0,0]];
var highPriWin = [[0,"O","O"],["O",0,"O"],["O","O",0]];
var highPriBlock = [[0,"X","X"],["X",0,"X"],["X","X",0]];
var gameState = 0;
var gameAttempts = 0;

var xImg = "static/imgs/cross-sm.png";
var oImg = "static/imgs/circle-tick-sm.png";
var blankImg = "static/imgs/blank-dark.png";

//compares two arrays, returns true if they match
function compare(a,b) {
	if (a === b) {
		return true;
	}
	if (a == null || b == null) {
		return false;
	}
  if (a.length != b.length) {
  	return false;
  }
  for (var i=0; i<a.length; i++) {
  	if (a[i] !== b[i]) return false;
  }
 	return true;
}

//get the next move from minimax algo in .
function getNextMove() {
	//checks gameGrid against passed in array
	function arrayCheck(toCheck){
		for (var i=0; i<3; i++){
			//initialize counter arrays
			if (i == 0){
			var diag1 = [];
			var diag2 = [];
			}
			var check1 = [];
			var check2 = [];
			//fill diag arrays with grid variables
			diag1[i] = gameGrid[i][i];			
			diag2[i] = gameGrid[i][2-i];
			//check for move in diag
			if (i == 2) {
				var array = [];
				for (var k=0; k<toCheck.length; k++){					
					array = toCheck[k];
					if (compare(diag1,array)){	
						computerMove(diag1.indexOf(0), diag1.indexOf(0));
						return true;
					} else if (compare(diag2,array)){
						computerMove(diag2.indexOf(0), (2-diag2.indexOf(0)));
						return true;
					}
				}
			}
			// check for moves in rows and columns		
			for (var j=0; j<3; j++){
				check1[j] = gameGrid[i][j];
				check2[j] = gameGrid[j][i];
				if (j == 2){
					var array = [];
					for (var k=0; k<toCheck.length; k++){					
						array = toCheck[k];
						if (compare(check1,array)){	
							computerMove(i, check1.indexOf(0));
							return true;
						} else if (compare(check2,array)){
							computerMove(check2.indexOf(0), i);
							return true;
						}
					}
				}		
			}
		}
		return false;
	}
	//check for potential win
	if (arrayCheck(highPriWin)){
		return;
	}
	//check for potential block
	if (arrayCheck(highPriBlock)){
		return;
	}
	//play in the middle if available
	if (gameGrid[1][1] == 0){
		computerMove(1,1);
		return;
	}
	// LOW PRIORITY MOVE - plays around human player. currently assumes human goes first
	var played = true;
  do {
		var a = Math.round(2*Math.random())
		var b = Math.round(2*Math.random())
		if (gameGrid[a][b] == 0){
			computerMove(a,b);
			played = false;
		}
	}	while (played);
	return;	
}

// places an O in the grid array and changes div class to .X for given index
function computerMove(i,j) {
	gameGrid[i][j] = "O";
	var divName = "square_"+i+"_"+j;
	console.log(divName);
	$("#"+divName).children("img").attr('src',xImg);
	document.getElementById(divName).classList.remove("blank");
	document.getElementById(divName).classList.add("X");	
}

// checks for win condition and displays modal
function gameOver() {
	//check for draw
	var flatArray = gameGrid[0].concat(gameGrid[1],gameGrid[2]);
	console.log(flatArray);
	if (flatArray.indexOf(0) == -1) {
		gameState = 1;
		$('#drawModal').modal('show');
	}
	//check for win
	//initialize diag counters 
	var diag1X = 0;
	var diag1O = 0;
	var diag2X = 0;
	var diag2O = 0;
	// row and column checks
	for (var i=0; i<3; i++){
		//counter initialize
		var rowX = 0;
		var rowO = 0;
		var colX = 0;		
		var colO = 0;		
		//check diagonals
		if (gameGrid[i][i] == "X") {
			diag1X++;			
		} else if (gameGrid[i][i] == "O") {
			diag1O++;
		}	if (gameGrid[i][(2-i)] == "X") {
			diag2X++;
		}	else if (gameGrid[i][(2-i)] == "O") {
			diag2O++;
		} if (i == 2) {					
			if (diag1X == 3 || diag2X == 3) {
				gameState = 1;
				$('#winModal').modal('show');
			}
			else if (diag1O == 3 || diag2O == 3) {
				gameState = 1;
				$('#loseModal').modal('show');
			}
		}
		// count and check rows and columns for win
		for (var j=0; j<3; j++) {
			if (gameGrid[i][j] == "X") {
				rowX++;				
			}	else if (gameGrid[i][j] == "O") {
				rowO++;
			}	if (gameGrid[j][i] == "X") {
				colX++;				
			}	else if (gameGrid[j][i] == "O") {
				colO++; 					
			} if (j==2) {					
				if (rowX == 3 || colX == 3) {
					gameState = 1;
					$('#winModal').modal('show');
				} else if (rowO == 3 || colO == 3) {
					gameState = 1;
					$('#loseModal').modal('show');
				}
			}
		}	
	}
}

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
function incrementCounter(condition){
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

//jQuery to create gaem on page load and capture clicks
$(document).ready(function(){
	createGame();	
	incrementCounter();

	$(document).on("mousedown", ".blank", function(){
		if ($(this).hasClass("blank")){
			if (gameState == 0){
				this.classList.remove("blank");
				this.classList.add("X");
				$(this).children("img").attr('src',oImg);
				gameGrid[xIndex(this.id)][yIndex(this.id)] = "X";
				gameOver();
				if (gameState == 0) {
					getNextMove();
					gameOver();
				}
			}
		}
	})
	$("#drawModal").on('hide.bs.modal', function(){
			incrementCounter();
	});
	$("#winModal").on('hide.bs.modal', function(){
		incrementCounter("reset");
	});
	$("#loseModal").on('hide.bs.modal', function(){
		incrementCounter();
	});

	$(".btn-reset").click(function(){
		resetGame();
	})

	$(".btn-reset-user").click(function(){
		incrementCounter();
		resetGame();
	})
});
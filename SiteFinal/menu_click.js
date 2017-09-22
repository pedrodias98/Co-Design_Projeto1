function menu_change (){
  if (document.getElementById("demo").innerHTML === "Menu") {
    document.getElementById("demo").innerHTML = "Matteo I. ";
    document.getElementById("demo1").innerHTML = "Pedro V. ";
    document.getElementById("demo2").innerHTML = "Jhow. ";
    document.getElementById("demo3").innerHTML = "Alegro. ";
  }
  else {
    document.getElementById("demo").innerHTML = "Menu";
    document.getElementById("demo1").innerHTML = "";
    document.getElementById("demo2").innerHTML = "";
    document.getElementById("demo3").innerHTML = "";
  };
};

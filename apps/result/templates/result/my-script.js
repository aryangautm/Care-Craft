function identifRandom() {
    // *.querySelector, *.querySelectorAll take as parameter a CSS selector.
    // hence here You're missing a dot. The class is .identifiantRandom.
    let columnNumber = document.querySelectorAll('.identifiantRandom'); // This is a list of HTML (DOM) elements
    for (let i = 0; i < columnNumber.length; i++) {
       // But here, You're not accessing any of the DOM elements.
      //  let nombreIdentifiant = Math.floor((Math.random() * 100) + 1);
      let bools;
      if ( Math.random() > .5 ){
        bools[i] = true;
      } 
      else {
        bools[i] = false;  
      }
      console.log(bools);
      columnNumber[i].innerText = bools;
    }
}
identifRandom();
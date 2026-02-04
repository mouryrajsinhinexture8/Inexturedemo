//problem: Reverse all Word in a one by one
//without using generic functions like reverse(), split(), map()
function reverseWord(str) {
  let reversed = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }
  return reversed;
}

function word(sentence) {
  let result = [];
  let currentWord = "";

  //iterate through each one
  for (let i = 0; i < sentence.length; i++) {
    let char = sentence[i];

    if (char !== " ") {
      currentWord += char;
    } else {
      if (currentWord) {
        result.push(reverseWord(currentWord));
        currentWord = "";
      }
      result.push(" ");
    }
  }

  //add the last word if it there
  if (currentWord) {
    result.push(reverseWord(currentWord));
  }

  //array into string
  let finalResult = "";
  for (let i = 0; i < result.length; i++) {
    finalResult += result[i];
  }

  return finalResult;
}

// Test cases
console.log(word("Mouryraj")); 
console.log(word("Inexture")); 
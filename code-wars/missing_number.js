// https://www.codewars.com/kata/return-the-missing-element/train/javascript


function getMissingElement(superImportantArray){
  superImportantArray.sort();
  for (let i in superImportantArray) {
    if (superImportantArray[i] !== i) {
      return parseInt(i);
    }
  }
}
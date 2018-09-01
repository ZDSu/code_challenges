// https://www.hackerrank.com/challenges/js10-loops/problem


function vowelsAndConsonants(s) {
    let vowels = []
    let consonants = []
    
    for (let each of s) {
        if ('aeiou'.includes(each)) {
            vowels.push(each)
        }
        else {
            consonants.push(each)
        }
    }
    
    for (let each of vowels) {
        console.log(each)
    }
    for (let each of consonants) {
        console.log(each)
    }
}
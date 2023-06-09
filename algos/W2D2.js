/* 
  Given a string,
  return a new string with the duplicate characters excluded
  Bonus: Keep only the last instance of each character.
*/

const str1 = "abcABCabcABCabcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

//bonus
const str5 = "aba"
const expected5 = "ba" // ab

/**
 * De-dupes the given string.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str A string that may contain duplicates.
 * @returns {string} The given string with any duplicate characters removed.
 */
function stringDedupe(str) {
    //Your code here
}

console.log(stringDedupe(str1));
console.log(stringDedupe(str2));
console.log(stringDedupe(str3));
console.log(stringDedupe(str4));
console.log(stringDedupe(str5));



function stringDedupe(str = "") {
    let distinctStr = "";
    const seen = {};

    // loop backwards to include last occurrence
    for (let i = str.length - 1; i >= 0; --i) {
        if (!seen.hasOwnProperty(str[i])) {
            distinctStr = str[i] + distinctStr;
            seen[str[i]] = true;
        }
    }

    return distinctStr;
}

// associative array
function stringDedupe(str) {
    let temp =[]
    for (let i = str.length-1; i >= 0; i--){
        temp[str[i]] = str[i]
    }
    // console.log(temp)
    let result = Object.values(temp)
    return result.reverse().join('')
}
/* 
  String: Reverse
  Given a string,
  return a new string that is the given string reversed
*/

const str1 = "creature";
const expected1 = "erutaerc";

const str2 = "dog";
const expected2 = "god";

const str3 = "hello";
const expected3 = "olleh";

const str4 = "";
const expected4 = "";

/**
 * Reverses the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str String to be reversed.
 * @returns {string} The given str reversed.
 */
function reverseString(str) {
    //your code here
}

//TEST CODE FOR REVERSE
console.log(reverseString(str1)) // Expected: erutaerc
console.log(reverseString(str2)) // Expected: god
console.log(reverseString(str3)) // Expected: olleh
console.log(reverseString(str4)) // Expected: ""

// try to do it without any built in methods!
// try to do it looping forwards only!


function reverseString(str) {
  if (str.length < 2) {
      return str;
  }
  let result = '';
  for (let i = 0; i < str.length; i++) {
       result += str[str.length-1 - i];       // the same as result = result + foo
  }

  /*
  Spencer's suggestion
  for (let k = 0; k< str.length-1; k++) {
      result = str[k] + result                // this is result = foo + result
  }
   */
  return result;
}
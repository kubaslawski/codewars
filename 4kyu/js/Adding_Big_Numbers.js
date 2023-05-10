/*
e need to sum big numbers and we require your help.

Write a function that returns the sum of two numbers. The input numbers are strings and the function must return a string.

Example
add("123", "321"); -> "444"
add("11", "99");   -> "110"
Notes
The input numbers are big.
The input is a string of only digits
The numbers are positives
 */

const reverseString = (string) => {
    return string.split('').reverse().join('');
}

const addToString = (str, n) => {
  for (let i = 0; i < n; i++) {
    str += '0'
  }
  return str
}

const add = (a, b) => {
    let num1 = reverseString(a);
    let num2 = reverseString(b);
    if (num1.length > num2.length) {
        num2 = addToString(num2, (num1.length - num2.length))
    } else if (num2.length > num1.length) {
        num1 = addToString(num1, (num2.length - num1.length))
    }

    let res = 0;
    let num3 = '';
    for(let i=0; i<num1.length; i++){
        let n1 = parseInt(num1[i]);
        let n2 = parseInt(num2[i]);
        num3 += ((n1 + n2 + res) % 10).toString();
        // console.log(n1, n2)
        res = Math.floor((n1 + n2 + res) / 10);
        // console.log(res)
    }
    if(res > 0){
        num3 += res.toString();
        return reverseString(num3);
    } else {
        return reverseString(num3)
    }
}
/*
DESCRIPTION:
John has invited some friends. His list is:

s = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill";
Could you make a program that

makes this string uppercase
gives it sorted in alphabetical order by last name.
When the last names are the same, sort them by first name. Last name and first name of a guest come in the result between parentheses separated by a comma.

So the result of function meeting(s) will be:

"(CORWILL, ALFRED)(CORWILL, FRED)(CORWILL, RAPHAEL)(CORWILL, WILFRED)(TORNBULL, BARNEY)(TORNBULL, BETTY)(TORNBULL, BJON)"
It can happen that in two distinct families with the same family name two people have the same first name too.

Notes
You can see another examples in the "Sample tests".
 */

const meeting = (s) => {
    let arr = s.split(";").map((x) => x.toUpperCase().split(":"));
    arr.sort((a, b) => {
        if (a[1] === b[1]) {
            return a[0] < b[0] ? -1 : 1;
        }
        return a[1] < b[1] ? -1 : 1;
    });
    let str = "";
    for (let i = 0; i < arr.length; i++) {
        str += `(${arr[i][1]}, ${arr[i][0]})`
    }
    return str
}

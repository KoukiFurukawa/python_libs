"use strict";

const Main = arg => {
    const input = arg.trim().split(" ");
    const a = parseInt(input[0]);
    const b = parseInt(input[1]);
    if (a*6 >= b && b >= a) {
        console.log("Yes");
    }else{
        console.log("No");
    }
}
Main(require("fs").readFileSync("/dev/stdin","utf8"));
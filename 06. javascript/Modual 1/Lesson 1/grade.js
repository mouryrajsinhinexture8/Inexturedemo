const prompt = require("prompt-sync")();

function subject(html, database, javascript) {
    let average = (html + database + javascript) / 3;

    if (average >= 80) {
        grade = "A";
    } else if (average >= 60) {
        grade = "B";
    } else if (average >= 40) {
        grade = "C";
    } else{
        grade = "Fail";
    }
    console.log("Average:",average.toFixed(2));
    console.log("Grade:",grade);
}

let html = Number(prompt("Enter html marks: "));
let database = Number(prompt("Enter database marks: "));
let javascript = Number(prompt("Enter javascript marks: "));

subject(html, database, javascript);

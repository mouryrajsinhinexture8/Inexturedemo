let employees = [
    { name: "Jadeja", salary: 45000, department: "it" },
    { name: "Zala", salary: 60000, department: "hr" },
    { name: "Abjydeep", salary: 75000, department: "finance" },
    { name: "fenil", salary: 50000, department: "it" },
    { name: "Dhruv", salary: 90000, department: "management" }
];

let highEarners = employees.filter(emp => emp.salary > 50000);
console.log("Employees earning more than 50,000:", highEarners);

let totalSalary = employees.reduce((sum, emp) => sum + emp.salary, 0);
console.log("Total Salary of All Employees:", totalSalary);

employees.forEach(emp => {
    let { name, salary, department } = emp;
    console.log(`Name: ${name}, Salary: ${salary}, Department: ${department}`);
});

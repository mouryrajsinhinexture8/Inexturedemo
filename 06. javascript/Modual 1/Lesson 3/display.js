// user object
const user = {
  name: "Rahul",
  age: 22,
  role: "Student"
};

//arrow function + destructuring + template literal
const showUserProfile=({name,age,role})=> 
  {
  console.log(`User Profile:-
Name:-${name}
Age:-${age}
Role:-${role}`);
};

//call function
showUserProfile(user);

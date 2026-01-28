let cart = [
    { Name: "Laptop", price: 50000, quantity: 1 },
    { Name: "Headphones", price: 2000, quantity: 2 },
    { Name: "Mouse", price: 800, quantity: 1 }
];

let total = cart.reduce((sum, item) => {
    return sum + (item.price * item.quantity);
}, 0);

console.log("Total amount:" + total);
let newItem = { Name: "Keyboard", price: 1500, quantity: 1 };

let updatedCart = [...cart, newItem];

console.log("\nUpdated Shopping Cart:");
updatedCart.forEach(item => {
    let { Name, price, quantity } = item;
    console.log(`Item: ${Name}, Price: ${price}, Quantity: ${quantity}`);
});

class product {
  constructor(name, price) {
    this.name = name;
    this.price = price;
  }

  getDetails() {
    return `Product:- ${this.name},Price:- ${this.price}`;
  }
}

//create product objects
const products = [
  new product("Laptop", 55000),
  new product("Mobile", 18000),
  new product("Tablet", 25000),
  new product("Headphones", 5000),
];

//display products in one
products.forEach((product) => console.log(product.getDetails()));

// const {Operaciones} = require("./mi_lib");
const milib = require("./mi_lib.js");

const lista1 = [2, 3, 4];
const num_a_sumar = 2;

let resultado = milib.Operaciones.suma(lista1);
console.log(resultado);

resultado = milib.Operaciones.suma(lista1, num_a_sumar);
console.log(resultado);


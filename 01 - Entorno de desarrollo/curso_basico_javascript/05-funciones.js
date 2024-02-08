// Definición de funcinoes
function saludar() {
    console.log('Hola Mundo');
}
saludar();

function saludar2(nombre) {
    console.log('Hola ' + nombre);
}
saludar2('Carlos');

function sumar(a, b) {
    return a + b;
}
let resultado = sumar(1, 2);
console.log(resultado);

function sumar2(a, b) {
    console.log(arguments);
    return a + b;
}
resultado = sumar2(1, 2);
console.log(resultado);

function sumar3(a, b) {
    if (typeof a !== 'number' || typeof b !== 'number') {
        console.error('Los argumentos deben ser números');
        return;
    }
    return a + b;
}
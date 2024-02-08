class NombreDeMiClase {
    constructor(atributo_1, atributo_2) {
        this.atributo_1 = atributo_1;
        this.atributo_2 = atributo_2;
    }
    metodo_1() {
        console.log(`Hola, el valor de attr1 es: ${this.atributo_1} y el valor de attr2 es: ${this.atributo_2}`);
    }


}

let mi_objeto = new NombreDeMiClase("Valor atributo_1", "Valor atributo_1");
mi_objeto.metodo_1();


class NombreDeMiClase {
    constructor(atributo_1, atributo_2) {
        // Dentro de paréntesis se coloca la referencia a la instancia y los argumentos necesarios para la creación de la misma
        console.log("Constructor")
        this.atributo_1 = atributo_1; // this hace referencia a la instancia de la clase
        this.atributo_2 = atributo_2;
    }
    metodo_1() {
        console.log(`Hola, el valor de attr1 es: ${this.atributo_1} y el valor de attr2 es: ${this.atributo_2}`);
    }
}

let mi_objeto = new NombreDeMiClase("Valor atributo_1", "Valor atributo_1"); // En esta línea se instancia la clase
mi_objeto.metodo_1();

class NombreDeSubclase extends NombreDeMiClase{
    constructor(atributo_1, atributo_2) {
        this.atributo_1 = atributo_1;
        this.atributo_2 = atributo_2;
    }
    metodo_1() {
        console.log(`Hola, este método sobreescribe al metodo de la clase base`);
    }
}



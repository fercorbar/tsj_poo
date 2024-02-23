class Operaciones {
    constructor() {}

    static suma(lista, num = null) {
        if (num) {
            let result = [];
            for (let element of lista) {
            result.push(element + num);
            }
            return result;
        } else {
            let result = 0;
            for (let element of lista) {
            result += element;
            }
            return result;
        }
    }
}

module.exports = {
    Operaciones: Operaciones
};


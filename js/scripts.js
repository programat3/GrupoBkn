//API ropa
fetch('https://fakestoreapi.com/products')
    .then(response => response.json())
    .then(products => {
        const cardsContainer = document.getElementById('cards-ropa');

        products.forEach(product => {
            const card = document.createElement('div');
            card.classList.add('card');
            card.setAttribute('id', 'cardRopa');

            const img = document.createElement('img');
            img.src = product.image;
            img.alt = product.title;
            card.appendChild(img);

            const title = document.createElement('h4');
            title.textContent = product.title;
            card.appendChild(title);

            const price = document.createElement('p');
            price.textContent = `$${product.price.toFixed(2)}`;
            card.appendChild(price);
        });
    });



//Validador formulario de registro
    $(document).ready(function () {

    // Agregar método de validación para RUT chileno
    $.validator.addMethod("rutChileno", function (value, element) {
        // Eliminar puntos y guión del RUT
        value = value.replace(/[.-]/g, "");

        // Validar que el RUT tenga 8 o 9 dígitos
        if (value.length < 8 || value.length > 9) {
            return false;
        }

        // Validar que el último dígito sea un número o una 'K'
        var validChars = "0123456789K";
        var lastChar = value.charAt(value.length - 1).toUpperCase();
        if (validChars.indexOf(lastChar) == -1) {
            return false;
        }

        // Calcular el dígito verificador
        var rut = parseInt(value.slice(0, -1), 10);
        var factor = 2;
        var sum = 0;
        var digit;
        while (rut > 0) {
            digit = rut % 10;
            sum += digit * factor;
            rut = Math.floor(rut / 10);
            factor = factor === 7 ? 2 : factor + 1;
        }
        var dv = 11 - (sum % 11);
        dv = dv === 11 ? "0" : dv === 10 ? "K" : dv.toString();

        // Validar que el dígito verificador sea correcto
        return dv === lastChar;
    }, "Por favor ingrese un RUT válido.");

    $("#formregistro").validate({
        rules: {
            rut: {
                required: true,
                rutChileno: true,
            },
            nombres: {
                required: true,
            },
            apellidos: {
                required: true,
            },
            email: {
                required: true,
                email: true,
            },
            direccion: {
                required: true,
            },
            contrasena: {
                required: true,
                minlength: 8,
            },
            confcontrasena: {
                required: true,
                equalTo: "#contrasena",
            },
        },
        messages: {
            rut: {
                required: "El RUT es un campo obligatorio",
                rutChileno: "El formato del rut no es válido",
            },
            nombres: {
                required: "Su nombre es un campo obligatorio",
            },
            apellidos: {
                required: "Su apellido es un campo obligatorio",
            },
            email: {
                required: "El correo es un campo obligatorio",
                email: "El correo no cumple con el formato",
            },
            direccion: {
                required: "La dirección es un campo obligatorio"
            },
            contrasena: {
                required: "La contraseña es una campo obligatorio",
                minlength: "Mínimo 8 caracteres",
            },
            confcontrasena: {
                required: "Repita la contraseña anterior",
                equalTo: "Debe ser igual a la contraseña anterior",
            },
        },
    });
});       
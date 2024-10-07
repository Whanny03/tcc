document.addEventListener("DOMContentLoaded", function() {
    const emailCard = document.getElementById("email-card");
    const passwordCard = document.getElementById("password-card");
    const successCard = document.getElementById("success-card");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const nextStepBtn = document.getElementById("next-step");
    const loginBtn = document.getElementById("login");

    // Evento de continuação após inserir e-mail
    nextStepBtn.addEventListener("click", function() {
        if (emailInput.value) {
            // Esconde o primeiro card com transição de dropdown
            emailCard.style.transition = "all 0.7s cubic-bezier(0.19, 1, 0.22, 1)";
            emailCard.style.transform = "translateY(-500px)";
            emailCard.style.opacity = "0";

            setTimeout(() => {
                emailCard.classList.add("hidden");
                passwordCard.classList.remove("hidden");

                // Mostra o segundo card vindo de baixo
                passwordCard.style.transition = "all 0.7s cubic-bezier(0.19, 1, 0.22, 1)";
                passwordCard.style.transform = "translateY(0)";
                passwordCard.style.opacity = "1";
            }, 700);
        } else {
            alert("Por favor, insira um e-mail válido.");
        }
    });

    // Evento de login após inserir a senha
    loginBtn.addEventListener("click", function() {
        if (passwordInput.value) {
            // Esconde o segundo card com transição de subida
            passwordCard.style.transition = "all 0.7s cubic-bezier(0.19, 1, 0.22, 1)";
            passwordCard.style.transform = "translateY(500px)";
            passwordCard.style.opacity = "0";

            setTimeout(() => {
                passwordCard.classList.add("hidden");
                successCard.classList.remove("hidden");

                // Mostra o terceiro card vindo da direita
                successCard.style.transition = "all 0.7s cubic-bezier(0.19, 1, 0.22, 1)";
                successCard.style.transform = "translateX(0)";
                successCard.style.opacity = "1";
            }, 700);

            // Simula o redirecionamento após 3 segundos
            setTimeout(() => {
                window.location.href = "index.html";
            }, 3000);
        } else {
            alert("Por favor, insira sua senha.");
        }
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById("editEmployeeModal");
    const closeModal = document.querySelector(".close");

    document.querySelectorAll('.edit-btn').forEach(button => {
        button.addEventListener('click', function () {
            modal.style.display = "block";
        });
    });

    closeModal.onclick = function () {
        modal.style.display = "none";
    };

    window.onclick = function (event) {
        if (event.target === modal) {
            modal.style.display = "none";
        }
    };
});

function openEditModal(id, surname, firstname, email, totalLeave, plannedLeave) {
    document.getElementById("editId").value = id;
    document.getElementById("editSurname").value = surname;
    document.getElementById("editFirstname").value = firstname;
    document.getElementById("editEmail").value = email;
    document.getElementById("editTotalLeave").value = totalLeave;
    document.getElementById("editPlannedLeave").value = plannedLeave;
    
    document.getElementById("editModal").style.display = "flex"; // Affiche le modal
}

// Fermer le popup en cliquant sur la croix
document.querySelector(".close").addEventListener("click", function() {
    document.getElementById("editModal").style.display = "none";
});

// Fermer le popup en cliquant en dehors du contenu
window.onclick = function(event) {
    let modal = document.getElementById("editModal");
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

document.getElementById("editForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Empêche le rechargement de la page

    // Récupérer les valeurs du formulaire
    let id = document.getElementById("editId").value;
    let surname = document.getElementById("editSurname").value;
    let firstname = document.getElementById("editFirstname").value;
    let email = document.getElementById("editEmail").value;
    let totalLeave = document.getElementById("editTotalLeave").value;
    let plannedLeave = document.getElementById("editPlannedLeave").value;

    // Création de l'objet de données
    let updatedData = {
        surname: surname,
        firstname: firstname,
        email: email,
        total_leave_days: totalLeave,
        planned_leave_days: plannedLeave
    };

    // Envoi des données via fetch API
    fetch(`/update_employee/${id}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(updatedData)
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message); // Message de succès ou d'erreur
        document.getElementById("editModal").style.display = "none"; // Fermer le modal
        location.reload(); // Recharger la page pour voir les modifications
    })
    .catch(error => console.error("Error:", error));
});
function deleteEmployee(id) {
    if (confirm("Are you sure you want to delete this employee?")) {
        fetch(`/delete_employee/${id}`, {
            method: "DELETE"
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message); // Message de confirmation
            location.reload(); // Recharger la page pour voir les changements
        })
        .catch(error => console.error("Error:", error));
    }
}

var deleteButton = document.querySelector("#delete"); // delete button

deleteButton.addEventListener("click", function (ev) {
  var confirmDelete = confirm("Are you sure you want to delete this Place?"); // Confirm dialog
  if (!confirmDelete) {
    ev.preventDefault(); // Prevent form from submitting if the user does not confirm
  }
});

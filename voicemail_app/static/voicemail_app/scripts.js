document.addEventListener("DOMContentLoaded", function () {
  // Function to get CSRF token from cookies
  function getCSRFToken() {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, 10) === "csrftoken" + "=") {
          cookieValue = decodeURIComponent(cookie.substring(10));
          break;
        }
      }
    }
    return cookieValue;
  }

  // Event listener for the Review & Send button to show modal with form data
  $("#confirmModal").on("show.bs.modal", function (event) {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var toNumber = $("#toNumber").val();
    var voicemail = $("#messageText").val();
    // Update modal content with the form data
    var modal = $(this);
    modal.find(".modal-body #modalToNumber").text(toNumber);
    modal.find(".modal-body #modalMessageText").text(voicemail);
  });

  // Event listener for the Confirm & Send button inside the modal
  $("#confirmSend").click(function () {
    var toNumber = $("#toNumber").val();
    var voicemail = $("#messageText").val();
    console.log("sending-call in scripts.js file");
    // AJAX call to send the voicemail
    $.ajax({
      url: "/voicemail_app/send_voicemail/",
      type: "POST",
      headers: { "X-CSRFToken": getCSRFToken() },
      data: JSON.stringify({
        to_number: toNumber, // Pass fromNumber to match server-side
        voicemail: voicemail, // Rename voicemail to match server-side
        is_text: true,
      }),
      contentType: "application/json",
      dataType: "json",
      success: function (response) {
        console.log("Voicemail sent successfully!");
        $("#voicemailForm")[0].reset();
        $("#confirmModal").modal("hide");
      },
      error: function (xhr) {
        if (xhr.status === 400) {
          alert(
            "Failed to send voicemail: Please ensure all fields are correctly filled."
          );
        } else if (xhr.status === 500) {
          alert("Failed to send voicemail: An internal error occurred.");
        } else {
          alert("Failed to send voicemail. Please try again.");
        }
      },
    });
  });
});

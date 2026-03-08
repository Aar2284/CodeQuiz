document.addEventListener('DOMContentLoaded', function() {
    // Check if resultModal exists (passed via context and rendered in template)
    var resultModalEl = document.getElementById('resultModal');
    if (resultModalEl && typeof bootstrap !== 'undefined') {
        var myModal = new bootstrap.Modal(resultModalEl);
        myModal.show();
    }
});

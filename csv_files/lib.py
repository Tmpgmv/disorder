import os
from stat import S_IREAD

def make_file_readonly_callback(sender, instance, created, **kwargs):
    """
    Makes the uploaded CSV file read‑only after the CsvFile instance is saved.
    """

    # Only run on new objects.
    if not created:
        return

    # If the file field is empty, skip.
    if not instance.file:
        return

    # Build absolute filesystem path.
    # model.FileField.path is always absolute.
    file_path = instance.file.path

    # Check that file exists.
    if not os.path.exists(file_path):
        return

    # Make file read‑only for the owner (on Unix‑like) and “read‑only” in practice.
    # Adjust mask as needed depending on your OS.
    os.chmod(file_path, S_IREAD)  # owner read‑only

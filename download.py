from huggingface_hub import snapshot_download

# Variable für die Modell-ID
model_id = input("Bitte geben Sie die Modell-ID ein: ")

# Download des Modells
snapshot_download(
    repo_id=model_id, 
    local_dir="model",
    local_dir_use_symlinks=False, 
    revision="main"
)

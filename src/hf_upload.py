from huggingface_hub import HfApi, upload_folder

def push_dataset(local_folder: str, repo_id: str):
    api = HfApi()
    api.create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True)
    upload_folder(repo_id=repo_id, repo_type="dataset", folder_path=local_folder)
    return f"https://huggingface.co/datasets/{repo_id}"

def push_model(local_folder: str, repo_id: str):
    api = HfApi()
    api.create_repo(repo_id=repo_id, repo_type="model", exist_ok=True)
    upload_folder(repo_id=repo_id, repo_type="model", folder_path=local_folder)
    return f"https://huggingface.co/{repo_id}"

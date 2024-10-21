from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_files():
    return [{"filename": "file1.txt"}, {"filename": "file2.txt"}]

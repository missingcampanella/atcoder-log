import requests
import shutil
from pathlib import Path

def fetch_difficulty_data():
    url = "https://kenkoooo.com/atcoder/resources/problem-models.json"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"取得失敗: {e}")
        return None

def get_problem_files(directory: str) -> list[Path]:
    dir_path = Path(directory)
    return [file for file in dir_path.iterdir() if file.is_file()]

def get_color_folder(difficulty) -> str:
    if difficulty is None:
        return "unclassified"
    if difficulty < 400:
        return "gray"
    elif difficulty < 800:
        return "brown"
    elif difficulty < 1200:
        return "green"
    elif difficulty < 1600:
        return "cyan"
    elif difficulty < 2400:
        return "blue"
    elif difficulty < 2800:
        return "yellow"
    elif difficulty < 3200:
        return "orange"
    else:
        return "red"

def normalize_problem_id(problem_id: str, data: dict) -> str:
    if problem_id in data:
        return problem_id
    
    mapping = {"a": "1", "b": "2", "c": "3", "d": "4"}
    parts = problem_id.split("_")
    
    if len(parts) == 2 and parts[1] in mapping:
        converted = parts[0] + "_" + mapping[parts[1]]
        if converted in data:
            return converted
    
    return problem_id

def main(source_dir: str, dest_base_dir: str):
    data = fetch_difficulty_data()
    if data is None:
        print("データが取得できませんでした")
        return

    files = get_problem_files(source_dir)

    for file in files:
        problem_id = file.stem
        normalized_id = normalize_problem_id(problem_id, data)
        info = data.get(normalized_id)
        difficulty = info.get("difficulty") if info else None
        folder_name = get_color_folder(difficulty)

        dest_dir = Path(dest_base_dir) / folder_name
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest_path = dest_dir / file.name

        if file.exists() and file != dest_path:
            shutil.move(str(file), str(dest_path))
            print(f"移動完了: {file.name} -> {folder_name}")

if __name__ == "__main__":
    main(
        source_dir="./atcoder-sorter",
        dest_base_dir="./difficulty"
    )
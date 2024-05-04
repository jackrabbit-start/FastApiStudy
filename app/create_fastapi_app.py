#!usr/bin/python
import os
import sys

# 스크립트의 위치를 파이썬의 모듈 검색 경로에 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def create_files(folder_name, file_names):
    script_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app"
    )
    for file_name in file_names:
        with open(os.path.join(script_dir, folder_name, f"{file_name}.py"), "w") as f:
            pass


def create_folder(folder_name):
    try:
        script_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "app"
        )
        os.makedirs(os.path.join(script_dir, folder_name))
        print(f"폴더 '{folder_name}'가 생성되었습니다.")
    except OSError as e:
        print(f"폴더 생성 실패: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용법: python createfolder.py [폴더 이름]")
        sys.exit(1)
    folder_name = sys.argv[1]
    create_folder(folder_name)
    file_names = [
        "__init__",
        "constants",
        "controllers",
        "dependencies",
        "models",
        "schemas",
        "services",
    ]
    create_files(folder_name, file_names)

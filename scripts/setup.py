from pathlib import Path


def main():
    for i in range(1, 26):
        if i < 10:
            Path(f"../days/day0{i}").mkdir(parents=True, exist_ok=True)
            Path(f"../days/day0{i}/.gitkeep").touch()
        else:
            Path(f"../days/day{i}").mkdir(parents=True, exist_ok=True)
            Path(f"../days/day{i}/.gitkeep").touch()

if __name__ == "__main__":
    print("Creating directories...")
    main()

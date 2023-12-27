import time
import os
import subprocess


def time_decorator(func):
    """
    A decorator that measures the execution time of a function.

    Parameters:
    func (function): The function to be decorated.

    Returns:
    tuple: A tuple containing the result of the function and the time taken to execute it.
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_taken = end_time - start_time
        return result, time_taken

    return wrapper


@time_decorator
def run_subprocess(*args, **kwargs):
    return subprocess.run(*args, **kwargs)


def is_male_filename(filename):
    if "K" in filename:
        return False
    return True


def test_gender_recognition(data_dir, gender_recognition_script):
    """
    Test the gender recognition script on a directory of audio files.

    Args:
        data_dir (str): The directory path containing the audio files.
        gender_recognition_script (str): The path to the gender recognition script.

    Returns:
        None
    """
    files = os.listdir(data_dir)
    correct_count = 0
    total_count = 0
    times = []

    for file in files:
        if file.endswith(".wav"):
            file_path = os.path.join(data_dir, file)
            expected_is_male = is_male_filename(file)

            result, time_taken = run_subprocess(
                ["python", gender_recognition_script, file_path],
                capture_output=True,
                text=True,
            )

            detected_gender = result.stdout.strip()
            detected_is_male = detected_gender == "M"

            if detected_is_male == expected_is_male:
                correct_count += 1
            total_count += 1

            times.append(time_taken)

            print(f"File: {file}", end="\t")
            print(f"Expected: {'Man' if expected_is_male else 'Woman'}", end="\t")
            print(f"Detected: {'Man' if detected_is_male else 'Woman'}", end="\t\t")
            if detected_is_male != expected_is_male:
                print("ERROR", end="\t")
            else:
                print("OK", end="\t")
            print(f"Time taken: {time_taken:.3f}s")

    accuracy = correct_count / total_count * 100
    print(f"Accuracy: {accuracy:.3f}%")
    print(f"Average time taken: {sum(times)/len(times):.3f}s")


def main():
    # Modify the following variables as needed
    data_dir = "./../trainall"
    gender_recognition_script = "gender_recognition_by_voice.py"

    test_gender_recognition(data_dir, gender_recognition_script)


if __name__ == "__main__":
    main()

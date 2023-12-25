import time

def write_text2file(filename_w, text_w):
    for t in range(1, 2000):
        try:
            with open(filename_w, 'w') as file_handle:
                file_handle.write(str(text_w))
            break
        except:
            time.sleep(0.01)  # 20 секунд выполнения
            continue
    return


def read_text_from_file(TextFileName):
    for _ in range(3):
        try:
            with open(TextFileName, "r") as file:
                text = file.read()
                return text
        except FileNotFoundError:
            time.sleep(0.01)
    return ''
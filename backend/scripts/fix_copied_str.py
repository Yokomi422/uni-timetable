import sys
import unicodedata

argc, argv = len(sys.argv), sys.argv


def fix_copied_str():
    """
    argv[1]には修正したい文字列のfilepathを指定

    copyした文字列に対して、以下の処理をする
    - 改行を\nに変換
    - 全角空白を半角空白に変換
    -
    """
    if argc != 2:
        print("Usage: python fix_copied_str.py filename")
        sys.exit(1)  # 0は正常終了.  1は以上終了

    filename = argv[1]

    with open(filename, "r") as f:
        text = f.read()

    # 全角空白を半角空白に変換
    # 参考 https://note.nkmk.me/python-unicodedata-normalize/#unicode
    text = unicodedata.normalize("NFKC", text)

    # 改行を削除
    text = text.replace("\n", r"\n")
    print(text)


fix_copied_str()

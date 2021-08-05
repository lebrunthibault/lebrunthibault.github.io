import glob

import markdown


def build_algolia_index():
    for filename in glob.glob(".\\content\\post\\*.md"):
        print(filename)
        with open(filename, "r") as f:
            md_content = f.read().split("---")[-1]

        md = markdown.Markdown(md_content, extensions=['toc'])
        print(md)
        return
        # html = markdown.markdown(your_text_string)


    # md = markdown.Markdown(extensions=['toc'])


if __name__ == "__main__":
    build_algolia_index()

import glob
import json
import os
import sys
from os.path import realpath, dirname, basename

import frontmatter
import markdown

from dotenv import load_dotenv

from algoliasearch.search_client import SearchClient

project_root = dirname(dirname(realpath(__file__)))

load_dotenv()


def flatten(list: list) -> list:
    return [item for sublist in list for item in sublist]


def get_headers_name(header_info: dict) -> list:
    names = [header_info["name"].split("{#")[0].strip()]
    if header_info.get("children"):
        return names + flatten(
            [get_headers_name(header_info=sub_header_info) for sub_header_info in header_info.get("children")])
    else:
        return names


def get_document_headers(content: str):
    md = markdown.Markdown(extensions=['toc'])
    md.convert(content)
    return flatten([get_headers_name(header_info=header_info) for header_info in md.toc_tokens])


def get_document_info(post: frontmatter.Post, filename: str):
    title: str = post.get('title')
    if not title:
        return None
    path = basename(filename).replace(".md", "")
    return {
        "objectID": title,
        "title": title,
        "description": post.get("description"),
        "keywords": post.get("keywords"),
        "headers": get_document_headers(post.content),
        "draft": post.get("draft", False),
        "url": f"/post/{path}"
    }

def push_settings(index):
    with open(f"{project_root}/algolia/settings.json") as f:
        settings = json.loads(f.read())
    res = index.set_settings(settings)
    print("settings pushed")

def index_documents_in_algolia():
    documents_info = []
    for filename in glob.glob(f"{project_root}/content/post/**/*.md"):
        post = frontmatter.load(filename)
        document_info = get_document_info(post=post, filename=filename)
        if document_info:
            documents_info.append(document_info)

    client = SearchClient.create(os.environ.get("ALGOLIA_APP_ID"), os.environ.get("ALGOLIA_ADMIN_KEY"))
    index = client.init_index(os.environ.get("ALGOLIA_INDEX_NAME"))
    settings = index.get_settings()
    res = index.replace_all_objects(documents_info)
    print(res.responses)
    print(f"{len(documents_info)} documents pushed to index {index.name}")

    push_settings(index)


if __name__ == "__main__":
    index_documents_in_algolia()

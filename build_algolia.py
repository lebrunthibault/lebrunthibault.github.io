import glob
import json
import os
import sys

import frontmatter
import markdown

from dotenv import load_dotenv

from algoliasearch.search_client import SearchClient

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


def get_document_info(post: frontmatter.Post):
    return {
        "objectID": post.get("title"),
        "title": post.get("title"),
        "description": post.get("description"),
        "summary": post.get("summary"),
        "keywords": post.get("keywords"),
        "headers": get_document_headers(post.content)
    }


def index_documents_in_algolia(build_drafts):
    documents_info = []

    for filename in glob.glob(".\\content\\post\\*.md"):
        print(filename)
        post = frontmatter.load(filename)
        if not post.get("draft") or build_drafts:
            documents_info.append(get_document_info(post))

    client = SearchClient.create(os.environ.get("ALGOLIA_APP_ID"), os.environ.get("ALGOLIA_ADMIN_KEY"))
    index = client.init_index(os.environ.get("ALGOLIA_INDEX_NAME"))
    res = index.replace_all_objects(documents_info)
    print(res.responses)
    with open("./debug.json", "w") as f:
        f.write(json.dumps(documents_info))
    print(f"{len(documents_info)} documents pushed to index {index.name}")



if __name__ == "__main__":
    build_drafts = os.environ.get("ENV") == "dev"
    index_documents_in_algolia(build_drafts=build_drafts)

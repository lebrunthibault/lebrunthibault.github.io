# From least integrated / flexible to most integrated

- SAAS Rest API
- Library install (via pip)
- Forked library install
- Library install in local
- Code copy paste



| Method                 | Setup                                 | Updates from upstream                     | Modification          |
| ---------------------- | ------------------------------------- | ----------------------------------------- | --------------------- |
| SAAS Rest API          | A bit slow                            | Automatic and reliable                    | Not possible          |
| Library install        | Fast                                  | Semi automatic and reliable               | Possible only locally |
| Forked library install | Slow (need to setup a package in pip) | Semi automatic and in both repos (slower) | Full                  |
| Library install local  | Fast : git submodule                  | Automatic, quite fast                     | Full                  |
| Library install local  | Fast: git subtree                     | Like git submodule but automatic deploy   | Full                  |
| Code copy paste        | Very fast                             | No updates                                | Full                  |


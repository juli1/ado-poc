# Azure DevOps POC

## Getting your token

Signup for Azure Devops.

Then, generate a token.

See the following pictures as to how to generate the token.

![Generate Token](imgs/token1.png "Generate Token")

## Setup

First, export your token under the variable `ADO_TOKEN`

```shell
export ADO_TOKEN=<your-token>
```

Then, install dependencies

```shell

./bootstrap.sh

```

### Get a code snippet

Edit `code-snippet.py` with the parameters of your repository and run.


### Post a Summary PR comment


Edit `pull-request-summary-comment.py` and run.

![Summary Comment on PR](imgs/summary-comment.png "Summary Comment 1")


### Post a comment in a file


Edit `pull-request-file-comment.py` and run.

![Comment on file, example 1](imgs/file-comment1.png "File Comment 1")
![Comment on file, example 2](imgs/file-comment2.png "File Comment 2")



## Special Thanks

Special thanks to my [Claude.ai](https://claude.ai/) subscription that got this done in 30 mins.
#!/bin/bash
function create() {
    cd 
    python create.py
    cd C:\Users\rutle\OneDrive\Documents\Code Projects\$1
    git init
    git remote add origin https://github.com/rutrut6969/$1.git
    echo > ReadMe.md
    git add .
    git commit -m "Initial Commit"
    git push -u origin master
    code .
}
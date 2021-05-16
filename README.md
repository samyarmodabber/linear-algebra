# Linear Algebra and its Application

This repository holds the Jupyter Book source for `Linear Algebra and its Application`.

You can find the book here:
https://linear-algebra.ir

## 1. To make a change to the book and update

1. Fork the repository:

   ```
   git clone https://github.com/samyarmodabber/linear-algebra
   ```
2. Change the file you wish and commit it to the repository.
3. Make Pull Request.

## 2. Build and preview the book locally

To build locally, 
```
pip install -r requirements.txt
```
and then 
```
jupyter-book build . (Do not forgot point at the end!)

```

## 3. Automatically push your build files with ghp-import

### A. Install ghp-import

```
pip install ghp-import
```

### B. From the master branch of your book’s root directory (which should contain the _build/html folder) call ghp-import and point it to your HTML files, like so:

```
ghp-import -n -p -f _build/html
```
### C.Setup Github page
Select `gh-page` pranch and `docs` in setting of github page of the ripository.

**Follow the build instructions on the Jupyter Book guide**. The guide has
information for how to use the Jupyter Book CLI to build this book. You can find
the [Jupyter Book build instructions here](https://jupyterbook.org/start/build.html).

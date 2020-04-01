## Python documentation

1. Write docstrings in your classes, functions and methods

Use triple-quoted strings at the start of the thing you are documenting. Follow the Sphinx style, 

Examples of writing 
https://www.datacamp.com/community/tutorials/docstrings-python#fifth-sub

If you use one of the other styles, google or numpy, that's fine, but you should pick one and be consistent. If you choose one of the other styles you'll need to add an extension to be able to process it. 

2. pip install sphinx

`pip install sphinx`

https://www.sphinx-doc.org/en/master/index.html

3. Make docs folder and navigate to it

mkdir docs
cd docs 

3. Run the quickstart to set up documentation config files

from the docs folder 

`sphinx-quickstart`

Separate source and build directories: No
Project name: Enter your project's name
Author name(s): your name or your team's names
Project release: press enter here
Language: press enter for English


4. Import your module(s) into conf.py

Inside the docs folder, there's a file called conf.py.

uncomment the first 3 lines, modify the 3rd line (.. not .) 
```
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
```

5. Add the autodoc extension

Open the docs/conf.py file and modify the line that says `extensions = []` to 

```
extensions = [
    'sphinx.ext.autodoc'
]
```


6. set up .rst files with

(make sure you are in the /docs folder)

`sphinx-apidoc -o source/ ../utilities`

Use your own package name 
If you have modules, not a package, then write 

`sphinx-apidoc -o source/ ..`


7. Fix package names in docs/source/???.rst files 

For example, a file like this will be generated,

```
collection\_utilities module
============================

.. automodule:: collection_utilities
   :members:
   :undoc-members:
   :show-inheritance:
```

Change to - note the package name 

```
collection\_utilities module
============================

.. automodule:: utilities.collection_utilities
   :members:
   :undoc-members:
   :show-inheritance:
```

8.  Show your modules documentation on the home page

In docs/index.rst, Add `source/modules`. Watch the indentation, there are 3 spaces at the start of this line

```
Welcome to Utilities!'s documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   source/modules


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```


9. Build documentation from docs folder with 

`make html`

Documentation will be in the form of HTML pages, in _build/html.


10. As you work on project, run 

`make html`

to update your documentation.

If you add new files, repeat the sphinx-autodoc command (steps 6 and 7) to generate documentation for those. 
INSTALLATION
------------

Prerequisites:

- Captcha_solver requires python 3.x
- Install `Google Tesseract OCR <https://github.com/tesseract-ocr/tesseract>`_ 4.0 or greater
  (additional info how to install the engine on Linux, Mac OSX and Windows).
  You must be able to invoke the tesseract command as *tesseract*.
  Under Debian/Ubuntu you can use the package **tesseract-ocr**.
  For Mac OS users please install homebrew package **tesseract**.

After installing Tesseract OCR, you need to download `this trained data file <https://github.com/tesseract-ocr/tessdata_best/raw/master/hat.traineddata>`_ and place it to *tessdata*
folder inside Tesseract-OCR installation directory.

Clone project from github to your local directory

.. code:: bash

    $> git clone https://github.com/prikid/captcha_solver_demo.git

    $> cd captcha_solver_demo && pip install .

To run demo:

.. code:: bash

    $ (env)> python demo/main.py
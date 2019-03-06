from setuptools import setup

setup(
    name='captcha_solver',
    version='0.1',
    packages=['captcha_solver'],
    url='prikid.app',
    license='',
    author='Serhii Riabcheniuk',
    author_email='serhii@prikid.app',
    description='',
    install_requires=[
        'numpy',
        'opencv-python',
        'imutils',
        'pytesseract'
    ],

)
